# Modified from https://github.com/timmmlim/bt4103-junyi

import pandas as pd
import numpy as np
import networkx as nx


def lower_bound_student_exercise_frequencies(log_problem, lower_bound=4):
    """
    Remove the students who took the exercises less than "lower_bound" times.
    For example, if a student only took one problem_id in the exercise, this will not correctly reflect the accuracy of the exercise itself.

    Parameters
    ----------
    log_problem : pd.DataFrame
      The log_problem that is filtered according to the exercise_ids that we want

    lower_bound : int
      The minimum number of problem_ids that a student must take in order to contribute to the mean accuracy of the exercise.
    """
    filtered_df = log_problem.groupby(['uuid', 'ucid'], sort=False)['upid'].count()
    filtered_df = filtered_df[filtered_df > lower_bound].reset_index().drop(columns=['upid'], axis=1)
    log_problem_filtered = log_problem.merge(filtered_df, left_on=['uuid', 'ucid'], right_on=['uuid', 'ucid'],
                                             how='right')
    return log_problem_filtered


def create_graphing_dataframe(flp):
    # create SUM student performance for each student on a particular exercise
    student_sum_performance = flp.groupby(['uuid', 'ucid'], sort=False)['is_correct'].sum().reset_index().rename(
        columns={'is_correct': 'sum_is_correct'})
    # Remove duplications of students and exercise since we aggregated the result in the df above
    flp_student_sum_performance = flp.drop_duplicates(subset=['uuid', 'ucid']).merge(student_sum_performance,
                                                                                     left_on=['uuid', 'ucid'],
                                                                                     right_on=['uuid', 'ucid'])

    # create the dataframe to create our graph
    user_to_content_student_performance = flp_student_sum_performance.groupby(['uuid'], sort=False)['ucid'].apply(
        lambda x: x.tolist()).reset_index()
    user_to_content_student_performance['individual_sum_score'] = \
    flp_student_sum_performance.groupby(['uuid'], sort=False)['sum_is_correct'].apply(lambda x: x.tolist()).values

    # # need to remove students who only took one exercise, since they do not contribute to edge weight
    user_to_content_student_performance = user_to_content_student_performance[
        user_to_content_student_performance['ucid'].apply(lambda x: len(x) > 1)]
    user_to_content_student_performance['from'] = user_to_content_student_performance['ucid'].apply(lambda x: x[:-1])
    user_to_content_student_performance['to'] = user_to_content_student_performance['ucid'].apply(lambda x: x[1:])
    user_to_content_student_performance['individual_sum_score_to'] = user_to_content_student_performance[
        'individual_sum_score'].apply(lambda x: x[1:])
    return user_to_content_student_performance[['uuid', 'from', 'to', 'individual_sum_score_to']]


def create_networkx_graph(user_to_content_student_performance):
    """
    Create the graph according to the given inputs that contains uuid, from, to, individual_sum_score_to

    Parameters
    ----------
    user_to_content_student_performance : pd.DataFrame
      The dataframe that we created using create_graphing_dataframe(flp)

    Returns
    G: NetworkXGraph
      The graph has edge attributes:
        1. number_of_individual_students from src to target node
        2. sum_of_correct_problems from src to target node
        3. average_score_from_src_to_tgt (part A in diagram)
        4. average_performance_tgt (Part B in diagram)
        5. final_average_performance (Part C in diagram)
    """
    graph = nx.DiGraph()
    for index, row in user_to_content_student_performance.iterrows():
        user = row['uuid']
        from_list = row['from']
        to_list = row['to']
        individual_sum_score_to = row['individual_sum_score_to']
        # always check that the number
        for src, tgt, score in zip(from_list, to_list, individual_sum_score_to):
            if graph.has_edge(src, tgt):
                graph[src][tgt]['number_of_individual_students'] += 1
                graph[src][tgt]['sum_of_correct_problems'] += score
            else:
                graph.add_edge(src, tgt, sum_of_correct_problems=score, number_of_individual_students=1)
    return get_true_edge(graph)


def get_true_edge(G):
    """
    Using the auxillary edge weights, create the final weight as shown in the diagram above

    Parameters
    ----------
    G: NetworkXGraph

    Returns
    -------
    G: NetworkXGraph
      This graph now has additional edge attributes :
        1. average_score_from_src_to_tgt (part A in diagram)
        2. average_performance_tgt (Part B in diagram)
        3. final_average_performance (Part C in diagram)
    """
    # calculate the average performance. handles part A
    average_score_from_src_to_tgt_dic = {(u, v): (dic['sum_of_correct_problems'] / dic['number_of_individual_students'])
                                         for u, v, dic in G.edges(data=True)}
    nx.set_edge_attributes(G, average_score_from_src_to_tgt_dic, 'average_score_from_src_to_tgt')

    # calculate the average performance of the target. handles part B
    def calc_average_performance_on_tgt(node):
        lst = list(map(lambda x: x[2], G.in_edges(node, data='average_score_from_src_to_tgt')))
        return np.mean(lst) if len(lst) > 0 else 0

    average_performance_on_tgt = {node: calc_average_performance_on_tgt(node) for node in G.nodes()}
    nx.set_node_attributes(G, average_performance_on_tgt, 'average_performance_tgt')

    # calculate the actual weight according to part C
    final_average_performance_dic = {(u, v): (w - G.nodes[v]['average_performance_tgt']) for u, v, w in
                                     G.edges(data='average_score_from_src_to_tgt')}
    nx.set_edge_attributes(G, final_average_performance_dic, 'final_average_performance')
    return G


def get_hubs_and_authorities(graph):
    """
    Calculate the Hubs and Authority scores to identify potential starting and ending exercises

    Parameters
    ----------
    graph: NetworkXGraph

    Returns
    -------
    authorities_hubs: pd.DataFrame
      exercises are ranked according to the highest Hub score and the highest Authority score.
    """
    names = ["Authorities", "Hubs"]
    hits = nx.hits(graph,
                   max_iter=200)  # https://stackoverflow.com/questions/63026282/error-power-iteration-failed-to-converge-within-100-iterations-when-i-tried-t
    all_measures = [hits[1], hits[0]]
    df = pd.concat([pd.Series(measure) for measure in all_measures], axis=1)
    df.columns = names
    authorities_hubs = df[['Authorities', 'Hubs']].sort_values(by='Authorities')
    authorities_hubs['Authorities_Rank'] = authorities_hubs['Authorities'].rank(ascending=False)
    authorities_hubs['Hubs_Rank'] = authorities_hubs['Hubs'].rank(ascending=False)
    return authorities_hubs


def get_top_k_hubs_and_authorities(df, k=5):
    """
    Return the list of potential starting exercises and list of ended exercises

    Parameters
    ----------
    df : pd.DataFrame
      The df that contains the corresponding Hub and Authority scores with their ranks attached to each exercise.

    k : int
      How many starting and ending exercises do we want to consider

    Returns
    -------
    top_k_hubs: list
      list of k potential starting exercises

    top_k_authorities: list
      list of k potential ending exercises
    """
    top_k_hubs = df[df['Hubs_Rank'] <= k]
    top_k_authorities = df[df['Authorities_Rank'] <= k]
    return top_k_hubs, top_k_authorities


def calculate_path_weight(G, path, method='final_average_performance'):
    """
    Parameters
    ----------
    G: NetworkXGraph

    path : list
      An actual path eg [1,2,3]

    method : str
      the edge weight used to calculate the path weights: can be any of the edge attributes mentioned in create_networkx_graph()

    Returns
    -------
    weight : float
      The sum of the the total path cost from start to ending exercise
    """
    weight = 0
    for u, v in zip(path[:-1], path[1:]):
        weight += G[u][v][method]
    return weight


def get_at_least_k_paths(graph, top_k_hubs, top_k_authorities, k=5, verbose=True):
    """
    Parameters
    ----------
    graph: NetworkXGraph

    top_k_hubs : list
      list of k potential starting exercises

    top_k_authorities : list
      list of k potential ending exercises

    k : int
      The maximum number of paths to store and recommend

    verbose : bool
      True for debugging, False otherwise

    Returns
    -------
    paths_to_return: list of list
      The list contains up to k paths
    """
    paths_to_return = []
    for hub in top_k_hubs.index:
        for aut in top_k_authorities.index:
            if hub != aut:
                if verbose:
                    logger.info(f'src: {hub} => tgt: {aut}')
                try:
                    if verbose:
                        logger.info(f'Number of paths: {len(list(nx.all_shortest_paths(graph, hub, aut)))}')
                    for path in nx.all_shortest_paths(graph, hub, aut):
                        if verbose:
                            logger.info(f"Available Paths: {path}")
                        # only add the paths that are of length 4 or more
                        if len(path) >= 4:
                            paths_to_return.append(
                                (path, calculate_path_weight(graph, path, method='final_average_performance')))

                            # if we get the number of paths already, terminate
                            if len(paths_to_return) == k:
                                return paths_to_return
                        if verbose:
                            for ex in path:
                                logger.info(f'Node: {ex}')
                except nx.NetworkXNoPath:
                    if verbose:
                        logger.info('No Path Available')
                    continue
                if verbose:
                    logger.info('=' * 100)
        return paths_to_return


def run_pipeline(log_problem, num_hubs_auth, lower_bound, policy):
    """
    Run the network algorithm
    1. Prune the network by removing students who took only a few problem_id in a exercise
    3. Create the dataframe for graphing
    4. Create the graph
    5. get the potential starting and ending exercises

    Parameters
    ----------
    log_problem: pd.DataFrame
      if recommending for individual clusters(student personas), just filter the log_problem for that specific group/persona

    num_hubs_auth: int
      The parameter to control how many potential starting and ending exercises you want

    lower_bound:
      The parameter to control the number of edges in the network by removing students who took less than lower_bound number of problem in an exercise.

    Returns
    -------
    graph: NetworkXGraph

    top_k_hubs : list
      list of k potential starting exercises

    top_k_authorities : list
      list of k potential ending exercises
    """

    flp = lower_bound_student_exercise_frequencies(log_problem, lower_bound=lower_bound)
    user_to_content_student_performance = create_graphing_dataframe(flp)
    graph = create_networkx_graph(user_to_content_student_performance)
    df = get_hubs_and_authorities(graph)
    top_k_hubs, top_k_authorities = get_top_k_hubs_and_authorities(df, k=num_hubs_auth)
    return graph, top_k_hubs, top_k_authorities


def create_recommend_learning_paths(logs
                                    , num_exercises
                                    , num_paths=5
                                    , policy="popularity"
                                    , student_frequency_lower_bound=11
                                    , verbose=True
                                    ):
    """
    Recommend the learning paths.

    Parameters
    ----------
    logs: list
     List of dicts as rows

    num_exercises: int
      Maximum number of potential nodes

    num_paths: int
      The maximum number of paths that you want to recommend

    policy: string
      The type of edge weight policy to be computed - currently supports "popularity" and "performance"

    student_frequency_lower_bound: int
      The parameter to control the number of edges in the network by removing students who took less than lower_bound number of problem in an exercise.

    verbose: bool
      True if want to debug the number of learning paths being recommended else False

    Returns
    -------
    paths: list of tuple
      returns the list of recommend path so that we can sort according to the path_cost Eg [(path1, path1_cost), (path2, path2_cost)]
    """
    logs = pd.DataFrame(logs)
    graph, top_k_hubs, top_k_authorities = run_pipeline(logs,
                                                        num_hubs_auth=min(10, num_exercises),
                                                        lower_bound=student_frequency_lower_bound,
                                                        policy=policy
                                                        )
    paths = get_at_least_k_paths(graph, top_k_hubs, top_k_authorities, k=num_paths, verbose=verbose)
    logger.info(paths)
    return paths

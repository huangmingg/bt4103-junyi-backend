from internal.db.db import db_instance


def get_logs_by_user(user_list):
    res = db_instance.fetch_rows(f"SELECT * FROM logs WHERE ucid in ({user_list})")
    return res


# Level 3 filter
def get_logs_by_modules(module_list):
    pass


# Level 4 filter
def get_logs_by_chapters(chapter_list):
    pass


# Level 5 filter
def get_logs_by_contents(content_list):
    pass


# Level 6 filter
def get_logs_by_problems(problem_list):
    pass

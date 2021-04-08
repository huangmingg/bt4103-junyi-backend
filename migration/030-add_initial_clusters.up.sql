WITH new_clusters(name, description) AS (
      VALUES
          ('Cluster 0', 'Description of cluster 0'),
          ('Cluster 1', 'Description of cluster 1'),
          ('Cluster 2', 'Description of cluster 2'),
          ('Cluster 3', 'Description of cluster 3'),
          ('Cluster 4', 'Description of cluster 4')
    )
INSERT INTO clusters (
    name
    , description
    , created_at
    , created_by
    , updated_at
    , updated_by
)
SELECT
    name
    , description
    , NOW()
    , 'e0309575@u.nus.edu'
    , NOW()
    , 'e0309575@u.nus.edu'
FROM
    new_clusters;
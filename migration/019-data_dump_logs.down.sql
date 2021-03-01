UPDATE
    logs
SET
    "deleted_at" = NOW()
  , "deleted_by" = 'e0309575@u.nus.edu'
WHERE
    ("deleted_at" IS NULL OR "deleted_at" > NOW())
  AND "created_by" = 'e0309575@u.nus.edu'
  AND "updated_by" = 'e0309575@u.nus.edu'
  AND "batch" = 16
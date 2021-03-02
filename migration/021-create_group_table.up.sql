CREATE TABLE IF NOT EXISTS groups
(
    "id"                    BIGSERIAL PRIMARY KEY,
    "name"                  VARCHAR NOT NULL,
    "created_by"            VARCHAR NOT NULL,
    "created_at"            TIMESTAMPTZ NOT NULL DEFAULT now(),
    "updated_by"            VARCHAR NULL,
    "updated_at"            TIMESTAMPTZ DEFAULT now(),
    "deleted_by"            VARCHAR NULL,
    "deleted_at"            TIMESTAMPTZ NULL
);
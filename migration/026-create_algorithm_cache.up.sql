CREATE TABLE IF NOT EXISTS algorithm_cache
(
    "id"                    BIGSERIAL PRIMARY KEY,
    "uuid"                  BIGSERIAL,
    "cluster"               SMALLINT,
    "bin"                   SMALLINT,
    "created_by"            VARCHAR NOT NULL,
    "created_at"            TIMESTAMPTZ NOT NULL DEFAULT now(),
    "updated_by"            VARCHAR NULL,
    "updated_at"            TIMESTAMPTZ DEFAULT now(),
    "deleted_by"            VARCHAR NULL,
    "deleted_at"            TIMESTAMPTZ NULL,
    CONSTRAINT fk_users FOREIGN KEY (uuid) REFERENCES users(id)
);

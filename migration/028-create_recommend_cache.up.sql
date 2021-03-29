CREATE TABLE IF NOT EXISTS recommend_cache
(
    "id"                    BIGSERIAL PRIMARY KEY,
    "group_id"              BIGSERIAL,
    "cluster"               SMALLINT,
    "content_id"            BIGSERIAL,
    "rank"                  SMALLINT,
    "position"              SMALLINT,
    "policy"                VARCHAR NULL,
    "created_by"            VARCHAR NOT NULL,
    "created_at"            TIMESTAMPTZ NOT NULL DEFAULT now(),
    "updated_by"            VARCHAR NULL,
    "updated_at"            TIMESTAMPTZ DEFAULT now(),
    "deleted_by"            VARCHAR NULL,
    "deleted_at"            TIMESTAMPTZ NULL,
    CONSTRAINT fk_groups FOREIGN KEY (group_id) REFERENCES groups(id),
    CONSTRAINT fk_contents FOREIGN KEY (content_id) REFERENCES contents(id)
);

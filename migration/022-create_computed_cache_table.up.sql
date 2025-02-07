CREATE TABLE IF NOT EXISTS computed_cache
(
    "id"                    BIGSERIAL PRIMARY KEY,
    "uuid"                  BIGSERIAL,
    "problems_attempted"    SMALLINT,
    "exercises_attempted"   SMALLINT,
    "avg_time_per_exercise" DECIMAL,
    "avg_accuracy"          DECIMAL,
    "no_downgrades"         SMALLINT,
    "no_upgrades"           SMALLINT,
    "avg_hint_per_attempt"  DECIMAL,
    "avg_time_btw_problem"  DECIMAL,
    "created_by"            VARCHAR NOT NULL,
    "created_at"            TIMESTAMPTZ NOT NULL DEFAULT now(),
    "updated_by"            VARCHAR NULL,
    "updated_at"            TIMESTAMPTZ DEFAULT now(),
    "deleted_by"            VARCHAR NULL,
    "deleted_at"            TIMESTAMPTZ NULL,
    CONSTRAINT fk_users FOREIGN KEY (uuid) REFERENCES users(id)
);

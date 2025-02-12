CREATE TABLE IF NOT EXISTS group_enrollments
(
    "id"                    BIGSERIAL PRIMARY KEY,
    "group_id"              BIGSERIAL,
    "uuid"                  BIGSERIAL,
    "created_by"            VARCHAR NOT NULL,
    "created_at"            TIMESTAMPTZ NOT NULL DEFAULT now(),
    "updated_by"            VARCHAR NULL,
    "updated_at"            TIMESTAMPTZ DEFAULT now(),
    "deleted_by"            VARCHAR NULL,
    "deleted_at"            TIMESTAMPTZ NULL,
    CONSTRAINT fk_groups FOREIGN KEY (group_id) REFERENCES groups(id),
    CONSTRAINT fk_users FOREIGN KEY (uuid) REFERENCES users(id)
);
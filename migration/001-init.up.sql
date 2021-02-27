
SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

--
-- Name: users; Type: TABLE; Owner: -
--

CREATE TABLE IF NOT EXISTS users
(
    "id"                    BIGSERIAL PRIMARY KEY,
    "name"                  VARCHAR NOT NULL,
    "gender"                VARCHAR,
    "points"                BIGINT NOT NULL DEFAULT 0,
    "badges_cnt"            INT NOT NULL DEFAULT 0,
    "first_login_date_TW"   DATE NOT NULL,
    "user_grade"            INT NOT NULL,
    "user_city"             VARCHAR,
    "is_self_coach"         BOOLEAN NOT NULL DEFAULT FALSE,
    "belongs_to_class_cnt"  INT DEFAULT 0,
    "has_class_cnt"         INT DEFAULT 0,
    "has_teacher_cnt"       INT DEFAULT 0,
    "has_student_cnt"       INT DEFAULT 0,
    "created_by"            VARCHAR NOT NULL,
    "created_at"            TIMESTAMPTZ NOT NULL DEFAULT now(),
    "updated_by"            VARCHAR NULL,
    "updated_at"            TIMESTAMPTZ DEFAULT now(),
    "deleted_by"            VARCHAR NULL,
    "deleted_at"            TIMESTAMPTZ NULL
);


--
-- Name: contents; Type: TABLE; Owner: -
--

CREATE TABLE IF NOT EXISTS contents
(
    "id"                    BIGSERIAL PRIMARY KEY,
    "name"                  VARCHAR NOT NULL,
    "difficulty"            VARCHAR NOT NULL,
    "learning_stage"        VARCHAR NOT NULL,
    "level2_id"             INT NOT NULL,
    "level3_id"             INT NOT NULL,
    "level4_id"             INT NOT NULL,
    "created_by"            VARCHAR NOT NULL,
    "created_at"            TIMESTAMPTZ NOT NULL DEFAULT now(),
    "updated_by"            VARCHAR NULL,
    "updated_at"            TIMESTAMPTZ DEFAULT now(),
    "deleted_by"            VARCHAR NULL,
    "deleted_at"            TIMESTAMPTZ NULL
);


--
-- Name: logs; Type: TABLE; Owner: -
--

CREATE TABLE IF NOT EXISTS logs (
    "id"                                BIGSERIAL PRIMARY KEY,
    "upid"                              INT,
    "ucid"                              BIGSERIAL,
    "uuid"                              BIGSERIAL,
    "attempt_timestamp"                 INT NOT NULL,
    "problem_number"                    SMALLINT NOT NULL,
    "exercise_problem_repeat_session"   SMALLINT NOT NULL,
    "is_correct"                        BOOLEAN NOT NULL,
    "total_sec_taken"                   INT NOT NULL,
    "total_attempt_cnt"                 SMALLINT NOT NULL,
    "used_hint_cnt"                     SMALLINT NOT NULL,
    "is_hint_used"                      BOOLEAN NOT NULL,
    "is_downgrade"                      BOOLEAN,
    "is_upgrade"                        BOOLEAN,
    "user_level"                        SMALLINT NOT NULL,
    "batch"                             SMALLINT,
    "created_by"                        VARCHAR NOT NULL,
    "created_at"                        TIMESTAMPTZ NOT NULL DEFAULT now(),
    "updated_by"                        VARCHAR NULL,
    "updated_at"                        TIMESTAMPTZ DEFAULT now(),
    "deleted_by"                        VARCHAR NULL,
    "deleted_at"                        TIMESTAMPTZ NULL,
    CONSTRAINT fk_users FOREIGN KEY (uuid) REFERENCES users(id),
    CONSTRAINT fk_contents FOREIGN KEY (ucid) REFERENCES contents(id)
);
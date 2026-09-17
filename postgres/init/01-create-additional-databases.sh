#!/bin/bash
# The official postgres image only auto-creates the single database named
# by POSTGRES_DB (set to "auth" in docker-compose.yml). This script runs
# once, on first container start against an empty data directory, to
# create the other two logical databases that tasks-service and
# analytics-service need on the same Postgres server.
set -euo pipefail

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE DATABASE tasks;
    CREATE DATABASE analytics;
EOSQL

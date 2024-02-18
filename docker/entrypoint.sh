#!/bin/bash


if [[ -z "${HOST}" ]]; then
  HOST="0.0.0.0"
else
  HOST="${HOST}"
fi

if [[ -z "${PORT}" ]]; then
  PORT=8080
else
  PORT="${PORT}"
fi

if [[ -z "${DEBUG}" ]]; then
  DEBUG="--no-debug"
else
  DEBUG="${DEBUG}"
fi

python -m flask --app src/app.py run --host=$HOST --port=$PORT $DEBUG

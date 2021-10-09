#!/usr/bin/env bash

#sleep 365d &
tail -f /dev/null &

ps --format pid,ppid,user,args

terminate(){
  kill -s TERM $!
  echo "sleep(pid $!)を途中終了、コンテナ停止。"
}

trap "terminate" TERM


sudo chown dev:dev /home/dev/{app,.vscode-server}

# Install module.
pipenv --venv > /dev/null || pipenv install --skip-lock --dev --ignore-pipfile

if [[ -z "${VIRTUAL_ENV}" ]]; then
  source "$(pipenv --venv)/bin/activate"
fi

wait

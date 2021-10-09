

if [[ -z "${VIRTUAL_ENV}" ]]; then
  source $(pipenv --venv)/bin/activate
fi

alias ll='ls -la'

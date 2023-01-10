#!/bin/bash

cd /application/web

function _runserver() {
  echo "Running server"
  exec python manage.py runserver 0.0.0.0:8000 "$@"
}

function _manage() {
  echo "Migrating"
  exec python manage.py "$@"
}

function _test() {
  echo "Testing:"
  exec pytest "$@"
  #exec python manage.py test --settings=ImageApi.configurations.test_settings --noinput "$@"
}

if [[ $1 == "" ]]; then
  CMD=runserver
else
  CMD=$1
  shift
fi

# Commands:

case $CMD in

  runserver)
      _runserver "$@"
  ;;

  manage)
    _manage "$@"
  ;;

  test)
    _test "$@"
  ;;

esac

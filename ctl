#!/bin/bash

SERVICE_NAME=python

cmd=$1

exec_cmd() {
  docker-compose exec ${SERVICE_NAME} /bin/bash -il -c "$1"
}

shell() {
  docker-compose exec ${SERVICE_NAME} /bin/bash
}

docker-up() {
  docker-compose up -d
}

docker-up-build() {
  docker-compose up -d --build
}

down() {
  docker-compose down
}

downv() {
  docker-compose down -v
}


case $cmd in
   "dub")
	  docker-up-build
      ;;
   "du")
	  docker-up
      ;;
   "dd")
      down
      ;;
   "s")
		  shell
      ;;
   *) 

cat << EOS
[Usage]

  $0 du: docker-compile up -d.

EOS
     ;;
esac

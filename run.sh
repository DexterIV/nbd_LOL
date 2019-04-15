#!/usr/bin/env bash


docker network create localnet
docker run -p 9042:9042 --rm --net localnet --name aCassandra -d cassandra:3.11
docker start aCassandra
# docker exec -it aCassandra bash
cd restapi
docker build -t docker_flask:latest .
docker run -p 9043:9043 --net localnet docker_flask
# Instructions
## Setup 
* setup network with "docker network create localnet" where localnet is some name.
 * run docker cassandra with "docker run -p 9042:9042 --rm --net localnet --name aCassandra -e -d cassandra:3.11"
  where aCassandra is some name.
 * If docker is already connected run "docker start aCassandra"
* To get into docker bash run "docker exec -it aCassandra bash" and to execute queries use cqlsh
* To fill database with starting data use App.java
## RESTAPI

*  build with "docker build -t docker_flask:latest ."
* run with "docker run -p 9043:9043 -- net localnet docker_flask"
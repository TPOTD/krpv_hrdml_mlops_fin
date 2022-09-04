#!/bin/bash

docker service create --replicas 1 --name serving -p 5555:5555 --mount type=bind,src=/opt/models,dst=/models 65.108.82.162:8090/serving
docker service create --replicas 1  --name api -p 5050:5050 --mount type=bind,src=/opt/clusters/,dst=/clusters --host host.docker.internal:host-gateway 65.108.82.162:8090/api
docker service create --replicas 1 --name cluster_service_0 -p 5010:5005 --mount type=bind,src=/opt/clusters/,dst=/clusters -e CLUSTER=0 65.108.82.162:8090/cluster
docker service create --replicas 1 --name cluster_service_1 -p 5011:5005 --mount type=bind,src=/opt/clusters/,dst=/clusters --constraint node.hostname==kcloud-production-user-154-vm-540 -e CLUSTER=1 65.108.82.162:8090/cluster
docker service create --replicas 1 --name cluster_service_2 -p 5012:5005 --mount type=bind,src=/opt/clusters/,dst=/clusters -e CLUSTER=2 65.108.82.162:8090/cluster
docker service create --replicas 1 --name cluster_service_3 -p 5013:5005 --mount type=bind,src=/opt/clusters/,dst=/clusters  -e CLUSTER=3 65.108.82.162:8090/cluster
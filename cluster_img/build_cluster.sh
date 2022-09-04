#!/bin/bash
docker build -t cluster .
docker tag cluster 65.108.82.162:8090/cluster
docker push 65.108.82.162:8090/cluster
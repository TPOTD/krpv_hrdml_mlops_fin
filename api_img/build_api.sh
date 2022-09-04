#!/bin/bash
docker build -t api ./api_img
docker tag api 65.108.82.162:8090/api
docker push 65.108.82.162:8090/api
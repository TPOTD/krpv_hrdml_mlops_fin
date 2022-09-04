#!/bin/bash
docker build -t template ./template_img
docker tag template 65.108.82.162:8090/template
docker push 65.108.82.162:8090/template
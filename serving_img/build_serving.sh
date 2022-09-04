#!/bin/bash
#готовим git для скачивания модели USE
apt install git-lfs
mkdir -p /opt/models
git lfs install || true
git clone https://huggingface.co/sentence-transformers/distiluse-base-multilingual-cased /opt/models/use_model
#строим image с сервингом
docker build -t serving ./serving_img
docker tag serving 65.108.82.162:8090/serving
docker push 65.108.82.162:8090/serving
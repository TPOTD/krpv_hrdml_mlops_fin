from flask import Flask, request, jsonify
import requests
import numpy as np
import json

#загружаем центры кластеров
centers = np.load('/clusters/centers.npy')

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_data():
    query = request.get_data().decode('utf-8')
    #отправляем в serving на энкодинг
    query_emb = requests.post('http://host.docker.internal:5555/process', query).json()
    query_emb = np.array(query_emb['embendings'], dtype='float32')[0]
    #считаем косинусное расстояние с центрами кластеров
    ab = np.sum(query_emb*centers, axis=1)
    norm_a = np.linalg.norm(query_emb)
    norm_b = np.linalg.norm(centers, axis = 1)
    cos_sims = ab / (norm_a * norm_b)
    clstr = np.argmin(cos_sims)
    #костыль - центров кластеров в первом покалении больше чем данных по кластерам
    clstr = 2 if clstr == 4 else clstr
    #отправляем на нужный кластер для поиска матча
    res = requests.post(f'http://host.docker.internal:501{clstr}/find_match', json={'embed':query_emb.tolist()}).json()
    return jsonify(res)
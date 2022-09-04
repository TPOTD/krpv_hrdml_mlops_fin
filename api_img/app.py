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
    query_emb = requests.post('http://host.docker.internal:5555/process', query).json()
    query_emb = np.array(json.loads(query)['embendings'], dtype='float32')[0]
    
    ab = np.sum(query_emb*centers, axis=1)
    norm_a = np.linalg.norm(query_emb)
    norm_b = np.linalg.norm(centers, axis = 1)
    cos_sims = ab / (norm_a * norm_b)
    clstr = np.argmin(cos_sims)
    
    res = requests.post(f'http://host.docker.internal:501{clstr}/find_match', json={'embed':query_emb.tolist()}).json()
    return jsonify(res)
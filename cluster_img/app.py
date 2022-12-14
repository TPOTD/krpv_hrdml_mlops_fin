from flask import Flask, request, jsonify
import joblib
import numpy as np
import json
import os
import faiss

CLUSTER = os.environ['CLUSTER']
#подгружаем FAISS
faiss_ind = joblib.load(f'/clusters/clust{CLUSTER}/faiss')
#подгружаем чистые предложения
with open(f'/clusters/clust{CLUSTER}/sentences.json') as f:
    sentences = json.load(f)

app = Flask(__name__)

@app.route('/find_match', methods=['POST'])
def find_match():
    emb_dict = request.json
    emb = np.array(emb_dict['embed'], dtype='float32')
    #поиск в Faiss
    _, doc = faiss_ind.search(emb.reshape(1,-1),1)
    doc = doc.flatten()
    match = sentences[doc[0]]
    return jsonify({'match':match})
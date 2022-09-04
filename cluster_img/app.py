from flask import Flask, request, jsonify
import joblib
import numpy as np
import json
import os

CLUSTER = os.environ['CLUSTER']
faiss_ind = joblib.load(f'/clusters/clust{CLUSTER}/faiss')
with open(f'/clusters/clust{CLUSTER}/sentences.json') as f:
    sentences = json.load(f)

app = Flask(__name__)

@app.route('/find_match', methods=['POST'])
def find_match():
    emb_dict = request.json
    emb = np.array(emb_dict['embed'], dtype='float32')
    _, doc = faiss_ind.search(emb.reshape(1,-1),1)
    doc = doc.flatten()
    match = sentences[doc[0]]
    return jsonify({'match':match})
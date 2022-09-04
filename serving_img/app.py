from flask import Flask, request, jsonify
import numpy as np
from sentence_transformers import SentenceTransformer
import json

model = SentenceTransformer('/models/use_model')

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_data():
    data = request.get_data().decode('utf-8')
    res = model.encode(json.loads(data)['instances'])
    res = res.tolist()
    return jsonify({'embendings':res})
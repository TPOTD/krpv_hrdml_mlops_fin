import joblib
import faiss
import pickle
import os
import numpy as np

gens = [1,2]
for dg in gens:
    #загружаем предложения по кластерам
    with open(f'clusters_use_dg{dg}.json') as f:
        clusters = json.load(f)
    #загружаем эмбендинги для постройки FAISS
    with open(f'use_embeddings_dg{dg}.pkl', 'rb') as f:
        use_embeddings = pickle.load(f)
    os.makedirs(f'dgs/dg{dg}', exist_ok=True)

    for clust_id in range(4):
        os.makedirs(f'dgs/dg{dg}/clust{clust_id}', exist_ok=True)
        #сохраним предложения по кластерно (файл=кластер)
        with open(f'dgs/dg{dg}/clust{clust_id}/sentences.json', 'w') as f:
            json.dump(clusters[str(clust_id)], f)
        #загружаем все embs кластера
        embs_cluster = np.vstack([use_embeddings[clusters[str(clust_id)][i]] for i in range(len(clusters[str(clust_id)]))])
        #создаем FAISS
        faiss_ind = faiss.IndexFlatL2(512)
        faiss_ind.add(embs_cluster)
        #сохраняем FAISS
        joblib.dump(faiss_ind, f'dgs/dg{dg}/clust{clust_id}/faiss')
    
    #загружаем центры кластеров чтобы сохранить покластерно
    with open(f'clusters_centers_use_dg{dg}.pkl', 'rb') as f:
        centers = pickle.load(f)
        centers = np.array([centers[i] for i in centers.keys()])
        np.save(f'dgs/dg{dg}/centers', centers)
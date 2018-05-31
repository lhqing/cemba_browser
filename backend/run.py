from flask import Flask, render_template, jsonify, request
import requests
from random import randint
from flask_cors import CORS
from db.query_compute_db import *


app = Flask(__name__,
            static_folder="../dist/static",
            template_folder="../dist")
#if app.debug:
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    # cors is for allowing other origin (e.g. the node.js server from frontend dev)
    # to access apis in backend. If close, only flask server can use api


@app.route('/api/random')  # toy api for test
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)


@app.route('/api/tsne')
def cell_tsne():
    response = {
        'dataset': get_cell_tsne()
    }
    return jsonify(response)


@app.route('/api/cluster')
def cell_cluster():
    dataset, tree = get_cell_tsne_cluster()
    response = {
        'dataset': dataset,
        'cluster_tree': tree
    }
    return jsonify(response)


@app.route('/api/gene_list')
def gene_id_list():
    data_list = get_gene_name_dict()
    response = {
        'dataset': data_list
    }
    return jsonify(response)


@app.route('/api/gene/', methods=['GET'])
def gene_mc():
    gene_id = request.args.get('gene_id')
    gene_name = request.args.get('gene_name')
    mc_type = request.args.get('mc_type')
    mc_type = mc_type if mc_type is not None else 'ch'

    norm_mc = request.args.get('normalize')
    norm_mc = False if norm_mc is not None and norm_mc[0].lower() == 'f' else True

    cov_cutoff = request.args.get('cov_cutoff')
    cov_cutoff = int(cov_cutoff) if cov_cutoff is not None else 5

    print(request.args)

    gene_df, gene_info = get_gene_data(db_names=['3C', '4B'],
                                       gene_id=gene_id,
                                       gene_name=gene_name,
                                       mc_type=mc_type,
                                       norm_mc=norm_mc,
                                       cov_threshold=cov_cutoff,
                                       return_df=True)
    tsne_df = get_cell_tsne(return_df=True)
    total_df = pd.concat([tsne_df, gene_df], axis=1).dropna(how='any')
    data_list = [['_id', 'tsne_2_1', 'tsne_2_2', 'cov', 'mc_rate', 'pass']]
    for index, row in total_df.iterrows():
        data_list.append([index]+row.tolist())
    response = {
        'dataset': data_list,
        'gene_info': gene_info
    }
    return jsonify(response)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    # because we use vue-router html5 history mode,
    # we will point any backend routes into index.html,
    # and let vue-router to handle

    if app.debug:
        # if app is in debug mode, let flask proxy front-end server
        text = requests.get('http://localhost:8080/{}'.format(path)).text
        # this makes flask server been able to proxy front-end server,
        # therefore we cau use frontend updates without run npm build
        return text
    return render_template("index.html")






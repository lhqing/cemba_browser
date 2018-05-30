from pymongo import MongoClient
import pandas as pd
import os

CWD = os.getcwd()
CLIENT_LINK = 'mongodb://gale-cluster-2.salk.edu:27270/'

CLIENT = MongoClient(CLIENT_LINK)
print(CWD)
gene_ref_table = pd.read_table(CWD+'/static/gencode.vM16.annotation.sorted.flat.gene_only.gtf', index_col='gene_id')

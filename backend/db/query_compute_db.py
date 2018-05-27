from .settings import *

MOP_DB = CLIENT['MOp']


def get_cell_tsne(db=MOP_DB, cell_list=None):
    """

    :param db:
    :param cell_list:
    :return: [['_id', 'tsne_2_1', 'tsne_2_2']]
    """
    tsne_collection = db['cell_tsne']
    cursor = tsne_collection.find({})
    data_list = [['_id', 'tsne_2_1', 'tsne_2_2']]
    if cell_list is None:
        for doc in cursor:
            data_list.append([doc['_id']] + doc['tsne_2d'])
    else:  # change this to $in
        cell_set = set(cell_list)
        for doc in cursor:
            if doc['_id'] in cell_set:
                data_list.append([doc['_id']] + doc['tsne_2d'])
    return data_list

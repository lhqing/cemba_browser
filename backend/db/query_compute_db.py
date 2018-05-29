from .settings import *
import pandas as pd
from collections import defaultdict

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


def get_cluster_tree(cluster_df, root_name):
    dedup_cluster_df = cluster_df.drop_duplicates().astype(object)
    child_list = None
    first = True
    for i in range(0, dedup_cluster_df.columns.size - 1, 1):
        pair_cluster_dict = defaultdict(set)
        pair_cols = dedup_cluster_df.iloc[:, [i, i + 1]]
        if first:
            first = False
            for _, row in pair_cols.iterrows():
                pair_cluster_dict[row.iloc[1]].add(row.iloc[0])
            child_list = []
            for parent, child in pair_cluster_dict.items():
                child = list(child)
                if len(child) == 1:
                    temp_dict = {'name': str(i + 1) + '_' + str(parent),
                                 'value': int((cluster_df.iloc[:, i + 1] == parent).sum())}
                else:
                    temp_dict = {'name': str(i + 1) + '_' + str(parent),
                                 'children': [{'name': str(i) + '_' + str(c),
                                               'value': 0} for c in child]}
                child_list.append(temp_dict)
        else:
            for _, row in pair_cols.iterrows():
                pair_cluster_dict[row.iloc[1]].add(row.iloc[0])

            new_child_list = []
            for parent, child in pair_cluster_dict.items():
                child_names = [str(i) + '_' + str(c) for c in child]
                child_dict_list = [child_dict for child_dict in child_list
                                   if child_dict['name'] in child_names]
                if len(child_dict_list) == 1:
                    temp_dict = child_dict_list[0]
                    if 'children' in temp_dict:
                        if len(temp_dict['children']) == 1:
                            temp_dict = temp_dict['children'][0]
                    temp_dict.update(name=str(i + 1) + '_' + str(parent))
                    new_child_list.append(temp_dict)
                else:
                    new_child_list.append({'name': str(i + 1) + '_' + str(parent),
                                           'children': child_dict_list})
            child_list = new_child_list
    root_dict = {'name': root_name,
                 'children': child_list}
    return root_dict


def get_cell_tsne_cluster(db=MOP_DB):
    tsne_collection = db['cell_tsne']
    cluster_collection = db['cell_cluster']

    data_list = [['_id', 'tsne_2_1', 'tsne_2_2']]
    cursor = tsne_collection.find({})
    for doc in cursor:
        data_list.append([doc['_id']] + doc['tsne_2d'])
    tsne_df = pd.DataFrame(data_list[1:], columns=data_list[0])
    tsne_df.set_index('_id', inplace=True)
    cluster_series = []
    cursor = cluster_collection.find({})
    for doc in cursor:
        s = pd.Series(doc['cluster'], name=doc['_id'])
        cluster_series.append(s)
    cluster_df = pd.DataFrame(cluster_series)
    total_df = pd.concat([cluster_df, tsne_df], axis=1).dropna(how='any')
    data_list = [['_id'] + total_df.columns.tolist()]
    for index, row in total_df.iterrows():
        data_list.append([index] + row.tolist())

    tree = get_cluster_tree(cluster_df, 'MOp')
    return data_list, tree
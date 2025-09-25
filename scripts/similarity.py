# -*- coding: utf-8 -*-

import argparse
import requests
from odps import ODPS
import re
from urllib.parse import quote
import argparse
import json
import random
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(o):
    

    sql = """
    """
    
    print(sql)
    input_table = o.execute_sql(sql)
    

    output_table = o.get_table("")
    write_partition = f'pt=""'
    output_table.delete_partition(write_partition, if_exists=True)
    output_table.create_partition(partition_spec=write_partition, if_not_exists=True)
    
    data_list = []
    with input_table.open_reader() as reader:
        for record in reader:
            feature_str = record.feature.strip('[]')
            if feature_str.startswith('[') and feature_str.endswith(']'):
                feature_str = feature_str.strip('[]')
            feature_array = np.fromstring(feature_str, sep=' ')
            data_list.append({
                'id': record.id,
                'feature': feature_array
            })
    
    

    features = np.array([item['feature'] for item in data_list])
    ids = [item['id'] for item in data_list]
    

    similarity_matrix = cosine_similarity(features)
    

    with output_table.open_writer(partition=write_partition, create_partition=False) as writer:
        n = len(data_list)
        for i in range(n):
            for j in range(i+1, n):
                similarity_score = float(similarity_matrix[i, j])
                write_record = [ids[i], ids[j], similarity_score]
                print(f"write: {write_record}")
                writer.write(write_record)
    

def main(augments):
    calculate_similarity(o)

def get_odps_parse_args():
    """
    :return:
    """
    parser = argparse.ArgumentParser(description='offline data to qa dataset')

if __name__ == '__main__':
    odps_args = get_odps_parse_args()
    o = ODPS(odps_args.access_id, odps_args.access_key, odps_args.project, odps_args.endpoint)
    
    args = parse_args()
    main(args)

import time
from json import dumps
from random import randrange
import uuid
from genData import gen_data
from elasticsearch import Elasticsearch

import logging
def connect_elasticsearch():
    _es = Elasticsearch([{
        'host': 'es-gsu.eastus.cloudapp.azure.com',
        'port': 9200,
        'http_auth': ("elastic","helloworld@123")
        }])
    if _es.ping():
        print('Connected')
    else:
        print('it could not connect!')
    return _es

def create_index(index_name):
    _es = connect_elasticsearch()
    _es.indices.create(index=index_name,ignore=400)
    return _es


def put_document(data,index):
    id = uuid.uuid1()
    return _es.create(document=data, index=index, id=id.int)
    # _es.bulk(body=data,index=index)


def get_document(index_name,id):
    return _es.get(index=index_name,id=id)

def get_all(inde_name):
    return _es.search(index=inde_name,query={"match_all": {}})


if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    _es = None
    index_name = 'radon-project'
    _es = create_index(index_name)


    while True:
        data = gen_data()
        for record in data:
            res = put_document(record,index_name)
            print(res['result'],record)
        time.sleep(5)

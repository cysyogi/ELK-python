import time
from json import dumps
from random import randrange
import uuid
from genData import gen_data
from elasticsearch import Elasticsearch

import logging
def connect_elasticsearch():
    _es = Elasticsearch([{
        'host': '192.168.58.19',
        'port': 9200,
        'http_auth': ("elastic","helloworld")
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
    _es.create(document=data, index=index, id=id.int)
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

    data = gen_data()
    while True:
        for record in data:
            put_document(dumps(record),index_name)
        time.sleep(5)

import os
import requests
import json
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_elasticsearch_socket(host):
    r = requests.get('http://127.0.0.1:9200')
    data = r.json()
    assert data['name'] == 'bullseye'

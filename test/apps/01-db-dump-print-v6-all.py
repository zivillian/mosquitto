#!/usr/bin/env python3

from mosq_test_helper import *

def do_test(file, stdout):

    cmd = ['../../apps/db_dump/mosquitto_db_dump',
            f'db_dump/{file}'
            ]

    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=1, encoding='utf-8')
    if res.stdout != stdout:
        raise mosq_test.TestError

stdout = """Mosquitto DB dump
CRC: 0
DB version: 6
DB_CHUNK_CFG:
	Length: 16
	Shutdown: 1
	DB ID size: 8
	Last DB ID: 208508774941868
DB_CHUNK_BASE_MSG:
	Length: 85
	Store ID: 208508774941868
	Source Port: 1883
	Source MID: 1
	Topic: (null)
	QoS: 1
	Retain: 1
	Payload Length: 7
	Expiry Time: 0
	Payload: message
DB_CHUNK_CLIENT:
	Length: 34
	Client ID: single-all
	Last MID: 1
	Session expiry time: 0
	Session expiry interval: 4294967295
DB_CHUNK_CLIENT_MSG:
	Length: 26
	Client ID: single-all
	Store ID: 208508774941868
	MID: 1
	QoS: 1
	Retain: 0
	Direction: 1
	State: 11
	Dup: 0
DB_CHUNK_SUB:
	Length: 27
	Client ID: single-all
	Topic: topic
	QoS: 1
	Subscription ID: 0
	Options: 0x00
DB_CHUNK_RETAIN:
	Length: 8
	Store ID: 208508774941868
"""
do_test('v6-single-all.test-db', stdout)
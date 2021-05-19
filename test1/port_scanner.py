#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ip - хост, который необходимо просканировать
# begin_port - начала диапозона портов для сканирования
# end_port - конец диапозона портов для сканирования


import asyncio
import json
from pprint import pprint


async def port_probe(ip, port):
    try:
        reader, writer = await asyncio.open_connection(ip, port)
        writer.close()
        state = 'open'
    except Exception as err:
        state = 'close'
    
    finally:
        pass

    return {'port' : port, 'state' : state}


async def scan(ip, begin_port, end_port):
    ports = range(begin_port, end_port + 1)
    futs = [port_probe(ip, port) for port in ports]
    ports_list = list()

    for fut in asyncio.as_completed(futs):
        ports_list.append(await fut)

    json_list = json.dumps(sorted(ports_list, key=lambda k: k['port']))
    
    return json_list, len(ports_list)


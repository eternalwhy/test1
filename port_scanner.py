#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ip - хост, который необходимо просканировать
# begin_port - начала диапозона портов для сканирования
# end_port - конец диапозона портов для сканирования


import asyncio
import json
from pprint import pprint

ip = '192.168.1.227'
begin_port = 1
end_port = 25


async def port_probe(loop, ip, port):
    try:
        reader, writer = await asyncio.open_connection(ip, port)
        # status = (True, port, writer.get_extra_info('peername')[0])
        writer.close()
        state = 'open'
    except Exception as err:
        # status = ('Err', port, err)
        state = 'close'
    
    finally:
        # print (status)
        pass

    return {'port' : port, 'state' : state}


async def scan():
    ports = range(begin_port, end_port + 1)
    futs = [port_probe(loop, ip, port) for port in ports]
    ports_list = list()

    for fut in asyncio.as_completed(futs):
        ports_list.append(await fut)

    json_list = json.dumps(sorted(ports_list, key=lambda k: k['port']))
    
    return json_list

loop = asyncio.get_event_loop()
json_ports_list = loop.run_until_complete(scan())
loop.close()

pprint (json_ports_list)

#!/usr/bin/env python3
# coding: utf-8

import asyncio
# import logging
from aiohttp import web
from port_scanner import scan

# log = logging.getLogger(__name__)


async def port_scan(request):
    logger      = request.app['logger']
    ip          = str(request.match_info['ip'])
    begin_port  = int(request.match_info['begin_port'])
    end_port    = int(request.match_info['end_port'])

    # print (request.__dir__())

    logger.info(f'Сканируем IP:{ip}, порты с {begin_port} по {end_port}')

    data, ports_count = await scan(ip, begin_port, end_port)

    logger.info(f'Просканировано {ports_count} портов')



    return web.json_response(data)

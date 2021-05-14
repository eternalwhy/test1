#!/usr/bin/env python3
# coding: utf-8

import asyncio
from aiohttp import web

from port_scanner import scan

async def port_scan(request):
    
    ip          = str(request.match_info['ip'])
    begin_port  = int(request.match_info['begin_port'])
    end_port    = int(request.match_info['end_port'])

    data = await scan(ip, begin_port, end_port)

    return web.json_response(data)

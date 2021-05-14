#!/usr/bin/env python3
# coding: utf-8

import asyncio
import logging
# import sys

from aiohttp import web
from routes import setup_routes

def init():

    app = web.Application()

    setup_routes(app)

    return app

def main():
    logging.basicConfig(level=logging.DEBUG)

    loop = asyncio.get_event_loop()

    app = init()
    
    web.run_app(app, host='0.0.0.0', port=8080)
    # web.run_app(app, path='/tmp/aiosock.sock')

if __name__ == '__main__':
    print ('\n'*5)
    main()
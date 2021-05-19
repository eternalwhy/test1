#!/usr/bin/env python3
# coding: utf-8

from views import port_scan

# GET /scan/<ip>/<begin_port>/<end_port>

def setup_routes(app):
    app.router.add_get('/scan/{ip}/{begin_port}/{end_port}', port_scan, name='port_scan')

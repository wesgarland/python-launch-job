#! /usr/bin/env python3
#
# @file         
# @author       Wes Garland, wes@distributive.network
# @date         March 2024
#

import pythonmonkey as pm
import asyncio

async def go():
    try:
        dcpConfig = pm.globalThis.dcpConfig
        url = pm.eval("""'use strict';
const { getenv } = dcp['dcp-env'];
const { DcpURL } = dcp['dcp-url'];
const url = new globalThis.URL(getenv('URL') || dcpConfig.scheduler.location.href);
url;
""")
        print(url.href);
    except Exception as e:
        print("trapped exception", e)

dcp_client = pm.require('dcp-client')
dcp_client['init'](go) 
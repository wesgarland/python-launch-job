#! /usr/bin/env python3
#
# @file         ping.py
#               Simple python program to connect to the job submit daemon, ping
#               it at the application layer, and close the connection.
# @author       Wes Garland, wes@distributive.network
# @date         March 2024
#

import pythonmonkey as pm
import asyncio

async def go():
    dcpConfig = pm.globalThis.dcpConfig
    Connection = pm.globalThis.dcp.protocol.Connection
    target = (dcpConfig.scheduler.services.jobSubmit)
    conn = pm.new(Connection)(target)
    conn.state.on("change", lambda state, unused: print("connection to", target.location.href, "now", state))
    conn.connect()
    await conn.keepalive()
    conn.close()

dcp_client = pm.require('dcp-client/index.py') # should be just dcp-client, see pm issue 247
dcp_client['init'](go)

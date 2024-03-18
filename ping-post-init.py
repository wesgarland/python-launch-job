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
    target = dcpConfig.scheduler.services.jobSubmit
    conn = pm.new(Connection)(target)

    conn.on("error",              lambda error:    print("! connection error:", error))
    conn.on("ready",              lambda:          print("! connection ready"))
    conn.on("session",            lambda unused:   print("! session established", conn.dcpsid))
    conn.on("end",                lambda:          print("! connection closing"))
    conn.on("close",              lambda *args:    print("! connection closed"))
    conn.on("disconnect",         lambda location: print("! transport layer disconnected from", location))
    conn.on("connect",            lambda location: print("! transport layer connected to", location))
    conn.on("connectionProgress", lambda obj:      print("! connection progress", obj))
# BUG under 5.3 !!!      conn.on("beforeSend",         lambda message:  print("! sending message", message)) 
    conn.on("beforeSend",         lambda message:  print("! sending", message.type))

    conn.state.on("change", lambda state, unused: print("! connection to", target.location.href, "now", state))
    print('connecting');
    await conn.connect()
    print('connected, sending keepalive');
    await conn.keepalive()
    print('received keepalive response; closing');
    conn.close()
    print('connection closed, exiting');

dcp_client = pm.require('dcp-client/index.py') # should be just dcp-client, see pm issue 247
dcp_client['init']()
#go()

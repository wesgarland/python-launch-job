#! /usr/bin/env python

import pythonmonkey as pm

async def go():
    pm.eval("""'use strict;'
const timers = dcp['dcp-timers'];
timers.setInterval(() => console.log(Date.now()/1000), 2000);
""");

dcp_client = pm.require('dcp-client')
dcp_client['init'](go)

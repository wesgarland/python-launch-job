#! /usr/bin/env python3
#
# @file         xhr-fetch.py
#               Example showing how to use XHR via dcp-client
# @author       Wes Garland, wes@distributive.network
# @date         March 2024
#

import pythonmonkey as pm
import asyncio

async def go():
    try:
        dcpConfig = pm.globalThis.dcpConfig
        pm.eval("""'use strict';
const { getenv } = dcp['dcp-env'];
const {
        reallyJustFetch,
        justFetchPrettyError,
      } = dcp['utils'];
const url = (getenv('URL') || dcpConfig.scheduler.location.href) + '/etc/dcp-config.js';

reallyJustFetch(url)
  .then(request => console.log(`rjf fetched ${request.responseText.length} chars, status =`, request.status))
  .catch(error => console.log('rjf error', justFetchPrettyError(error)))
""")
    except Exception as e:
        print("trapped exception", e)

dcp_client = pm.require('dcp-client')
dcp_client['init'](go)

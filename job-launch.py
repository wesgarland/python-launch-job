#! /usr/bin/env python3

import pythonmonkey as pm
import asyncio

def run_job():
    compute = pm.globalThis.dcp.compute
    job = compute['for']([1,2,3], "(x) => 3 * x");
    job.exec();
    
dcp_client = pm.require('dcp-client/index.py') # should be just dcp-client, see pm issue 247
dcp_client['init'](run_job)

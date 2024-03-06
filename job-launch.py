#! /usr/bin/env python3
#
# @file         job-launch.py
#               Simple python program to launch a trivial DCP job
# @author       Wes Garland, wes@distributive.network
# @date         March 2024
#

import pythonmonkey as pm
import asyncio

async def run_job():
    dcp = pm.globalThis.dcp
    job = dcp.compute['for']([1,2,3], "(x) => 3 * x");  # (input set, work function)
    job.on("readystatechange", lambda state: print ("ready state change:", state))
    job.on("accepted",         lambda x:     print ("job accepted, id", job.id))
    job.on("result",           lambda res:   print ("got result for slice number", res.sliceNumber))
    results = await job.exec();
    print("job", job.id, "finished")
    print("results:", results)

dcp_client = pm.require('dcp-client/index.py') # should be just dcp-client, see pm issue 247
dcp_client['init'](run_job)

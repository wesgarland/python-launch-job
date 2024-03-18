#! /usr/bin/env python3
#
# @file         job-launch.py
#               Simple python program to launch a trivial DCP job
# @author       Wes Garland, wes@distributive.network
# @date         March 2024
#
# note - needs DCP_INITIATOR_530=1 until dcp bundle is fixed
#
import pythonmonkey as pm

async def run_job():
    compute = pm.globalThis.dcp.compute
    input_set = [ 3,4,5 ]
    work_fn = "(x) => { progress(); return 3 * x }"
    job = compute['for'](input_set, work_fn)
    job.public.name = "pythonmonkey test job"
    job.on("readystatechange", lambda state: print ("ready state change:", state))
    job.on("accepted",         lambda x:     print ("job accepted, id", job.id))
    job.on("result",           lambda res:   print ("got result for slice number", res.sliceNumber))
    results = await job.exec();
    results = pm.eval('Array.from')(results) # dcp-client bug, this should not be necessary
    print("job", job.id, "finished")
    print("results:", results)
    pm.eval('console.log')(results)

dcp_client = pm.require('dcp-client/index.py') # should be just dcp-client, see pm issue 247
dcp_client['init'](run_job)

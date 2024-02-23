Quick demo which uses PythonMonkey to load dcp-client and launch a job.

This demo program (not yet working) shows basically how to load dcp-client into a python program and use the API.

The API should be usable from either Python or pm.eval(js);

Steps to create this demo:
 - git init
 - npm i dcp-client   (actually I used ../dcp-client because the prod dcp-client doesn't have pythonmonkey support yet)
 - pip install pythonmonkey
 - emacs job-launch.py (etc)

Steps to rebuild dcp-client bundle (only if installed from git directory)
 - get dcp building once via build-dev-platform in ~/git/dcp
 - (cd node_modules/dcp-client && build/bundle --dcp=~/git/dcp --build=debug) every change

Steps to run demo:
 - ./job-launch.py


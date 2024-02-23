Quick demo which uses PythonMonkey to load dcp-client and launch a job.

Steps to create this demo:
 - git init
 - npm i dcp-client   (actually I used ../dcp-client because the prod dcp-client doesn't have pythonmonkey support yet)
 - pip install pythonmonkey
 - pminit npm i crypto-browserify # should not be necessary, pythonmonkey's package.json should have this
 - emacs job-launch.py

Steps to rebuild dcp-client bundle:
 - get dcp building once via build-dev-platform in ~/git/dcp
 - (cd node_modules/dcp-client && build/bundle --dcp=~/git/dcp --build=debug) every change

Steps to run demo:
 - ./job-launch.py


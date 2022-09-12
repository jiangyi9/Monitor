docker run --name=dockerMonitor monitor:v1
sleep 2s
docker rm -f $(docker ps -a |  grep "mon*"  | awk '{print $1}')

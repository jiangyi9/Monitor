docker run --name=dockerMonitor monitor:v1
docker cp dockerMonitor:$(awk '$1 ~ /WORKDIR/ {print $2}' Dockerfile)/cubeLocation.json $(pwd)/cubeLocation.json
docker rm -f $(docker ps -a |  grep "mon*"  | awk '{print $1}')
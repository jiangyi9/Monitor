sleep 0.5s
docker cp $(pwd)/pic.png dockerMonitor:$(awk '$1 ~ /WORKDIR/ {print $2}' Dockerfile)/pic.png

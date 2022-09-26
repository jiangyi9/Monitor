sleep 0.5s
docker cp $(pwd)/img.png dockerMonitor:$(awk '$1 ~ /WORKDIR/ {print $2}' Dockerfile)/img.png

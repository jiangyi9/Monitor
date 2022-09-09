sleep 0.5s
docker cp /home/jelly/Desktop/Monitor/pic.png dockerMonitor:/home/jelly/Desktop/Monitor/pic.png
sleep 2.5s
docker cp dockerMonitor:/home/jelly/Desktop/Monitor/numpyData.json /home/jelly/Desktop/Monitor/numpyData.json

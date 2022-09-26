

# Developer Document for the Monitoring System



### How to use the monitoring system

First, we run the following command to build a docker image called "monitor:v1"

```
docker build -t monitor:v1 .
```

After successfully running this command, you will see a docker image called "monitor" with the tag "v1".

<img src="./dev_document_img/build_image.png" style="zoom: 67%;" />



Now, the docker image has been build.

Next, we run the following command to start the monitoring system.

```
parallel sh ::: run_docker.sh update_data.sh
```



Note: make sure you have put the screenshot of the webcam into the folder "monitor", and name it as "pic.png" before running the "parallel" command.

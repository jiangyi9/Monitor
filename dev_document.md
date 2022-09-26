

# Document of the Monitoring System for Developers



### Prerequisites

You have to install  `parallel` by entering the following command.

```
sudo apt-get -y install parallel
```



### Modify the WORKDIR in the Dockerfile

To successfully run the system, you have to change the path of WORKDIR in the Dockerfile.



Open the `Dockerfile`, you can find a line with `WORKDIR `. For example, I put the `monitor` folder on my Desktop (`/home/jelly/Desktop`), therefore my `WORKDIR ` should be written as:

```
WORKDIR /home/jelly/Desktop/Monitor
```

You should change the path of `WORKDIR` according to your own settings. (you must use the absolute path here)



### How to use the monitoring system

First, we input the following command to build a docker image called `monitor:v1`

```
docker build -t monitor:v1 .
```

After successfully running this command, you will see a docker image called `monitor` with the tag `v1`.

<img src="./dev_document_img/build_image.png" style="zoom: 67%;" />



Now, the docker image has been build.

Next, we input the following command to start the monitoring system.

```
# Switch the directory to your WORKDIR. 
# For example, the below command is: `cd /home/jelly/Desktop/Monitor` on my computer.
cd ${WORKDIR}   
parallel sh ::: scripts/run_docker.sh scripts/update_pic.sh
```

After successfully running this command, a new file `cubeLocation.json` will be generated in the project folder `Monitor`.






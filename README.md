# GCP-deploy

## deploy Google Cloud


### tutorial

https://cloud.google.com/sdk/docs/install-sdk?hl=pt-br

https://www.youtube.com/watch?v=7-s5ugThckY


### To download the Linux file, run the following command:

    curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-473.0.0-linux-x86_64.tar.gz

### To extract the contents of the file to the file system (preferably to the main directory), run the following command: 

    tar -xf google-cloud-cli-473.0.0-linux-x86_64.tar.gz

### 1: 

    cd google-cloud-sdk/

    

### 2

    ./install.sh

### 3 open another terminal: 

    ./google-cloud-sdk/bin/gcloud init

----------

### 4 How to initialize the gcloud CLI in project path

    gcloud init

## Deploy

    gcloud run deploy --source .





    

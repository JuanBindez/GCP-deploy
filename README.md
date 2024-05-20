# GCP-deploy
deploy Google Cloud

## gcloud init

### run this will initate the gcloudcli to ask you for authentication details and configuration


https://cloud.google.com/sdk/docs/install-sdk?hl=pt-br

https://www.youtube.com/watch?v=7-s5ugThckY


### Para fazer o download do arquivo do Linux, execute o seguinte comando:

    curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-473.0.0-linux-x86_64.tar.gz

### Para extrair o conteúdo do arquivo para o sistema de arquivos (preferencialmente para o diretório principal), execute o seguinte comando: 

    tar -xf google-cloud-cli-473.0.0-linux-x86_64.tar.gz

### Adicione a CLI gcloud ao caminho. Execute o script de instalação na raiz da pasta que você extraiu usando o comando a seguir: 

    ./google-cloud-sdk/install.sh

### Isso também pode ser feito de maneira não interativa (por exemplo, com um script) e fornecendo preferências como sinalizações. Para ver as flags disponíveis, execute::

    ./google-cloud-sdk/install.sh --help

###   Para inicializar a CLI gcloud, execute o comando gcloud init: 

    ./google-cloud-sdk/bin/gcloud init

----------


### Como inicializar a CLI gcloud

    gcloud init

## Deploy

    gcloud run deploy --source .





    

# Docker for Predictive Clinical Neuroscience Toolkit

## INTRODUCTION
We created a docker for the Predictive Clinical Neuroscience software toolkit by Andre Marquand ([PCN github](https://github.com/amarquand/PCNtoolkit))

## INSTALATION

First you need to make sure docker is in your system. Otherwise install it from [docker.com](https://docs.docker.com/get-docker/)
 

**i)** Type the following command on the terminal in order to download the latest image from the official **dockerhub** server:

```
docker pull noemigl/pcntoolkit:v2
```

**ii)** Build the image:

```
docker build -t noemigl/pcntoolkit:v2
```

**iii)** Run a container with a link to the location of data in your local machine (-v argument). This data folder must contain files: covariates_allpatients.txt, covariates_HC.txt, features_allpatients.txt, features_HC.txt

```
docker run -v /path/to/the/data/dir:/mnt/data -h master --privileged -it noemigl/pcntoolkit:v2 bash
```

## Once within the docker

#### With CV
Run the script "normative.py" with python, pointing to your data (mounted) with the arguments specifiying training covariates and training response variables. The -k argument specifies the partitions in cross validation.
```
/opt/conda/bin/python pcntoolkit/normative.py -c /mnt/data/covariates_HC.txt -k 3 /mnt/data/features_HC.txt
```

#### Without CV
The same as before but specifying as well the test filepaths. Here we won't use the -k argument (by default it is 1).
```
/opt/conda/bin/python pcntoolkit/normative.py -c /mnt/data/covariates_HC.txt -t /mnt/data/covariates_allpatients.txt -r /mnt/data/features_allpatients.txt /mnt/data/features_HC.txt
```

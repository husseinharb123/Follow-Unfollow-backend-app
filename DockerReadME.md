# (build, push ,pull) docker image workflow 

## `step 1   create a dockerfile `
1. open the project folder 
1. create  a file and name it **Dockerfile**
2. then add the following script :

```
FROM python:3-alpine

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["-m", "openapi_server"]

```

## `step 2   build the docker image `
1. create  a file and name it **.dockerignore** and write the file or fol/ders names and file types that you want to  ignore some when buidling the image
2. run the follwing command to include  all the necessary dependencies in requirements file :
   ```
   pip freeze >requirements.txt
   ```
3. run the following command  to start building the image:
   ```
   docker build -t myapp .
   ```
## `step 3   create a container for image using docker compose or cmd`
`You can run the following command`
```
docker run -d  -p5000:5000 myapp
```
`or`
1. create a yaml file called **docker-compose**
2. add the following scritp:

```
version: '3'
services:
  myappcon:
    image: myapp
    ports:
      - 5000:5000

```
3. run the following commmand :
```
docker-compose  -f docker-compose.yaml up

```


## `push the image to docker hub `
1. create a docker hub account 
2. create a reppsitory and name it **myimageapp**
3. then type the follwing commands :
    ```
    docker login --username=username --password-stdin=password 
    docker images to lookup  images
    
    tag your image 
     
    docker tag myapp <husseinharb123/myapp>
    docker push <husseinharb123/myapp>

    ```
## ` pull your image and use it  `
using the following command :
```
docker pull husseinharb123/myapp
```
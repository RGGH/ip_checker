[![Python application](https://github.com/RGGH/ip_checker/actions/workflows/python-app.yml/badge.svg)](https://github.com/RGGH/ip_checker/actions/workflows/python-app.yml)
<br>
# ip subnet ovelap checker
### FastAPI API checking subnet conflicts
#### Front end + API

* Download repo
* Start Uvicorn server
* Open index.html
  
  see : https://github.com/tiangolo/fastapi#run-it<br>
  to create your own Docker images check out : https://www.youtube.com/watch?v=p28piYY_wv8&t=9690s
---
## Try it out in Docker:

### How to get and run the image:
<br>(where 'redandgreen/subnet-api' is the REPOSITORY and '1' is the TAG):

    docker pull redandgreen/subnet-api
    docker run -it -p 8000:8000 -p 8080:8080 redandgreen/subnet-api:1
![img](https://github.com/RGGH/ip_checker/blob/main/misc/docker_run.png) 
---
#### How to access the api and the GUI
* Once you are running the docker image: 
* use http://127.0.0.1:8000/v1 for the api (see screenshot above for how to create the payload)
* or http://127.0.0.1:8080 in your browser to view the GUI 
---
![img1](https://github.com/RGGH/ip_checker/blob/main/misc/ssx.png)
![img](https://github.com/RGGH/ip_checker/blob/main/misc/screenshot.png)


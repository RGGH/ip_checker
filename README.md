[![Python application](https://github.com/RGGH/ip_checker/actions/workflows/python-app.yml/badge.svg)](https://github.com/RGGH/ip_checker/actions/workflows/python-app.yml)
<br>
# ip_checker
### FastAPI API checking subnet conflicts
#### Front end + API

* Download repo
* Start Uvicorn server
* Open index.html
  
  see : https://github.com/tiangolo/fastapi#run-it
  to create your own Docker images check out : https://www.youtube.com/watch?v=p28piYY_wv8&t=9690s
---
## Try it out in Docker:

##### How to get the image (where 'img2' is the image name):

    docker pull redandgreen/subnet-api:1
    docker run -it -p 8000:8000 -p 8080:8080 img2

Run the docker image and use 127.0.0.1:8000/v1 for the api and port 8080 for in your browser
---
![img1](https://github.com/RGGH/ip_checker/blob/main/misc/ssx.png)
![img](https://github.com/RGGH/ip_checker/blob/main/misc/screenshot.png)


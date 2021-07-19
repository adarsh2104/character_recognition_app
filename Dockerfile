#FROM python:3.7
#RUN apt-get update && apt-get install -y --no-install-recommends apt-utils > /dev/null
#RUN apt-get install -y build-essential tcl
#RUN apt-get install -y systemd-sysv
#RUN apt-get update  > /dev/null
#RUN apt-get install  -y wget > /dev/null
#RUN apt-get install  -y zip > /dev/null
#RUN apt-get install  -y libaio1 > /dev/null
#RUN apt-get update > /dev/null
#RUN apt-get install  -y alien > /dev/nullARG DEBIAN_FRONTED=noninteractive

#WORKDIR /
#RUN mkdir /code
#WORKDIR /code
#COPY . .
#RUN pip install -r requirements.txt
#RUN pip install --upgrade pip --user
#WORKDIR /code/web_app
#ENTRYPOINT ["make"]

# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
#WORKDIR  web_app
COPY requirements.txt requirements.txt
#RUN source venv/bin/activate
COPY . .
RUN pip3 install -r requirements.txt
WORKDIR  web_app
CMD [ "python3" , "webapp/start_server.py", "--host=0.0.0.0"]


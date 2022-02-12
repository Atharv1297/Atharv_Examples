FROM ubuntu

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN apt update -y
RUN apt upgrade -y
RUN apt install python3-pip -y
RUN pip install -r requirements.txt 
# copy every content from the local file to the image
COPY . /app

RUN python3 app.py
  #  It will create docker image and then we can create docker container
   # from this and run our application or edit whatever we want 
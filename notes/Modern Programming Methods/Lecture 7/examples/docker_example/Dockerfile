# set base image to build on
FROM python:3.8

# set/create current working directory inside container
WORKDIR /example

# copy a file from the host to the container
COPY requirements.txt .

# run a shell command
RUN pip install -r requirements.txt

# default command to run when container starts
ENTRYPOINT python 
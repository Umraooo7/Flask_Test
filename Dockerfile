# our base image
FROM alpine:3.5

# Install python ans pip
RUN apk add --update py2-pip

# upgrade pip
RUN pip install --upgrade pip

# install python modules needed by the python app
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# copy files required for the app to run
COPY app.py /usr/src/app/
COPY templates/HelloWorld.html /usr/src/app/TestProject/templates
COPY templates/hello.html /usr/src/app/TestProject/templates

# tell the port number the container should expose
EXPOSE 5000

# run the application
CMD ["python","/usr/src/app/app.py"]

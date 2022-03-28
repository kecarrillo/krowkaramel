# To build this:
# docker build -t [tag] [destination]

# To run the container:
# docker run -d -P [tag]

# Pull base image
FROM python:3.9

# info displayable with :
# docker inspect --format="{{json .Config.Labels}}" [tag]
LABEL app.name="krowkaramel" \
      app.version="1.0" \
      app.description="Site e-commerce krowkaramel." \
      app.author="kevin.carrillo75@yahoo.com"

# Set environnment variable
# No .pyc files:
ENV PYTHONDONTWRITEBYTECODE 1
# Python console :
ENV PYTHONBUFFERED 1

# Set work directory
WORKDIR /krowkaramel

# Install dependencies
COPY Pipfile Pipfile.lock /krowkaramel/
RUN pip install --upgrade pip
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /krowkaramel/

EXPOSE 8000:8000

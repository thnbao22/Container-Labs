# Base image
FROM ubuntu
MAINTAINER Charles Thien
# Install dependencies
RUN apt-get update
RUN apt-get install -y python3

COPY hello.py .
ENTRYPOINT ["python3"]
CMD ["hello.py"]
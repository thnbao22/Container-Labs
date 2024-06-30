# Pull Ubuntu base image with tag 18.04
FROM ubuntu:18.04

# Set non-interactive frontend
ENV DEBIAN_FRONTEND=noninteractive

# Install Apache, PHP and necessary dependencies
RUN apt-get update && \
		apt-get -y install apache2 \
		php libapache2-mod-php && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the welcome.php file to the Docker image		
COPY welcome.php /var/www/html

# Set working directory
WORKDIR /var/www/html

# Expose Apache
EXPOSE 80

# Start Apache
ENTRYPOINT ["apache2ctl", "-D", "FOREGROUND"]
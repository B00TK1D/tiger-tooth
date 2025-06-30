FROM debian:bullseye

# Install dependencies
RUN apt-get update && \
    apt-get install -y python3 shellinabox && \
    apt-get clean

# Copy the Python script and entrypoint
COPY ./src /opt/src
COPY entrypoint.sh /opt/entrypoint.sh
COPY darkmode.css /opt/darkmode.css
RUN chmod +x /opt/entrypoint.sh

# Shell-in-a-box config to run our Python script
RUN mkdir -p /etc/shellinabox
RUN echo "--no-beep --disable-ssl --css=/opt/darkmode.css --service=/:root:root:/root:/opt/entrypoint.sh" > /etc/default/shellinabox

# Expose web terminal port
EXPOSE 4200

CMD ["shellinaboxd", "--no-beep", "--disable-ssl", "--css=/opt/darkmode.css", "--service=/:root:root:/root:/opt/entrypoint.sh"]

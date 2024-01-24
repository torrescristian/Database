FROM bitnami/couchdb:latest

### Change user to perform privileged actions
USER 0
### Install dependencies
### Move your application into the container
### Change user to the default non-root user
# USER 1001 - ## Railway Throws permission error if this is enabled

### Modify the ports used by NGINX by default
# ENV COUCHDB_PORT_NUMBER=1234 # It is also possible to change this environment variable at runtime
# EXPOSE 1234

### Modify the default configuration file
COPY couchdb/custom.ini /opt/bitnami/couchdb/etc/local.d/10-custom.ini

EXPOSE 5984 4369 9100
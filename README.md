# persona_finance

Separate development and production environments and builds

Development:

- Uses default flask web server
- Uses volume to store app
- Assigns root user within container

Production

- Uses gunicorn web server and [nginx](https://www.patricksoftwareblog.com/how-to-configure-nginx-for-a-flask-web-application/) for reverse proxy to allow handling of client requests and serving up static files
- Implements [Docker](https://mherman.org/presentations/dockercon-2018/#74) multi-stage build to reduce production image size by using a builder to build Python wheels and then copying over into final production image

Base build originally inspired by [Michael Herman's Dockerizing Flask with Postgres, Gunicorn, and Nginx](https://github.com/testdrivenio/flask-on-docker) blog post on [testdriven.io](https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/#docker)

# Currently working on ./services/web/app/**init**.py to create home page

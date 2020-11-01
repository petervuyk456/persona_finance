# persona_finance

Separate development and production environments and builds

To start this application with test data, modify the `.db.env` and `.dev.env` files with your information and then move them into an `environments` folder in the base directory.

Once your environment variables have been set, run the following command to build a detached instance of the docker project:
```
docker-compose up -d --build
```

Base build originally inspired by [Michael Herman's Dockerizing Flask with Postgres, Gunicorn, and Nginx](https://github.com/testdrivenio/flask-on-docker) blog post on [testdriven.io](https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/#docker)

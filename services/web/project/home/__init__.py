def create_module(app, **kwargs):
    from .controllers import home_blueprint
    app.register_blueprint(home_blueprint)

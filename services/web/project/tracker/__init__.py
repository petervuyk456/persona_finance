def create_module(app, **kwargs):
    from .controllers import tracker_blueprint
    app.register_blueprint(tracker_blueprint)

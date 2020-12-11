from project import create_flask_app

app = create_flask_app()
app.app_context().push()

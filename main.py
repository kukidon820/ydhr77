from flask import Flask
from server.routes import routes
from data.models import Base
from data.create_engine import engine
from config import SECRET_KEY

app = Flask(__name__)

app.register_blueprint(routes)
app.secret_key = SECRET_KEY
Base.metadata.create_all(engine)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

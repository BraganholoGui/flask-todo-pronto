from flask import Flask
from routes.Web import web

app = Flask(__name__)
app.register_blueprint(web)

if __name__ == '__main__':
  app.run(host='0.0.0.0')
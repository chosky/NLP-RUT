from nplrut import app
from werkzeug.serving import WSGIRequestHandler

if __name__ == '__main__':
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(debug=True)
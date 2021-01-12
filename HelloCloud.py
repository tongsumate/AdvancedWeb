from flask import Flash
server = Flash(__name__)

@server.route("/")
def hello():
    return "Hello from Server"

if __name__ == "__main__":
    server.run(host='0.0.0.0',port=80)

from flask import Flask, request
import os
import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    # Output request headers "TAKEDA" to Log
    app.logger.info(request.headers.get("TAKEDA"))

    # Return current time
    dt_now = datetime.datetime.now()
    return dt_now.strftime('%Y-%m-%d %H:%M:%S') 


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8080)



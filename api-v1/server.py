from flask import Flask
import logging

app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.disabled = True
app.logger.disabled = True

@app.route('/api/v1/<num>')
def add_route(num):
    print("Api V1 request: ", num)
    return {
        'Api V1': num
    }

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

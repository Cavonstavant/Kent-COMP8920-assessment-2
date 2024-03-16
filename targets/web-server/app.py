from flask import Flask

app = Flask(__name__)

@app.route('/basic_passing', methods=['GET'])
def basic_passing():
    return 'This is a basic route that returns some text about nuclei and templates.'

@app.route('/basic_failing', methods=['GET'])
def basic_failing():
    return 'This is a random route.'

if __name__ == '__main__':
    app.run()
from flask import Flask

app= Flask(__name__)

@app.route('/')
def index():
    return  '''
    Don's Python Page
    Did you know? Python eats the world!
    Python Supports: Readable Code  Not Complicated
    Get started by: downloading Python Install Python
    '''

if __name__ == "__main__":
    app.run(debug=True)
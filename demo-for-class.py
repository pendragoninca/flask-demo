from flask import Flask

app= Flask(__name__)

@app.route('/')
def index():
    return  '''
    <!
        DOCTYPE html
    />
    <html lang="en">
    <!-- this is a comment-->
    <head>
        <title>
        </title>
    </head>
    <body>
        <h1>
            Don's Python Page
        </h1
    <p>
        Did you know? Python eats the world!
    </p>
    <p>
        Python Supports Readable Code is not complicated
    </p>
    <p>
        Get started by downloading Python Install Python
    </p>
    </body>
    '''

if __name__ == "__main__":
    app.run(debug=True)
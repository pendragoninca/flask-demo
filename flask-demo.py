from flask import Flask

app= Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html/>
    <html lang="en">
    <!-- this is a comment-->
    <head>
        <title>
            My Python Page
        </title>
        <style>
            h1 {
                color: blue;
                border-bottom: 1px solid black;
            }

            .red-text {
                color: red;
            }

            p {
                color: green;
            }
        </style>
    </head>
    <body>
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Python-logo.png/547px-Python-logo.png"
            alt="Python Logo"
            width="200" height="120" 
            />
        <h1>
            <em>
                Don's
            </em>
            Python Page
        </h1>
        <p>
            Did you know? 
            <em>
                <strong>
                    Python Eats the World Page!
                </strong>
            </em>
        </p>
        <br>
        <p class="red-text">
            Python supports:
        </p>
        <ul>
            <li>
                Readable
            </li>
             <li>
                Not Complicated
            </li>          
        </ul>
        <p>
            Get Started with Python by:
        </p>
        <ol>
            <li>
                Download Python
            </li>
            <li>
                Install Python
            </li>
        </ol>
        <br>
        <form action="" method="get" class="example">
            <label class="red-text">
                Enter your name:
            </label>
                <input type="text" name=name" id="name"
                required 
            />
            <input type="Submit" value="Submit"
            </>
        </form>
        <table>
            <tr>
               Today is Thursday 
            </tr>
            <tr>
                The Time is 6P
            </tr>
        </table>
    </body>
        '''
if __name__ == "__main__":
    app.run(debug=True)


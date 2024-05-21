from flask import Flask, render_template
from faker import Faker
from dotenv import load_dotenv

# load_dotenv()
faker = Faker()
names = [faker.unique.first_name() for _ in range(5)]
names.append("Betty")
names.sort()

# names = ["Betty","Bob","Robert","Karen","Sally"]

app= Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html",title="Jinja!",page_name="Sally's",names=names)

# if __name__ == "__main__":
#     app.run(debug=True)


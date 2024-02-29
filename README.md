# homegpt

I found it intriguing to develop a user-friendly front end for OpenAI's API to enhance customization. This project marks the initial stages of that project. 

The primary focus was on establishing a strong foundation, given my intent to integrate this tool into my daily routine. By following this guide, you can create a simple web interface for interacting with OpenAI's chatGPT. As a learner myself, I understand some of the challenges in finding guides, so I tailored this content with beginners in mind but also short and to the point.

Moving forward, my goal is to expand this project by adding features like a chat history and individual user accounts. This serves as the first installment of the project.

## How to Set Up the OpenAI API with Python and Flask

#### Create your project folder. 
```
mkdir homeGPT
cd homeGPT
```

#### Create your virtual environment
```
python3 -m venv homeGPT
```

#### Activate the virtual environment 
```
source homeGPT/bin/activate
```


#### Install [flask](https://pypi.org/project/Flask/), [requests](https://pypi.org/project/requests/), [python-dotenv](https://pypi.org/project/python-dotenv/)
```
pip install flask requests python-dotenv
```


#### Create file _app.py_. I use vim.
```
vim app.py
```

#### Add this code to _app.py_
```
from flask import Flask, render_template, request
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form['prompt']
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
                {"role": "user", "content": prompt}
            ]
        )
        return render_template('home.html', prompt=prompt, response=response.choices[0].message.content)
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
```


#### Create a templates folder
```
mkdir templates
```

#### Create a file _home.html_ within templates
```
vim home.html
```

#### Add this code to _home.html_
```
<!DOCTYPE html>
<html>
<head>
    <title>HomeGPT</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>HomeGPT</h1>
        <form method="POST">
            <div class="form-group">
                <input type="text" name="prompt" class="form-control" placeholder="Enter your prompt">
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>

        {% if response %}
            <div class="mt-3">
                <h2>The AI Says:</h2>
                <pre class="bg-light p-3">{{ response }}</pre>
            </div>
        {% endif %}
    </div>
</body>
</html>
```

#### Your file structure should look like this.
```
 project_folder/
 ├── app.py
 ├── templates/
 │   └── home.html
```

#### Grab your OpenAI API key [Link](https://openai.com/)

#### Set it as an environment variable
```
vim ~/.bashrc
```

#### Add this line at the end with your own api key.
```
export OPENAI_API_KEY="yourAPIkey"
```

#### This will let you use your new key.
```
source ~/.bashrc
```

#### Now let's test, you should see your api key.
```
echo $OPENAI_API_KEY
```

#### Startup the app
```
flask run
```

#### Assuming no errors, you should see this!

![homegpt](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qvhidrdv7lqro8idqlwp.png)

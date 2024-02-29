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

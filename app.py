from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/slideshow')
def slideshow():
    image_folder = 'static/images'
    images = [filename for filename in os.listdir(image_folder) if filename.endswith(('.jpg', '.png'))]
    return render_template('slideshow.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)

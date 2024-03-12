from flask import Flask, render_template

app = Flask(__name__)
#initialized flask

@app.route('/')
#decorator - tells the computer to run the program in internet browser of the computer

def load_html():
    print('html pages loaded')
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
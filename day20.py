from flask import Flask
app=Flask(__name__)


@app.route('/')
def some_function():
    return "Some message  from flask"

@app.route('/home')
def some_function2():
    return '''
    <html>
    <head><title> Home</title>
    </head>
    <body>
    <h3 style="color:red;">HOME PAGE</h3>
    <p> This is our new brand home page </p>
    </body>
    </html>
    '''







app.run(debug=True)
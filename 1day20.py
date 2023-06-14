from flask import Flask,render_template
app=Flask(__name__)


@app.route('/')
def some_function():
    return "Some message  from flask"

@app.route('/home/<name>')
def some_function2(name):
    print(name)
    return render_template(
        'home.html', name_value = name
        )   #fetch content from html file change to string and display it here
            #python code se data html page pe bhejna hai





app.run(debug=True)
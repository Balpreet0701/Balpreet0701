from flask import Flask

app=Flask(__name__)         #app is the object, flask name ka local web server bn jaega
                            # while running the value of name is __main__
                            #@ is the decorator in python to make ordinary function as extraordinary. Enhances the single function


@app.route('/')
def sample():
    return 'kuch bhi sample'

@app.route('/new')
def  new():
    return '<h1>  this is heading </h1>'


app.run(debug=True)               #debug use krke online server pe changes kr skte hai without closing server
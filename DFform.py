'''
Program to take input from html page
'''
from flask import Flask, render_template, request

app = Flask( __name__ )

@app.route('/')
def index( ):
    return render_template('Digital Fortress Webpage.html')

@app.route( '/', methods=['POST'] )
def getvalue( ):
    string = request.form['string']
    seed = request.form['seed']

    return render_template( 'pass.html', string=string, seed=seed)


if __name__ == '__main__':
    app.run( debug=True )
getvalue( )
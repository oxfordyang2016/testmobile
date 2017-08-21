from flask import Flask,redirect, url_for,request,make_response
from flask import  render_template
app = Flask(__name__)






@app.route('/')
def start():
    #return 'hello world, newzealand!!!!!'
    return render_template('index.html')



@app.route('/treatments')
def price():
    return render_template('treatments.html')



@app.route('/aboutus')
def abus():
    return render_template('aboutus.html')



@app.route('/coverage')
def coverage():
    return render_template('coverage.html')    


@app.route('/appointment')
def appointment():
    return render_template('appointment.html')


@app.route('/google9014931f0be3f413.html')
def goolecheck():
    return render_template('google9014931f0be3f413.html')





@app.route('/generic')
def generic():
    return render_template('generic.html')

@app.route('/element')
def ele():
    return render_template('elements.html')


@app.route('/test')
def test():
    return 'designed by jack yang,please communicate with yang756260386@gmail.com 233 '



if __name__ == '__main__':
    app.run('0.0.0.0',50,debug='True')

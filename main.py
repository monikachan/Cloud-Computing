from flask import Flask, render_template,redirect, request
app = Flask(__name__)


@app.route('/')
def hello_world():

  return render_template("main.html",abc=abc)

@app.route('/is_prime', methods=['GET','POST'])
def is_prime():
    import array as arr
    number = request.form.get('Num')
  #  n = int(number)
    try:
        n = int(number)
    except TypeError:
        n = 0
    arr = []
    if n == 0:
        return 'Invalid'
    if n == 2:
        return 'Even-Prime'

    if n >= 3:
        for i in range(3,n):
            if  n % i == 0:
                arr.append('False')

    size = len(arr)
    if size != 0:
        return 'False'
    else:
        return 'True'

@app.route('/is',methods=['GET','POST'])
def abc():
        return 'hii'
if __name__ == '__main__':
  app.run()

from flask import *
import playfairCipher
app = Flask(__name__)
output = ''

@app.route('/',methods=['GET','POST'])
def indexPage():
    if (request.method == 'GET'):
        return render_template('index.html',op='')
    
    elif (request.method == 'POST'):
        output = ''
        if (request.form.get('action',None) == 'Encrypt'):
            output = playfairCipher.encrypt(request.form['plaintext'],request.form['cipher'])
        elif (request.form.get('action',None) == 'Decrypt'):
            output = playfairCipher.decrypt(request.form['plaintext'],request.form['cipher'])
        elif (request.form.get('action',None) == 'Clear'):
            return render_template('index.html',op = '')
        return render_template('index.html',op = output)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
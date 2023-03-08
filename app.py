from flask import Flask,render_template,flash,session,request,redirect,url_for
import wikiscraper

app = Flask(__name__)

app.config['SECRET_KEY']='blah'

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == "POST":
            data = request.form['search']
            print(data)

            
            info = wikiscraper.get_info(data)
            print(info)
            if(info == 1):
                return render_template('index.html',error=1)
            else:
                return render_template('index.html',info=info)

    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)
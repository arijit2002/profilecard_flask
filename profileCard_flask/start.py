import cx_Oracle as c
from flask import Flask,render_template, request,make_response
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form',methods=['POST'])
def form():
    return render_template('form.html')

@app.route('/store',methods=['POST'])
def store():
    if request.method=='POST':
        con=c.connect('c##scott/tiger@localhost/orcl')
        print(con.version)
        cur=con.cursor()
        msg=''
        try:
            name=request.form.get('name')
            contact=request.form.get('contact')
            email=request.form.get('email')
            cur.execute("insert into profileCard values(:x,:y,:z)",{"x":name,"y":contact,"z":email})
            con.commit()
            msg='Message Successfully delivered'
            print(msg,con)
        except Exception as e:
            print(e)
            con.rollback()
            msg='error in insert'
    return '<h1>Message Delivered</h1>'

if __name__=='__main__':
    app.run()


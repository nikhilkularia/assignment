from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class products(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    product_name1 = db.Column(db.String(50))
    price1 = db.Column(db.Integer)
    product_name2 = db.Column(db.String(50))
    price2 = db.Column(db.Integer)
    product_name3 = db.Column(db.String(50))
    price3 = db.Column(db.Integer)
    product_name4 = db.Column(db.String(50))
    price4 = db.Column(db.Integer)
    def __repr__(self):
        return f"products('{self.product_name1}',{self.price1},{self.product_name2}',{self.price2},{self.product_name3}',{self.price3},{self.product_name4}',{self.price4})"



class products2(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    product_name5 = db.Column(db.String(50))
    price5 = db.Column(db.Integer)
    product_name6 = db.Column(db.String(50))
    price6 = db.Column(db.Integer)
    product_name7 = db.Column(db.String(50))
    price7 = db.Column(db.Integer)
    product_name8 = db.Column(db.String(50))
    price8 = db.Column(db.Integer)
    def __repr__(self):
        return f"products2('{self.product_name5}',{self.price5},{self.product_name6}',{self.price6},{self.product_name7}',{self.price7},{self.product_name8}',{self.price8})"


@app.route('/',methods=['GET','POST'])
def home():
    obj=products.query.first()
    obj1=products2.query.first()

    context = {'product_name1':obj.product_name1,'price1':obj.price1,
               'product_name2': obj.product_name2, 'price2': obj.price2,
               'product_name3': obj.product_name3, 'price3': obj.price3,
               'product_name4': obj.product_name4, 'price4': obj.price4,

               'product_name5': obj1.product_name5, 'price5': obj1.price5,
               'product_name6': obj1.product_name6, 'price6': obj1.price6,
               'product_name7': obj1.product_name7, 'price7': obj1.price7,
               'product_name8': obj1.product_name8, 'price8': obj1.price8,
               }
    return render_template('home.html', context=context)


@app.route('/mail',methods=['GET','POST'])
def mail():
    return render_template('mail.html')

if __name__ == '__main__':
    app.run()


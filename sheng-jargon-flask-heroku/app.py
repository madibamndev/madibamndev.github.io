import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'sheng_jargon'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://mwemn:qRTbx%jHn%213KUhJ0FfRqLgItES%0AgH923D%Kls@myfirstcluster.cnxjr.mongodb.net/sheng_jargon?retryWrites=true&w=majority')
mongo = PyMongo(app)


@app.route('/')
@app.route('/quick_jargon_search/')
def quick_jargon_search():
    jargon = mongo.db.jargon.find()
    return render_template("quickjargonsearch.html",
        jargon=jargon)


@app.route('/advanced_jargon_search/')
def advanced_jargon_search():
    jargon = mongo.db.jargon.find()
    return render_template("advancedjargonsearch.html",
        jargon=jargon)


@app.route('/browse_jargon_by_alphabet/')
def browse_jargon_by_alphabet():
    jargon = mongo.db.jargon.find()
    return render_template("browsejargonbyalphabet.html",
        jargon=jargon)


@app.route('/browse_jargon/')
def browse_jargon():
    jargon = mongo.db.jargon.find()
    return render_template("browsejargon.html",
        jargon=jargon)


@app.route('/add_jargon')
def add_jargon():
    jargon = mongo.db.jargon.find()
    return render_template('addjargon.html',
        jargon=jargon)


@app.route('/delete_jargon/<jargon_id>')
def delete_jargon(jargon_id):
    mongo.db.jargon.remove({'_id': ObjectId(jargon_id)})
    return redirect(url_for('browse_jargon'))


@app.route('/edit_jargon/<jargon_id>')
def edit_jargon(jargon_id):
    the_jargon=mongo.db.jargon.find_one({"_id": ObjectId(jargon_id)})
    all_categories=mongo.db.categories.find()
    all_part_of_speech=mongo.db.part_of_speech.find()
    return render_template('editjargon.html', jargon=the_jargon,
                           categories=all_categories, part_of_speech=all_part_of_speech)


@app.route('/insert_jargon', methods=['POST'])
def insert_jargon():
    jargon =  mongo.db.jargon
    jargon.insert_one(request.form.to_dict())
    return redirect(url_for('browse_jargon'))


@app.route('/update_jargon/<jargon_id>', methods=["POST"])
def update_jargon(jargon_id):
    jargon = mongo.db.jargon
    jargon.update( {'_id': ObjectId(jargon_id)},
    {
        'category_name':request.form.get('category_name'),
        'word': request.form.get('word'),
        'definition': request.form.get('definition'),
        'meaning': request.form.get('meaning'),
        'synonyms': request.form.get('synonyms'),
        'antonyms_or_opposite': request.form.get('antonyms_or_opposite'),
        'part_of_speech': request.form.get('part_of_speech'),
        'alphabets': request.form.get('alphabets'),
        'date_added': request.form.get('date_added')
    })
    return redirect(url_for('browse_jargon'))


@app.route('/categories/', endpoint='categories')
def categories():
    categories = mongo.db.categories.find()
    return render_template("categories.html",
        categories=categories)


@app.route('/add_category')
def add_category():
    return render_template('addcategory.html')


@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('categories'))


@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
    category=mongo.db.categories.find_one({'_id': ObjectId(category_id)}))


@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.categories.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form.get('category_name')})
    return redirect(url_for('categories'))


@app.route('/insert_category', methods=['POST'])
def insert_category():
    category_doc = {'category_name': request.form.get('category_name')}
    mongo.db.categories.insert_one(category_doc)
    return redirect(url_for('categories'))


@app.route('/contact/')
def contact():
    messages = mongo.db.messages.find()
    return render_template('contact.html',
        messages=messages)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', '8080')),
            debug=True)
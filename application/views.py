from application import app, db
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    try:
        col = db['data']
        documents = col.find()
        docs = []
        count = 1
        for doc in documents:
            doc['序号'] = count
            count += 1
            docs.append(doc)
    except Exception as e:
        err_msg = '数据库操作失败：' + str(e)
        return render_template('error.html', message=err_msg)

    return render_template('main.html', docs=docs)
from flask import Flask, request, jsonify, render_template, redirect, url_for
import pandas as pd

import zh_core_web_sm
from markupsafe import Markup
import json

app = Flask(__name__)

# 省略了ent_name、ent_box、DEFAULT_LABEL_COLORS和entity函数的定义



def ent_name(name):
    return f'<span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem;">{name}</span>'

def ent_box(children, color):
    return f'<mark style="background: {color}; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;">{children}</mark>'

def entity(children, name):
    if type(children) is str:
        children = [children]

    children.append(ent_name(name))
    color = DEFAULT_LABEL_COLORS[name]
    return ent_box(''.join(children), color)


def render(doc):
    children = []
    last_idx = 0
    for ent in doc.ents:
        children.append(doc.text[last_idx:ent.start_char])
        children.append(entity(doc.text[ent.start_char:ent.end_char], ent.label_))
        last_idx = ent.end_char
    children.append(doc.text[last_idx:])
    return Markup(''.join(children))



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        filename = file.filename
        if filename.endswith('.csv'):
            df = pd.read_csv(file)
        elif filename.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(file)
        else:
            return jsonify({'error': 'Unsupported file format'}), 400

        df['text'] = df['text'].astype(str)

        data = df.to_dict(orient='records')

        nlp = zh_core_web_sm.load()
        result_data = []
        for row in data:
            doc = nlp(row['text'])
            entities = [{'text': ent.text, 'label': ent.label_} for ent in doc.ents]
            result_data.append({
                'section': row['section'],
                'text': row['text'],
                'date': row['date'],
                'entity': entities
            })

        return redirect(url_for('show_table', data=json.dumps(result_data)))
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500

@app.route('/show_table')
def show_table():
    data_str = request.args.get('data')

    if data_str is None:
        return render_template('error.html', message='No data available')

    data = json.loads(data_str)

    return render_template('show_table.html', data=data)
@app.route('/', methods=['POST'])
def analyze():
    text = request.form['textarea']
    nlp = zh_core_web_sm.load()
    ruler=nlp.add_pipe("entity_ruler")
  


    doc = nlp(text)
    
    output = render(doc)
    return output
if __name__ == '__main__':
    app.run(host='0.0.0.0')

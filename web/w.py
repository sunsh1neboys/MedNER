from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import *
from model import *
from config import *

app = Flask(__name__)
CORS(app)  # 允许跨域请求

@app.route('/recognize', methods=['POST'])
def recognize():
    data = request.json
    text = data.get('text', '')
    
    if text:
        _, word2id = get_vocab()
        # tokenizer = BertTokenizer.from_pretrained(BERT_MODEL)
        _, word2id = get_vocab()
        input = torch.tensor([[word2id.get(w, WORD_UNK_ID) for w in text]])
        mask = torch.tensor([[1] * len(text)]).bool()

        model = torch.load(MODEL_DIR + 'model_0.pth', map_location=DEVICE)
        y_pred = model(input, mask)
        id2label, _ = get_label()

        label = [id2label[l] for l in y_pred[0]]
        info = extract(label, text)

        return jsonify({'info': info})
    else:
        return jsonify({'error': 'No text provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)

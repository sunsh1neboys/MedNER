ORIGIN_DIR = '/Users/qiu/Desktop/2.28/ruijinyiyuan/input/origin/'
ANNOTATION_DIR = '/Users/qiu/Desktop/2.28/ruijinyiyuan/output/annotation/'

TRAIN_SAMPLE_PATH = '/Users/qiu/Desktop/2.28/ruijinyiyuan/output/train_sample.txt'
TEST_SAMPLE_PATH = '/Users/qiu/Desktop/2.28/ruijinyiyuan/output/test_sample.txt'

VOCAB_PATH = '/Users/qiu/Desktop/2.28/ruijinyiyuan/output/vocab.txt'
LABEL_PATH = '/Users/qiu/Desktop/2.28/ruijinyiyuan/output/label.txt'

WORD_PAD = '<PAD>'
WORD_UNK = '<UNK>'

WORD_PAD_ID = 0
WORD_UNK_ID = 1
LABEL_O_ID = 0

VOCAB_SIZE = 3000
EMBEDDING_DIM = 100
HIDDEN_SIZE = 256
TARGET_SIZE = 31
LR = 1e-3
EPOCH = 100

MODEL_DIR = '/Users/qiu/Desktop/2.28/ruijinyiyuan/output/model/'

import torch

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'


BERT_MODEL = '/Users/qiu/Desktop/2.28/ruijinyiyuan/huggingface/bert-base-chinese'
EMBEDDING_DIM = 768
MAX_POSITION_EMBEDDINGS = 512
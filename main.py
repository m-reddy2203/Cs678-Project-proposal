pip install nltk==3.5
pip install numpy==1.19.5,
pip install sklearn==0.0
pip install torch==1.7.1+cu110
pip install transformers==3.0.2
pip install OpenHowNet==0.0.1a11"
pip install nltk
import nltk
nltk.download('punkt')
from OpenHowNet import download
download()
python english_word_sememe.py
python chinese_token_sememe.py
python english_train_test.py 
python modern_chinese_train_test.py
python ancient_chinese_train_test.py

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
import string

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('omw-1.4')

input_text = (
    "The quick brown fox jumps over the lazy dog. I found this interesting text in Internet, because it "
    "contains all the letters of the English alphabet. I liked that, so I use that. "
    "What do you think?"
)

input_file = "original_text.txt"
output_file = "processed_text.txt"

with open(input_file, "w", encoding="utf-8") as file:
    file.write(input_text)

with open(input_file, "r", encoding="utf-8") as file:
    text = file.read()

tokens = word_tokenize(text)

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
stemmed_tokens = [stemmer.stem(token) for token in tokens]

stop_words = set(stopwords.words("english"))
tokens_no_stopwords = [token for token in tokens if token.lower() not in stop_words]

translator = str.maketrans('', '', string.punctuation)
tokens_no_punctuation = [token.translate(translator) for token in tokens_no_stopwords]
tokens_no_punctuation = [token for token in tokens_no_punctuation if token]

processed_text = " ".join(tokens_no_punctuation)
with open(output_file, "w", encoding="utf-8") as file:
    file.write(processed_text)

print("Токенізація по словам:", tokens)
print("Лемматизація:", lemmatized_tokens)
print("Стеммінг:", stemmed_tokens)
print("Оброблений текст без стоп-слів та пунктуації записано у файл.")

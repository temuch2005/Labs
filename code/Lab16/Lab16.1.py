import nltk
from nltk.corpus import gutenberg
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt

nltk.download('gutenberg')
nltk.download('stopwords')
nltk.download('punkt')

text = gutenberg.raw('bryant-stories.txt')

words = nltk.word_tokenize(text)
word_count = len(words)
print(f"Кількість слів у тексті: {word_count}")

word_freq = Counter(words)
most_common_words = word_freq.most_common(10)

def plot_most_common_words(common_words, title):
    words, counts = zip(*common_words)
    plt.figure(figsize=(10, 5))
    plt.bar(words, counts, color='skyblue')
    plt.title(title)
    plt.xlabel('Слова')
    plt.ylabel('Кількість вживань')
    plt.show()

print("10 найбільш вживаних слів у тексті (з пунктуацією і стоп-словами):")
print(most_common_words)
plot_most_common_words(most_common_words, "10 найбільш вживаних слів у тексті")

stop_words = set(stopwords.words('english'))
words_no_punct = [word.lower() for word in words if word.isalpha()]
filtered_words = [word for word in words_no_punct if word not in stop_words]

filtered_word_freq = Counter(filtered_words)
filtered_most_common_words = filtered_word_freq.most_common(10)

print("10 найбільш вживаних слів після видалення пунктуації і стоп-слів:")
print(filtered_most_common_words)
plot_most_common_words(filtered_most_common_words, "10 найбільш вживаних слів після фільтрації")

import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('stopwords')
stopwords_ru = set(stopwords.words('russian'))

# Change to website_text_alt.txt for second web-page
with open("website_text.txt", encoding='utf-8') as f:
    words = re.findall(r'\b\S+\b', f.read())

    temp = set(words) - stopwords_ru
    text_words = []
    for word in temp:
        text_words.append(word.lower())

with open("keywords/news.txt", encoding='utf-8') as f:
    news_keywords = set()
    news_keywords.update(f.read().split())

with open("keywords/science.txt", encoding='utf-8') as f1:
    science_keywords = set()
    science_keywords.update(f1.read().split())

with open("keywords/shopping.txt", encoding='utf-8') as f2:
    shopping_keywords = set()
    shopping_keywords.update(f2.read().split())

with open("keywords/sport.txt", encoding='utf-8') as f3:
    sport_keywords = set()
    sport_keywords.update(f3.read().split())


def jaccard_index(text: list, keywords: set):
    text_keywords = set(text)
    intersection = len(text_keywords.intersection(keywords))
    union = len(text_keywords.union(keywords))
    return intersection / union

def cosine_similarity_impl(text: str, keywords: str):
    count_vectorizer = CountVectorizer()
    sparse_matrix = count_vectorizer.fit_transform([text, keywords])
    return cosine_similarity(sparse_matrix, sparse_matrix)


if __name__ == '__main__':
    text_news_jaccard = jaccard_index(text_words, news_keywords)
    text_science_jaccard = jaccard_index(text_words, science_keywords)
    text_shopping_jaccard = jaccard_index(text_words, shopping_keywords)
    text_sport_jaccard = jaccard_index(text_words, sport_keywords)

    print("JACCARD COEFFICIENT:")
    print(f"news: {text_news_jaccard}")
    print(f"science: {text_science_jaccard}")
    print(f"shopping: {text_shopping_jaccard}")
    print(f"sport: {text_sport_jaccard} \n")

    text_words_string = " ".join(list(text_words))
    news_keywords_string = " ".join(list(news_keywords))
    science_keywords_string = " ".join(list(science_keywords))
    shopping_keywords_string = " ".join(list(shopping_keywords))
    sport_keywords_string = " ".join(list(sport_keywords))

    text_news_cosine = cosine_similarity_impl(text_words_string, news_keywords_string)[0][1]
    text_science_cosine = cosine_similarity_impl(text_words_string, science_keywords_string)[0][1]
    text_shopping_cosine = cosine_similarity_impl(text_words_string, shopping_keywords_string)[0][1]
    text_sport_cosine = cosine_similarity_impl(text_words_string, sport_keywords_string)[0][1]

    print("COSINE SIMILARITY:")
    print(f"news: {text_news_cosine}")
    print(f"science: {text_science_cosine}")
    print(f"shopping: {text_shopping_cosine}")
    print(f"sport: {text_sport_cosine}")

import streamlit as st
import speech_recognition as sr
import nltk
nltk.download("vader_lexicon")
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize


sentiment_analyzer = SentimentIntensityAnalyzer()

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    return recognizer.recognize_google(audio)

def analyze_sentiment(text):
    sentiment = sentiment_analyzer.polarity_scores(text)
    return sentiment



def suggest_improvements(sentiment):
    if sentiment["compound"] > 0.05:
        return "The text has a positive tone. Keep it up!"
    elif sentiment["compound"] < -0.05:
        return "The text has a negative tone. Try to use more positive words and phrases."
    else:
        return "The text has a neutral tone. Try to add some emotions to make it more interesting."

def main():
    st.title("Awesome app")
    st.subheader("Upload your audio file below:")
    audio_file = st.file_uploader("", type=["wav", "mp3", "aac"])
    if audio_file:
        text = transcribe_audio(audio_file)
        st.write("Transcription!!:" + text)
        sentiment = analyze_sentiment(text)
        improvement_suggestion = suggest_improvements(sentiment)
        st.success(improvement_suggestion)

if __name__ == '__main__':
    main()

def passive(text):
    passive_words = ["am", "is", "been", "was", "are", "be", "being"]
    non_passive_words = ['do', 'did', 'does', 'have', 'has', 'had']
    passive_score = 0
    tokens = word_tokenize(text)
    for token in tokens: 
        if token in passive_words: 
            passive_score += 1
        elif token in non_passive_words: 
            passive_score -= 1

    return passive_score

def suggestions(text):
    suggestions = []

    if passive(text) > 10: 
        suggestions.append("Your tone is too passive. Use more active words. Examples of active words are do, did, does")


def get_formality_score(text):
    formal_words = ["please", "kindly", "thank you", "sincerely", "yours truly"]
    informal_words = ["gonna", "wanna", "ain't", "don't", "can't"]

    formality_score = 0
    tokens = word_tokenize(text)
    for token in tokens:
        if token in formal_words:
            formality_score += 1
        elif token in informal_words:
            formality_score -= 1
    
    return formality_score

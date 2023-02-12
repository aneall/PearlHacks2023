import streamlit as st
import streamlit.components.v1 as atest
import speech_recognition as sr
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

 
sentiment_analyzer = SentimentIntensityAnalyzer()


def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    return recognizer.recognize_google(audio)


def sentiment_scores(text):
 
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()
 
    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(text)
     
    print("Here is your tone distribution! : ", sentiment_dict)
    print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")
 
    print("Sentence Overall Rated As", end = " ")
 
    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05 :
        print("This recording has a positive connotation!")
 
    elif sentiment_dict['compound'] <= - 0.05 :
        print("This recording has a negative connotation!")
 
    else :
        print("This recording has a neutral tone!")


def passive(text):
    passive_words = ["am", "is", "been", "was", "are", "be", "being"]
    non_passive_words = ['do', 'did', 'does', 'have', 'has', 'had']
    passive_counter = 0 
    non_passive_counter = 0 
    broken = text.split()
    for i in broken:
        if i in passive_words: 
            passive_counter += 1
        elif i in non_passive_words: 
            non_passive_counter += 1 
    if non_passive_counter!= 0:
        passive_ratio = passive_counter/non_passive_counter
    return passive_ratio

def confidence(text):
    not_confident = ["like", "umm", "um", "but", "uh", "you know", "i mean", "so", "just", "basically", "i guess"]
    weakling_counter = 5
    broken = text.split()
    for i in broken: 
        if i in not_confident:
            weakling_counter -= 1
    return weakling_counter

def get_formality_score(text):
    formal_words = ["please", "kindly", "thank you", "sincerely", "yours truly"]
    informal_words = ["gonna", "wanna", "ain't", "don't", "can't"]
    formal_counter = 0
    informal_counter = 0
    formality_ratio = 0

    broken = text.split()
    for i in broken:
        if i in formal_words:
            formal_counter += 1
        elif i in informal_words:
            informal_counter -= 1
    if informal_counter!= 0: 
        formality_ratio = formal_counter/informal_counter
    return formality_ratio


def suggestions(text):

    if passive(text) > 1: 
        print("Your tone is too passive. Use more active words. Examples of active words are do, did, does.")
    
    if passive(text) < 1: 
        print("Your recording uses active verbs and non-passive words for the most part! Good job!")
    
    if confidence(text) <= 0: 
        print("The tone could be more confident. Avoid using filler words and take pauses instead of rambling on with 'ums' and 'buts'. You got this! :) ")

    if confidence(text) > 0: 
        print("Your tone has the right amount of confidence! Keep it up!")
    
    if get_formality_score(text) > 1:
        print("The overall tone of your recording is formal!")
    
    if get_formality_score(text) < 1: 
        print("The overall tone of your recording is informal.")
    
    if get_formality_score(text) == 0: 
        print("The overall tone of your recording in terms of formality is neutral!")
    

def main():
    st.title("Awesome app")
    st.subheader("Upload your audio file below:")
    audio_file = st.file_uploader("", type=["wav", "mp3", "aac"])
    if audio_file:
        text = transcribe_audio(audio_file)
        st.write("Your file has run successfully!")
        overall = print(sentiment_scores(text))
        more_suggestions = print(suggestions(text))
        st.write(overall)
        st.write(more_suggestions)

if __name__ == '__main__':
    main()


atest.html(
    import streamlit as st
import streamlit.components.v1 as atest
import speech_recognition as sr
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


sentiment_analyzer = SentimentIntensityAnalyzer()


def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    return recognizer.recognize_google(audio)


def sentiment_scores(text):
 
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()
 
    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(text)
     
    print("Here is your tone distribution! : ", sentiment_dict)
    print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")
 
    print("Sentence Overall Rated As", end = " ")
 
    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05 :
        print("This recording has a positive connotation!")
 
    elif sentiment_dict['compound'] <= - 0.05 :
        print("This recording has a negative connotation!")
 
    else :
        print("This recording has a neutral tone!")


def passive(text):
    passive_words = ["am", "is", "been", "was", "are", "be", "being"]
    non_passive_words = ['do', 'did', 'does', 'have', 'has', 'had']
    passive_counter = 0 
    non_passive_counter = 0 
    broken = text.split()
    for i in broken:
        if i in passive_words: 
            passive_counter += 1
        elif i in non_passive_words: 
            non_passive_counter += 1 
    if non_passive_counter!= 0:
        passive_ratio = passive_counter/non_passive_counter
    return passive_ratio

def confidence(text):
    not_confident = ["like", "umm", "um", "but", "uh", "you know", "i mean", "so", "just", "basically", "i guess"]
    weakling_counter = 5
    broken = text.split()
    for i in broken: 
        if i in not_confident:
            weakling_counter -= 1
    return weakling_counter

def get_formality_score(text):
    formal_words = ["please", "kindly", "thank you", "sincerely", "yours truly"]
    informal_words = ["gonna", "wanna", "ain't", "don't", "can't"]
    formal_counter = 0
    informal_counter = 0
    formality_ratio = 0

    broken = text.split()
    for i in broken:
        if i in formal_words:
            formal_counter += 1
        elif i in informal_words:
            informal_counter -= 1
    if informal_counter!= 0: 
        formality_ratio = formal_counter/informal_counter
    return formality_ratio


def suggestions(text):

    if passive(text) > 1: 
        print("Your tone is too passive. Use more active words. Examples of active words are do, did, does.")
    
    if passive(text) < 1: 
        print("Your recording uses active verbs and non-passive words for the most part! Good job!")
    
    if confidence(text) <= 0: 
        print("The tone could be more confident. Avoid using filler words and take pauses instead of rambling on with 'ums' and 'buts'. You got this! :) ")

    if confidence(text) > 0: 
        print("Your tone has the right amount of confidence! Keep it up!")
    
    if get_formality_score(text) > 1:
        print("The overall tone of your recording is formal!")
    
    if get_formality_score(text) < 1: 
        print("The overall tone of your recording is informal.")
    
    if get_formality_score(text) == 0: 
        print("The overall tone of your recording in terms of formality is neutral!")
    

def main():
    st.title("Awesome app")
    st.subheader("Upload your audio file below:")
    audio_file = st.file_uploader("", type=["wav", "mp3", "aac"])
    if audio_file:
        text = transcribe_audio(audio_file)
        st.write("Your file has run successfully!")
        overall = print(sentiment_scores(text))
        more_suggestions = print(suggestions(text))
        st.write(overall)
        st.write(more_suggestions)

if __name__ == '__main__':
    main()


atest.html 
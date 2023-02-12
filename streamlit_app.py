import streamlit as st
import streamlit.components.v1 as embeddedrenderer
import speech_recognition as sr
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import requests
import time

st.markdown("""
    <style>
    body {
        background-color: #D0B3A1;
        font-family: "Courier New", Courier, monospace;
    }
    </style>
    """, unsafe_allow_html=True)
    
sentiment_analyzer = SentimentIntensityAnalyzer()


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

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
    st.write('**We analyzed your pitch-- here are a couple of pointers on things you did well and things that could use improvement:**')
    st.write("🎓 The tone of your pitch was ", sentiment_dict['neg']*100, "% Negative")
    st.write("🎓 The tone of your pitch was ", sentiment_dict['neu']*100, "% Neutral")
    st.write("🎓 The tone of your pitch was ", sentiment_dict['pos']*100, "% Positive")
 
    st.write('**_The tone of your pitch was overall..._**', end = " ")
 
    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05 :
        st.write("Positive!")
 
    elif sentiment_dict['compound'] <= - 0.05 :
        st.write("Negative. :(")
 
    else :
       st.write("Neutral!")


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
        st.write("✔️ Your tone is :violet[**too passive**]. Using passive words makes the overall tone of your pitch less engaging-- to make that awesome idea ✨shine✨ from within, **use active words** like 'do', 'does' and 'have'. ")
    
    if passive(text) < 1: 
        st.write("✔️ Your recording uses :orange[non-passive words] for the most part! Good job!")
    
    if confidence(text) <= 0: 
        st.write("✔️ :violet[**Your tone could be more confident.**] Avoid using filler words and take pauses instead of rambling on with the 'ums' and 'buts'. Remember that you are awesome and you got this! 🙌 ")

    if confidence(text) > 0: 
        st.write("✔️ Wow, you sound :orange[confident]! Keep it up! 😎")
    
    if get_formality_score(text) > 1:
        st.write("✔️ The overall tone of your recording is :red[**formal**].")
    
    if get_formality_score(text) < 1: 
        st.write("✔️ The overall tone of your recording is :red[**informal**].")
    
    if get_formality_score(text) == 0: 
        st.write("✔️ The overall tone of your recording in terms of formality is :red[**neutral!**]")
    


def create_iphone_model(model_type):
    if model_type == "iPhone X":
        iphone_mesh = trimesh.creation.box(extents=[0.07, 0.15, 0.02], centroid=[0,0,0])
        return iphone_mesh
    else:
        print("Invalid model type. Only 'iPhone X' is supported in this example.")
        return None

def add_css():
    st.markdown(
        f"""
        <style>
        {open("custom.css").read()}
        </style>
        """,
        unsafe_allow_html=True,
    )

   

    
def main():


    st.title("👩‍🎤 " + " Welcome to Pitch Perfect! " + "👩‍🔬")
    st.subheader('Meet your :violet[personal pitch assistant] that will help you climb the corporate ladder of success!')
    
    lottie_url = "https://assets6.lottiefiles.com/packages/lf20_yCjSOH1fA9.json"
    lottie_json = load_lottieurl(lottie_url)
    st_lottie(lottie_json)

    if st.button("Download"):
        with st_lottie_spinner(lottie_json):
            time.sleep(5)
        st.balloons()
    
    st.subheader(':violet[Upload your audio file below:]')
    audio_file = st.file_uploader("", type=["wav", "mp3", "aac"])
    if audio_file:
        text = transcribe_audio(audio_file)
        st.write("Your file has run successfully!")
        overall = sentiment_scores(text)
        more_suggestions = suggestions(text)
        st.write(more_suggestions)
        
 
        embeddedrenderer.html(
        """
        <html>
          <head>

          </head>
        <body>
          <embed src="https://pearlhackstest.glitch.me/pink.html"
            width="800px"
            height="800px"
            visibility="hidden"
            allowfullscreen
            sandbox>
            
            <embed src="https://pearlhackstest.glitch.me/purple.html"
            width="800px"
            height="800px"
            allowfullscreen
            sandbox>
            
            <embed src="https://pearlhackstest.glitch.me/green.html"
            width="800px"
            height="800px"
            allowfullscreen
            sandbox>
            
          </body>
        </html>
        """,
    height=900, width=920, scrolling=True)
    


if __name__ == '__main__':
    main()

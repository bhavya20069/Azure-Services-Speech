from gtts import gTTS
from IPython.display import Audio, display

# Text to convert into speech
text = "Hello! Welcome to Python text to speech. Your program is working successfully."

try:
    # Convert text into speech
    tts = gTTS(text=text, lang="en")

    # Save audio file
    tts.save("output.mp3")

    print("Speech synthesized successfully!")
    print("Audio saved as output.mp3")

    # Play audio in Google Colab
    display(Audio("output.mp3"))

except Exception as e:
    print("Error:", e)

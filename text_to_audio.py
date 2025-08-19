import nltk
from gtts import gTTS
import os
from newspaper import Article  # This import is necessary

# Get the article
article = Article('https://www.hostinger.com/in/tutorials/how-to-make-a-web-app-with-hostinger-horizons')
article.download()
article.parse()

# Download the punkt package for nltk
nltk.download('punkt')

# Natural Language Processing
article.nlp()

# Get the text of the article
mytext = article.text

# Convert the text to audio
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)

# Save the audio file
myobj.save("article.mp3")

# Play the audio file
os.system("start article.mp3")  # Use "start" on Windows, "afplay" on macOS, or "xdg-open" on Linux

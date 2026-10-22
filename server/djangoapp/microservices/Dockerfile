FROM python:3.9.18-slim-bookworm


WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Put the VADER word list where NLTK looks for it
COPY sentiment /usr/local/share/nltk_data/sentiment
# Fail the build now if NLTK can't load the analyzer
RUN python3 -c "from nltk.sentiment import SentimentIntensityAnalyzer; SentimentIntensityAnalyzer(); print('VADER OK')"

COPY . .
RUN ls
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

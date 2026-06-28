"""
This module deploys a Flask web application that exposes an endpoint
for emotion detection using Watson NLP.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_analyzer():
    """
    Retrieves the text to analyze from the request, passes it to the
    emotion detector, and returns the formatted result.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    # Analyze the text using the emotion detector
    response = emotion_detector(text_to_analyze)

    # Handle invalid or blank input
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    # Format and return the system response string
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is "
        f"{response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the index page of the application.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

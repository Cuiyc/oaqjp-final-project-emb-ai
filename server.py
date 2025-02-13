"""
A flask web server that makes emotion detection
"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """
    Defualt '/' path to show input page.
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detect():
    """
    Call emotion_detector in EmotionDetection module to detect emotion.
    The parameter is a text string and the result is a dict have below attributes.

    Example of good respone: 
        {
        "anger": 0.006274985, 
        "disgust": 0.0025598293, 
        "fear": 0.009251528, 
        "joy": 0.9680386, 
        "sadness": 0.049744144, 
        "dominant_emotion":"joy"
        }
    
    If the input text is invalid, same structure dict will return but all the values are None.
        {
        "anger": None, 
        "disgust": None, 
        "fear": None, 
        "joy": None, 
        "sadness": None, 
        "dominant_emotion": None
        }
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if None is response['dominant_emotion']:
        return 'Invalid text! Please try again!'

    result = f"For the given statement, the system response is 'anger': {response['anger']}, "
    result += f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
    result += f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
    result += f"The dominant emotion is <b>{response['dominant_emotion']}</b>."
    return result

if __name__ == '__main__':
    app.run()

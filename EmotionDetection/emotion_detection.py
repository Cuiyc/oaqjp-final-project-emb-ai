import requests
import json

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

BAD_RESPONSE = {
"anger": None, "disgust": None,  "fear": None, "joy": None, "sadness": None, "dominant_emotion": None }

def emotion_detector(text_to_analyze):
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json = input_json, headers=HEADERS)
    if response.status_code == 400: 
        return BAD_RESPONSE
    else:
        resp_json = json.loads(response.text)
        emotion_scores = resp_json['emotionPredictions'][0]['emotion']
        dominant_emotion = ''
        dominant_score = 0
        for index, (key, value) in enumerate(emotion_scores.items()):
            if value > dominant_score:
                dominant_emotion = key
                dominant_score = value
        emotion_scores['dominant_emotion'] = dominant_emotion
        return emotion_scores


if __name__ == '__main__':
    print(emotion_detector("I love this new technology."))
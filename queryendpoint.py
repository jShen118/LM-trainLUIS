import urllib
import webbrowser
import json

def query(utterance):
    queryLink = 'https://hydluissbx01.cognitiveservices.azure.com/luis/prediction/v3.0/apps/bc12f380-fc99-4ecc-8b0e-4dd6cde01400/slots/production/predict?subscription-key=3106ba28b86b42ce9ca45c3d00987f21&verbose=true&show-all-intents=true&log=true&query='
    return webbrowser.open(queryLink + urllib.parse.quote(utterance))

file = open("bt3.json", "r") 
training_list = json.load(file) 
utterance_output_list = []  
for full_utterance_dict in training_list:     
    utterance_text = full_utterance_dict["text"]     
    utterance_output_list.append(utterance_text)




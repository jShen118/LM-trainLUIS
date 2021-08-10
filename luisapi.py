#https://docs.microsoft.com/en-us/azure/cognitive-services/luis/client-libraries-rest-api?tabs=windows&pivots=programming-language-python
from azure.cognitiveservices.language.luis.authoring import LUISAuthoringClient
from azure.cognitiveservices.language.luis.authoring.models import ApplicationCreateObject
from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from msrest.authentication import CognitiveServicesCredentials
from functools import reduce
import json, time, uuid


#  1 - Setup LUIS API Variables
#     authoringKey = 'PASTE_YOUR_LUIS_AUTHORING_SUBSCRIPTION_KEY_HERE'
#     authoringEndpoint = 'PASTE_YOUR_LUIS_AUTHORING_ENDPOINT_HERE'
#     predictionKey = 'PASTE_YOUR_LUIS_PREDICTION_SUBSCRIPTION_KEY_HERE'
#     predictionEndpoint = 'PASTE_YOUR_LUIS_PREDICTION_ENDPOINT_HERE'
client = None
    
def quickstart():
    global client
    # We use a UUID to avoid name collisions.
    appName = "Intern Copy of V2" + str(uuid.uuid4())
    versionId = "0.6.1"
    intentName = None
#  2 - Connect to LUIS API, creating 'client' object
    client = LUISAuthoringClient(authoringEndpoint, CognitiveServicesCredentials(authoringKey))

quickstart()
runtimeCredentials = CognitiveServicesCredentials(predictionKey)
clientRuntime = LUISRuntimeClient(endpoint=predictionEndpoint, credentials=runtimeCredentials)

#takes in utterance, returns predictionResponse
def response(utterance):
    predictionRequest = {'query': utterance}
    predictionResponse = clientRuntime.prediction.get_slot_prediction(appId, "Production", predictionRequest, verbose=True)
    
    entities = []
    for key in predictionResponse.prediction.entities['$instance'].keys():
        e = predictionResponse.prediction.entities['$instance'][key][0]
        entityjso = {
            'entity': key,
            'startPos': e['startIndex'],
            'endPos': e['startIndex'] + e['length'] - 1,
            'children': []
        }
        entities.append(entityjso)
        
    jso = {
        'text': utterance,
        'intent': predictionResponse.prediction.top_intent,
        'entities': entities
    }
    return jso
    
def responses(utterances):
    jsonData = []
    for u in utterances:
        jsonData.append(response(u))
    with open('luis.json','w') as luisjson :
        json.dump(jsonData, luisjson, indent=4, separators=(',',': '))


    


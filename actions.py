# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []
# This files contains your custom actions which can be used to run
# custom Python code.
from rasa_sdk.actions import Action
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionShowTypeOfServices(Action):
    def name(self):
        return 'actionshowtypeofservices'
    def run(self, dispatcher, tracker,domain):
        message = "we provide following type of services"
        buttons = [{'title': 'SAP ISU',
                   'payload': '{}'.format('SAP ISU')},
                  {'title': 'WEB DEVELOPMENT',
                   'payload': '{}'.format('WEB DEVELOPMENT')},
                  {'title': 'MOBILE APPLICATION DEVELOPMENT',
                   'payload': '{}'.format('MOBILE APPLICATION DEVELOPMENT')},
                  {'title': 'DIGITAL MARKETING',
                   'payload': '{}'.format('DIGITAL MARKETING')},
                  {'title': 'TRAINING AND MENTORING',
                   'payload': '{}'.format('TRAINING AND MENTORING')},
                  {'title': 'RESEARCH CONSULTANCY',
                   'payload': '{}'.format('RESEARCH CONSULTANCY')}   
                   ]
        dispatcher.utter_button_message(message, buttons=buttons)

class FetchTypeOfServices(Action):
	def name(self):
		return 'fetchtypeofservices'

	def run(self,dispatcher,tracker,domain):
		service_type = tracker.get_slot('type_of_services')
		service_link = "http://oretes.com/services/"
		response = "We are providing {} services. You can get more info on {} from {}".format(service_type,service_type,service_link)
		dispatcher.utter_message(response)
		return [SlotSet('type_of_services', service_type)]

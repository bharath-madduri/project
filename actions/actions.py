import re
import pytz
import json
import pickle
import random
import smtplib
import datetime
import requests
import mysql.connector
from datetime import timedelta
from rasa_sdk import Action, Tracker
from email.message import EmailMessage
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from typing import Any, Text, Dict, List, Union
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset, FollowupAction
from rasa_sdk.forms import FormValidationAction, FormAction, REQUESTED_SLOT
from rasa_sdk.events import SlotSet, UserUtteranceReverted, SessionStarted
from rasa_sdk.types import DomainDict

# cent percent  35cCbsE6EF4dxgVQnh_


def test_email(name, phone, email):
    EMAIL_ADDRESS = 'noreply@mauvetix.com'
    EMAIL_PASSWORD = 'Lacasa@201'
    EMAIL_CLIENT = 'support@centpercent.co'
    msg = EmailMessage()
    msg['Subject'] = 'Website Enquiries'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_CLIENT
    localtime = datetime.datetime.now(pytz.timezone(
        'Asia/Kolkata')).isoformat('T', 'seconds')
    localtime = datetime.datetime.strptime(localtime, '%Y-%m-%dT%H:%M:%S%z')
    localtime = localtime.strftime("%Y-%m-%d %H:%M")
    msg.set_content(''' 
    <!DOCTYPE html>
    <html lang="en">

    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <link rel="stylesheet" href="path/to/font-awesome/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
        .container {
            width: 90%;
            overflow: hidden;
            background: #d3d3d3;
            margin: 20px auto;
            padding: 20px;
            text-align: center;
        }

        .content {
            background: #fff;
            padding: 30px;
        }

        img {
            width: 40px;
            height: 40px;
            margin: 2px;
        }

          
        table {
            display: table;
            border-collapse: separate;
            box-sizing: border-box;
            text-indent: initial;
            border-spacing: 2px;
            border-color: grey;
        }
    </style>
    <title>Document</title>
    </head>

    <body>
    <div class="container">
        <div class="row">
            <img src="https://api.mauvechat.io/static/mauvechat.png"
                alt="Mauvechat" style="width:133px;height:49px;">
            <table cellpadding="0" cellspacing="0" border="0" align="center" style="background-clip:padding-box;border-collapse:collapse;color:#545454;font-family:'Helvetica Neue',Arial,sans-serif;font-size:13px;line-height:20px;margin:0 auto;width:100%">
                <tbody>
                    <tr>
                        <td valign="top">
                            <table cellpadding="0" cellspacing="0" border="0"  style="background-clip:padding-box;border-collapse:separate;width:100%;background:#fff;border-radius:3px;padding-bottom:20px">
                                <tbody>
                                    <tr>
                                        <td style="background-clip:padding-box;color:#545454;font-family:'Helvetica Neue',Arial,sans-serif;font-size:14px;line-height:20px;overflow:hidden;padding:15px 20px" colspan="3">
                                            <p style="margin:10px 0;font-size:20px;text-align:center">
                                                Offline message sent by '''+str(name.capitalize())+'''
                                            </p>
                                            <div style="width:100%;height:1px;background:#e4e4e4;margin:20px 0"></div>
                                            <p style="margin:5px 0;text-align:center">
                                                '''+str(localtime)+'''
                                            </p>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td
                                            style="padding:5px 5px 5px 20px;text-align:right;vertical-align:top;width:20%;min-width:60px">
                                            Name
                                        </td>
                                        <td
                                            style="width:5%;min-width:20px;text-align:center;vertical-align:top;padding:5px 0">
                                            &nbsp;:&nbsp;</td>
                                        <td
                                            style="overflow:hidden;padding:5px 20px 5px 5px;text-align:left; width:80%;vertical-align:top">
                                            '''+str(name.capitalize())+'''
                                        </td>
                                    </tr>
                                    <tr>
                                        <td
                                            style="padding:5px 5px 5px 20px;text-align:right;vertical-align:top;width:20%;min-width:60px">
                                            Email
                                        </td>
                                        <td
                                            style="width:5%;min-width:20px;text-align:center;vertical-align:top;padding:5px 0">
                                            &nbsp;:&nbsp;</td>
                                        <td
                                            style="overflow:hidden;padding:5px 20px 5px 5px;text-align:left;width:80%;vertical-align:top">
                                            '''+str(email)+'''
                                        </td>
                                    </tr>
                                    <tr>
                                        <td
                                            style="padding:5px 5px 5px 20px;text-align:right;vertical-align:top;width:20%;min-width:60px">
                                            Mobile
                                        </td>
                                        <td
                                            style="width:5%;min-width:20px;text-align:center;vertical-align:top;padding:5px 0">
                                            &nbsp;:&nbsp;</td>
                                        <td
                                            style="overflow:hidden;padding:5px 20px 5px 5px;text-align:left;width:80%;vertical-align:top">
                                            '''+str(phone)+'''
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                </tbody>
            </table>

            <p>Follows us on :</p>
            <a href="https://www.facebook.com/mauvechat"> <img src="https://cdn3.iconfinder.com/data/icons/capsocial-round/500/facebook-256.png"  alt=""> </a>
            <a href="https://www.linkedin.com/company/mauvetix-solutions-pvt-ltd/"><img src="https://cdn3.iconfinder.com/data/icons/material-design-social-icons/152/Linkedin_icon-512.png" alt=""> </a>
        </div>

    </div>
    </body>

    </html>

     ''', subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    return


class ActionGetStarted35cCbsE6EF4dxgVQnh(Action):
    def name(self) -> Text:
        return "action_get_started_35cCbsE6EF4dxgVQnh"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text='Welcome to Centpercent. Our end to end plug and play OTT platform is all you will ever need.')
        dispatcher.utter_message(
            template="utter_35cCbsE6EF4dxgVQnh_get_started")
        return []


class ActionClose35cCbsE6EF4dxgVQnh(Action):
    def name(self) -> Text:
        return "action_close_35cCbsE6EF4dxgVQnh"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text='Cool, Let me know if you would need any assistance. Happy to help!')
        dispatcher.utter_message(
            text='Just say "Hi" or Hello" to start our conversation.')
        return []


class ActionOttSolutions35cCbsE6EF4dxgVQnh(Action):
    def name(self) -> Text:
        return "action_ott_solutions_35cCbsE6EF4dxgVQnh"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text='We help businesses develop innovative and cutting-edge Over-the-Top platforms and connected apps that are architected to deliver superior speed and reliability.')
        return []


class ActionIptv35cCbsE6EF4dxgVQnh(Action):
    def name(self) -> Text:
        return "action_iptv_35cCbsE6EF4dxgVQnh"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text='We help you develop end-to-end custom IPTV OTT solutions that suit your specific needs and allows customers to stream the content as and when they want.')
        return []


class ActionSubscription35cCbsE6EF4dxgVQnh(Action):
    def name(self) -> Text:
        return "action_subscription_35cCbsE6EF4dxgVQnh"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text='Fast and secured - One single interface to manage your subscribers. Acquiring and engaging your customers has never been so simple.')
        return []


class ActionContent35cCbsE6EF4dxgVQnh(Action):
    def name(self) -> Text:
        return "action_content_35cCbsE6EF4dxgVQnh"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text='Our comprehensive content management platform performs key functions of encoding, DRM protection, ABR, CDN & more.')
        return []


class ActionMonetization35cCbsE6EF4dxgVQnh(Action):
    def name(self) -> Text:
        return "action_monetization_35cCbsE6EF4dxgVQnh"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text='With 100+ publishers and a state of art tracking platform, Go live with our Ad monetization solution in 48 hrs.')
        return []


class ActionForm35cCbsE6EF4dxgVQnh(Action):
    def name(self) -> Text:
        return "action_form_35cCbsE6EF4dxgVQnh"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        buttons = []
        buttons.append(
            {'title': 'Yes', 'payload': '/35cCbsE6EF4dxgVQnh_affirm'})
        buttons.append({'title': 'No', 'payload': '/35cCbsE6EF4dxgVQnh_deny'})
        dispatcher.utter_message(
            text='Would you like a demo and check out our platform capabilities?', buttons=buttons)
        return []


class ActionAskName35cCbsE6EF4dxgVQnh(Action):
    def name(self) -> Text:
        return "action_ask_name_35cCbsE6EF4dxgVQnh"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_slot("name_invalid_35cCbsE6EF4dxgVQnh") == 'True':
            dispatcher.utter_message(text='Please enter your name.')
            return [SlotSet("name_invalid_35cCbsE6EF4dxgVQnh", 'False')]
        else:
            dispatcher.utter_message(text='May I have your name?')
        return []


class ValidateNameForm35cCbsE6EF4dxgVQnh(FormValidationAction):
    def name(self) -> Text:
        return "name_form_35cCbsE6EF4dxgVQnh"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["name_35cCbsE6EF4dxgVQnh"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {"name_35cCbsE6EF4dxgVQnh": [self.from_text()]}


class ValidateName35cCbsE6EF4dxgVQnh(FormValidationAction):
    def name(self) -> Text:
        return "validate_name_form_35cCbsE6EF4dxgVQnh"

    def validate_name_35cCbsE6EF4dxgVQnh(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker,
                                         domain: Dict[Text, Any], ) -> Dict[Text, Any]:

        a = tracker.get_slot('name_invalid_35cCbsE6EF4dxgVQnh')
        slot_value = slot_value.replace("35cCbsE6EF4dxgVQnh_", "")
        if a != 'True':
            if (re.search(r"^[a-zA-Z ]*$", slot_value)):
                return {"name_35cCbsE6EF4dxgVQnh": slot_value, "name_counter_35cCbsE6EF4dxgVQnh": 1, "name_invalid_35cCbsE6EF4dxgVQnh": "True"}
            else:
                dispatcher.utter_message(
                    text="Need your name to move forward.")
                return {"name_35cCbsE6EF4dxgVQnh": None}
        return {"name_counter_35cCbsE6EF4dxgVQnh": tracker.get_slot('name_counter_35cCbsE6EF4dxgVQnh') + 1}


class ActionAskEmail35cCbsE6EF4dxgVQnh(Action):
    def name(self) -> Text:
        return "action_ask_email_35cCbsE6EF4dxgVQnh"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_slot("email_invalid_35cCbsE6EF4dxgVQnh") == 'True':
            dispatcher.utter_message(text='Please enter your email id.')
            return [SlotSet("email_invalid_35cCbsE6EF4dxgVQnh", 'False')]
        else:
            dispatcher.utter_message(text='May I have your Email Id?')
        return []


class ValidateEmailForm35cCbsE6EF4dxgVQnh(FormValidationAction):
    def name(self) -> Text:
        return "email_form_35cCbsE6EF4dxgVQnh"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["email_35cCbsE6EF4dxgVQnh"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {"email_35cCbsE6EF4dxgVQnh": [self.from_text()]}


class ValidateEmail35cCbsE6EF4dxgVQnh(FormValidationAction):
    def name(self) -> Text:
        return "validate_email_form_35cCbsE6EF4dxgVQnh"

    def validate_email_35cCbsE6EF4dxgVQnh(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker,
                                          domain: DomainDict, ) -> Dict[Text, Any]:
        a = tracker.get_slot('email_invalid_35cCbsE6EF4dxgVQnh')
        slot_value = slot_value.replace("35cCbsE6EF4dxgVQnh_", "")
        if a != 'True':
            if (re.search(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", slot_value)):
                return {"email_35cCbsE6EF4dxgVQnh": slot_value, "email_counter_35cCbsE6EF4dxgVQnh": 1, "email_invalid_35cCbsE6EF4dxgVQnh": 'True'}
            else:
                dispatcher.utter_message(
                    text="Sorry, you've entered incorrect email id.")
                return {"email_35cCbsE6EF4dxgVQnh": None}
        return {"email_counter_35cCbsE6EF4dxgVQnh": tracker.get_slot('email_counter_35cCbsE6EF4dxgVQnh') + 1}


class ActionAskNumber35cCbsE6EF4dxgVQnh(Action):
    def name(self) -> Text:
        return "action_ask_number_35cCbsE6EF4dxgVQnh"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_slot("number_invalid_35cCbsE6EF4dxgVQnh") == 'True':
            dispatcher.utter_message(text='Please enter your mobile number.')
            return [SlotSet("number_invalid_35cCbsE6EF4dxgVQnh", 'False')]
        else:
            dispatcher.utter_message(text='May I have your Mobile number?')
        return []


class ValidateNumberForm35cCbsE6EF4dxgVQnh(FormValidationAction):
    def name(self) -> Text:
        return "number_form_35cCbsE6EF4dxgVQnh"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["number_35cCbsE6EF4dxgVQnh"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {"number_35cCbsE6EF4dxgVQnh": [self.from_text()]}


class ValidateNumber35cCbsE6EF4dxgVQnh(FormValidationAction):
    def name(self) -> Text:
        return "validate_number_form_35cCbsE6EF4dxgVQnh"

    def validate_number_35cCbsE6EF4dxgVQnh(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker,
                                           domain: Dict[Text, Any], ) -> Dict[Text, Any]:
        a = tracker.get_slot('number_invalid_35cCbsE6EF4dxgVQnh')
        slot_value = slot_value.replace("35cCbsE6EF4dxgVQnh_", "")
        if a != 'True':
            if (re.search(r"^[6789]\d{9}$", slot_value)):
                return {"number_35cCbsE6EF4dxgVQnh": slot_value, "number_counter_35cCbsE6EF4dxgVQnh": 1, "number_invalid_35cCbsE6EF4dxgVQnh": 'True'}
            else:
                dispatcher.utter_message(
                    text="Sorry, you've entered incorrect mobile number.")
                return {"number_35cCbsE6EF4dxgVQnh": None}
        return {"number_counter_35cCbsE6EF4dxgVQnh": tracker.get_slot('number_counter_35cCbsE6EF4dxgVQnh') + 1}


class ActionSubmit35cCbsE6EF4dxgVQnh(Action):
    def name(self) -> Text:
        return "action_submit_35cCbsE6EF4dxgVQnh"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if ((tracker.get_slot("name_counter_35cCbsE6EF4dxgVQnh") > 1) and (tracker.get_slot("email_counter_35cCbsE6EF4dxgVQnh") > 1) and (tracker.get_slot("number_counter_35cCbsE6EF4dxgVQnh") > 1)):
            dispatcher.utter_message(
                text='We have your details already.Our sales guy will get in touch with you within 24 hrs.')
        else:
            name = tracker.get_slot('name_35cCbsE6EF4dxgVQnh')
            phone = tracker.get_slot('number_35cCbsE6EF4dxgVQnh')
            email = tracker.get_slot('email_35cCbsE6EF4dxgVQnh')
            test_email(name, phone, email)
            dispatcher.utter_message(
                text='Thanks for sharing. I just send across our product deck to your email for your perusal.')
            dispatcher.utter_message(
                text='Your details has been shared with my sales guy - Koundinya.')
            dispatcher.utter_message(
                text='You should get a call from him within 24 hrs to schedule the demo.')
        dispatcher.utter_message(
            template="utter_35cCbsE6EF4dxgVQnh_anythingelse")
        return []


#  appointment booking sbCc4FE6_
class ValidateContactFormsbCc4FE6(FormValidationAction):
    def name(self) -> Text:
        return "contact_form_sbCc4FE6"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["name_sbCc4FE6", "mobile_sbCc4FE6", "email_sbCc4FE6"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {"name_sbCc4FE6": [self.from_text()], "mobile_sbCc4FE6": [self.from_text()], "email_sbCc4FE6": [self.from_text()]}


class ValidateContactsbCc4FE6(FormValidationAction):
    def name(self) -> Text:
        return "validate_contact_form_sbCc4FE6"

    def validate_name_sbCc4FE6(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker,
                               domain: Dict[Text, Any], ) -> Dict[Text, Any]:
        slot_value = slot_value.replace("sbCc4FE6_", "")
        if (re.search(r"^[a-zA-Z ]*$", slot_value)):
            return {"name_sbCc4FE6": slot_value}
        else:
            dispatcher.utter_message(text="Need your name to move forward.")
            return {"name_sbCc4FE6": None, "name_invalid_sbCc4FE6": 'True'}

    def validate_number_sbCc4FE6(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker,
                                 domain: Dict[Text, Any], ) -> Dict[Text, Any]:
        slot_value = slot_value.replace("sbCc4FE6_", "")
        if (re.search(r"^[6789]\d{9}$", slot_value)):
            return {"number_sbCc4FE6": slot_value}
        else:
            dispatcher.utter_message(
                text="Sorry, you've entered incorrect mobile number.")
            return {"number_sbCc4FE6": None, "number_invalid_sbCc4FE6": 'True'}

    def validate_email_sbCc4FE6(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker,
                                domain: DomainDict, ) -> Dict[Text, Any]:
        slot_value = slot_value.replace("sbCc4FE6_", "")
        if (re.search(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", slot_value)):
            return {"email_sbCc4FE6": slot_value}
        else:
            dispatcher.utter_message(
                text="Sorry, you've entered incorrect email id.")
            return {"email_sbCc4FE6": None, "email_invalid_sbCc4FE6": 'True'}


class ValidateBookingFormsbCc4FE6(FormValidationAction):
    def name(self) -> Text:
        return "booking_form_sbCc4FE6"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["name_sbCc4FE6", "mobile_sbCc4FE6", "booking_sbCc4FE6"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {"name_sbCc4FE6": [self.from_text()], "mobile_sbCc4FE6": [self.from_text()], "booking_sbCc4FE6": [self.from_text()]}


class ValidateBookingsbCc4FE6(FormValidationAction):
    def name(self) -> Text:
        return "validate_booking_form_sbCc4FE6"

    def validate_name_sbCc4FE6(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker,
                               domain: Dict[Text, Any], ) -> Dict[Text, Any]:
        slot_value = slot_value.replace("sbCc4FE6_", "")
        if (re.search(r"^[a-zA-Z ]*$", slot_value)):
            return {"name_sbCc4FE6": slot_value}
        else:
            dispatcher.utter_message(text="Need your name to move forward.")
            return {"name_sbCc4FE6": None, "name_invalid_sbCc4FE6": 'True'}

    def validate_number_sbCc4FE6(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker,
                                 domain: Dict[Text, Any], ) -> Dict[Text, Any]:
        slot_value = slot_value.replace("sbCc4FE6_", "")
        if (re.search(r"^[6789]\d{9}$", slot_value)):
            return {"number_sbCc4FE6": slot_value}
        else:
            dispatcher.utter_message(
                text="Sorry, you've entered incorrect mobile number.")
            return {"number_sbCc4FE6": None, "number_invalid_sbCc4FE6": 'True'}


class ActionAskNamesbCc4FE6(Action):
    def name(self) -> Text:
        return "action_ask_name_sbCc4FE6"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_slot("name_invalid_sbCc4FE6") == 'True':
            dispatcher.utter_message(text='Please enter your name.')
            return [SlotSet("name_invalid_sbCc4FE6", 'False')]
        else:
            dispatcher.utter_message(text='May I have your name?')
        return []


class ActionAskEmailsbCc4FE6(Action):
    def name(self) -> Text:
        return "action_ask_email_sbCc4FE6"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_slot("email_invalid_sbCc4FE6") == 'True':
            dispatcher.utter_message(text='Please enter your email id.')
            return [SlotSet("email_invalid_sbCc4FE6", 'False')]
        else:
            dispatcher.utter_message(text='May I have your Email Id?')
        return []


class ActionAskNumbersbCc4FE6(Action):
    def name(self) -> Text:
        return "action_ask_number_sbCc4FE6"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_slot("number_invalid_sbCc4FE6") == 'True':
            dispatcher.utter_message(text='Please enter your mobile number.')
            return [SlotSet("number_invalid_sbCc4FE6", 'False')]
        else:
            dispatcher.utter_message(text='May I have your Mobile number?')
        return []


class ActionBookingStatussbCc4FE6(Action):
    def name(self) -> Text:
        return "action_booking_status_sbCc4FE6"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Your vehicle shipment is expected to reach us in the next 7 days.")
        dispatcher.utter_message(
            text="Our sales team will be in touch with you with updates on your delivery.")
        dispatcher.utter_message(
            text="You can also call us on +91-8886333327 for any enquiries.")
        dispatcher.utter_message(template='utter_sbCc4FE6_anythingelse')

        return [AllSlotsReset()]


class ActionWelcomesbCc4FE6(Action):
    def name(self) -> Text:
        return "action_welcome_sbCc4FE6"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Hello, welcome to Mauvetix appointment booking.")
        dispatcher.utter_message(
            template="utter_sbCc4FE6_get_started")

        return [AllSlotsReset()]


class ActionServiceOptionssbCc4FE6(Action):
    def name(self) -> Text:
        return "action_service_options_sbCc4FE6"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        model = tracker.latest_message.get('text')
        model = model.replace("sbCc4FE6_", "")
        buttons = []
        buttons.append(
            {"title": "Free service", "payload": 'sbCc4FE6_Free sbCc4FE6_service'})
        buttons.append(
            {"title": "Paid service", "payload": 'sbCc4FE6_Paid sbCc4FE6_service'})
        buttons.append({"title": "Others", "payload": 'sbCc4FE6_Others'})

        dispatcher.utter_message(
            text="Following are the service options for you.")
        dispatcher.utter_message(
            text="Please select one of the following", buttons=buttons)

        return [SlotSet("model_sbCc4FE6", model)]


def day():
    today = datetime.datetime.now(pytz.timezone(
        'Asia/Kolkata')).isoformat('T', 'seconds')
    one = datetime.datetime.strptime(
        today, '%Y-%m-%dT%H:%M:%S%z') + timedelta(days=1)
    two = datetime.datetime.strptime(
        today, '%Y-%m-%dT%H:%M:%S%z') + timedelta(days=2)
    three = datetime.datetime.strptime(
        today, '%Y-%m-%dT%H:%M:%S%z') + timedelta(days=3)
    four = datetime.datetime.strptime(
        today, '%Y-%m-%dT%H:%M:%S%z') + timedelta(days=4)

    buttons = []
    buttons.append({"title": one.strftime("%b-%d-%Y"),
                    "payload": "{0}".format(one)})
    buttons.append({"title": two.strftime("%b-%d-%Y"),
                    "payload": "{0}".format(two)})
    buttons.append({"title": three.strftime("%b-%d-%Y"),
                    "payload": "{0}".format(three)})
    buttons.append({"title": four.strftime("%b-%d-%Y"),
                    "payload": "{0}".format(four)})

    return buttons


class ActionTimesbCc4FE6(Action):
    def name(self):
        return "action_time_sbCc4FE6"

    def run(self, dispatcher, tracker, domain):
        service_type = tracker.latest_message.get('text')
        service_type = service_type.replace("sbCc4FE6_", "")
        buttons = day()
        dispatcher.utter_message(
            text="When do you want to bring your vehicle?", buttons=buttons)
        return [SlotSet("service_type_sbCc4FE6", service_type)]


class ActionInformsbCc4FE6(Action):
    def name(self):
        return "action_inform_sbCc4FE6"

    def run(self, dispatcher, tracker, domain):
        date = tracker.latest_message.get('text')
        date = date.replace("sbCc4FE6_", "")
        date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S%z')
        date = date.replace(hour=10, minute=00)
        buttons = []
        buttons.append({"title": "Confirm", "payload": '/sbCc4FE6_affirm'})
        buttons.append({"title": "Cancel", "payload": '/sbCc4FE6_deny'})
        name = tracker.get_slot('name_sbCc4FE6')
        model = tracker.get_slot('model_sbCc4FE6')
        dispatcher.utter_message(
            text="**{0}**, the booking details are as follows: \n \n Model: **{1}** \n \n Date: **{2}** at **{3}:00AM** \n \n Service type: **{4}**".format(
                name.capitalize(), model, date.date(), date.hour, tracker.get_slot('service_type_sbCc4FE6')),
            buttons=buttons)
        date = str(date.date())
        return [SlotSet("date_sbCc4FE6", date)]


class ActionSubmitsbCc4FE6(Action):
    def name(self) -> Text:
        return "action_submit_sbCc4FE6"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        headers = {'Content-Type': 'application/json'}
        url = 'https://api.mauvechat.io/booking'
        # url = 'http://127.0.0.1:8000/booking'

        appointment = tracker.get_slot('date_sbCc4FE6')
        appointment = datetime.datetime.strptime(appointment, '%Y-%m-%d')
        appointment = appointment.isoformat('T', 'seconds') + '+05:30'
        appointment = datetime.datetime.strptime(
            appointment, '%Y-%m-%dT%H:%M:%S%z')
        appointment = appointment.replace(
            hour=10, minute=00, second=00).replace(tzinfo=None)

        message = [{'key': 'Model', 'value': tracker.get_slot(
            'model_sbCc4FE6')}, {'key': 'Service Type', 'value': tracker.get_slot('service_type_sbCc4FE6')}]

        data = {"Name": tracker.get_slot("name_sbCc4FE6"), "Email": tracker.get_slot("email_sbCc4FE6"),
                "Mobile": tracker.get_slot("number_sbCc4FE6"), "Message": message, "Source": 'Vehicle',
                "Appointment": str(appointment), "Company_id": "12", "Bot_id": "sbCc4FE6_"}

        response = requests.post(url, data=json.dumps(data), headers=headers)
        whatsapp_access_token = "EAAFw7Tvp3JoBAE6GKADRqMSSZBVDTDgjpE8n0PinmVVS17PTxCNseA1AjBQsciSQgCUBkXkCFduKYpyPYCqasF2zYJJoMaJfl74K1X52yyTFkpzXRFKnj0uZBiaEYT4FzBqI6D4pkkLG7k5tkemwAqHnjZAhZCPQlLsR3SaiI5ZBDHhZBrS6b3ZCQuZBYQRnF4RRpaptiXwAPQZDZD"
        from_phone_number_id = '106821558718090'
        to = '91'+tracker.get_slot("number_sbCc4FE6")
        url = f"https://graph.facebook.com/v13.0/{from_phone_number_id}/messages"
        headers = {'Authorization': 'Bearer {}'.format(
            whatsapp_access_token), "Content-Type": "application/json"}
        template_welcome = {
            "messaging_product": "whatsapp",
            "to": to,
            "type": "template",
            "template": {
                    "name": "vehicle_booking",
                    "language": {"code": "en"},
                    "components": [{
                        "type": "body",
                        "parameters": [{
                            "type": "text",
                            "text": tracker.get_slot("name_sbCc4FE6")
                        },
                            {
                            "type": "text",
                            "text": tracker.get_slot("name_sbCc4FE6")
                        },
                            {
                            "type": "text",
                            "text": tracker.get_slot("number_sbCc4FE6")
                        },
                            {
                            "type": "text",
                            "text": tracker.get_slot("email_sbCc4FE6")
                        },
                            {
                            "type": "text",
                            "text": tracker.get_slot('model_sbCc4FE6')
                        },
                            {
                            "type": "text",
                            "text": tracker.get_slot('service_type_sbCc4FE6')
                        },
                            {
                            "type": "text",
                            "text": str(appointment)
                        }]
                    }]
            }
        }
        response2 = requests.post(
            url, data=json.dumps(template_welcome), headers=headers)
        print(response2.json())
        dispatcher.utter_message(
            text="Thank you, the booking has been confirmed.")
        dispatcher.utter_message(
            text="You will receive a SMS with the booking details along with representative contact details.")

        return [AllSlotsReset()]


class ActionAppointmentTimesbCc4FE6(Action):
    def name(self):
        return "action_appointment_time_sbCc4FE6"

    def run(self, dispatcher, tracker, domain):
        buttons = day()
        department = tracker.latest_message.get('text')
        department = department.replace("sbCc4FE6_", "")
        dispatcher.utter_message(
            text="When would you like to visit us for consultation?", buttons=buttons)
        return [SlotSet("department_sbCc4FE6", department)]


def available_slots(date):

    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="mauvetix"
    )
    mycursor = mydb.cursor()
    # converting selected date from string to datetime object
    str_to_date = datetime.datetime.strptime(date, '%Y-%m-%d')
    # SQL Query to fetch events on selected date
    query = "SELECT convert_tz(appointment, '+00:00','+05:30') from app_mauvebookings where company_id = 12 AND source = 'Doctor' AND DATE(appointment) = DATE(%(value)s) "
    params = {'value': str_to_date.date()}
    mycursor.execute(query, params)
    myresult = mycursor.fetchall()
    events = []
    for i in myresult:
        temp = {'start': i[0], 'end': i[0] + timedelta(minutes=30)}
        events.append(temp)

    # working time period
    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    timeMin = date.replace(hour=10, minute=00, second=00).replace(tzinfo=None)
    timeMax = date.replace(hour=13, minute=00, second=00).replace(tzinfo=None)
    # checking if there are events and sorting
    if events:
        events.sort(key=lambda x: x['start'])
        events = events
    else:
        temp = {'start': timeMin, 'end': timeMax}
        events.append(temp)
    # finding free slots from the occupied events
    tstart = timeMin
    tstop = timeMax
    tp = [(tstart, tstart)]
    free_time = []
    for t in events:
        tp.append((t['start'], t['end']))
    tp.append((tstop, tstop))
    i = 1
    while i < len(tp):
        if (tp[i][0] < tp[i - 1][1]):
            start_times = [tp[i - 1][0], tp[i][0]]
            end_times = [tp[i - 1][1], tp[i][1]]
            tp[i - 1] = (min(start_times), max(end_times))
            tp.pop(i)
        else:
            i += 1
    for i, v in enumerate(tp):
        if i > 0:
            if ((tp[i][0] - tp[i - 1][1]) > datetime.timedelta(seconds=0)):
                tf_start = tp[i - 1][1]
                delta = tp[i][0] - tp[i - 1][1]
                tf_end = tf_start + delta
                free_time.append((tf_start, tf_end))
    # splitting available time period
    interval = datetime.timedelta(minutes=30)
    periods = []
    if free_time:
        for i in range(len(free_time)):
            tstart = free_time[i][0]
            tend = free_time[i][1]
            period_start = tstart
            while period_start < tend:
                period_end = min(period_start + interval, tend)
                periods.append((period_start, period_end))
                period_start = period_end
    else:
        tstart = events[0]['start']
        tend = events[0]['end']
        period_start = tstart
        while period_start < tend:
            period_end = min(period_start + interval, tend)
            periods.append((period_start, period_end))
            period_start = period_end

    buttons = []
    for i in periods:
        a = '{:02d}'.format(i[0].hour), ':', '{:02d}'.format(i[0].minute), '-'
        b = '{:02d}'.format(i[1].hour), ':', '{:02d}'.format(i[1].minute)
        c = a + b
        buttons.append({"title": c, "payload": '{0}'.format(c)})
    return buttons


class ActionSlotssbCc4FE6(Action):
    def name(self):
        return "action_slots_sbCc4FE6"

    def run(self, dispatcher, tracker, domain):
        doctor = tracker.latest_message.get('text')
        doctor = doctor.replace("sbCc4FE6_", "")
        buttons = available_slots(tracker.get_slot('date_sbCc4FE6'))

        dispatcher.utter_message(
            text="The following slots are available on {0} for consultation".format(tracker.get_slot('date_sbCc4FE6')))
        dispatcher.utter_message(
            text="Choose your slot", buttons=buttons)
        return [SlotSet("doctor_sbCc4FE6", doctor)]


def create(date, email, time, name):
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly',
              'https://www.googleapis.com/auth/calendar.addons.execute',
              'https://www.googleapis.com/auth/calendar.settings.readonly',
              'https://www.googleapis.com/auth/calendar.events',
              'https://www.googleapis.com/auth/calendar',
              'https://www.googleapis.com/auth/calendar.events.readonly']
    credentials = pickle.load(open(
        'C:/Users/Administrator/Desktop/Mounika/centpercent/token.pkl', 'rb'))
    service = build("calendar", "v3", credentials=credentials)
    start = datetime.datetime.strptime(date+'T'+time, "%Y-%m-%dT%H:%M")
    end = start + timedelta(minutes=30)
    # start = datetime.datetime(year, month, day, hour, minute)
    # end = start + timedelta(minutes=30)
    time = 'Asia/Kolkata'
    event = {
        'summary': 'Appointment confirmed',
        'location': 'Hospital',
        'description': 'Event created with google calendar',
        'start': {
            'dateTime': start.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': time,
        },
        'end': {
            'dateTime': end.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': time,
        },
        'attendees': [
            {'email': email}],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }
    dump = service.events().insert(calendarId='bharat@mauvetix.com',
                                   body=event, sendUpdates='all').execute()
    return


class ActionAppointmentSubmitsbCc4FE6(Action):
    def name(self) -> Text:
        return "action_appointment_submit_sbCc4FE6"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        time = tracker.latest_message.get('text')
        time = time.replace("sbCc4FE6_", "")
        temp = re.findall(r'\d+', time)
        res = list(map(int, temp))
        doctor = tracker.get_slot('doctor_sbCc4FE6')
        time = str(res[0]) + ':' + '{:02d}'.format(res[1])
        date = tracker.get_slot("date_sbCc4FE6")
        email = tracker.get_slot("email_sbCc4FE6")
        name = tracker.get_slot("name_sbCc4FE6")
        c = create(date, email, time, name)
        dispatcher.utter_message(
            text="Thank you for choosing mauvetix clinic.")

        headers = {'Content-Type': 'application/json'}
        url = 'https://api.mauvechat.io/booking'
        # url = 'http://127.0.0.1:8000/booking'

        appointment = date + str('-') + str(res[0]) + str(':') + str(res[1])

        appointment = datetime.datetime.strptime(appointment, '%Y-%m-%d-%H:%M')

        appointment = appointment.isoformat('T', 'seconds')

        message = [{'key': 'Department', 'value': tracker.get_slot('department_sbCc4FE6')}, {
            'key': 'Dr.Name', 'value': doctor}]

        data = {"Name": name, "Email": email,
                "Mobile": tracker.get_slot("number_sbCc4FE6"), "Message": message, "Source": 'Doctor',
                "Appointment": appointment, "Company_id": "12", "Bot_id": "sbCc4FE6_"}

        response = requests.post(url, data=json.dumps(data), headers=headers)
        whatsapp_access_token = "EAAFw7Tvp3JoBAE6GKADRqMSSZBVDTDgjpE8n0PinmVVS17PTxCNseA1AjBQsciSQgCUBkXkCFduKYpyPYCqasF2zYJJoMaJfl74K1X52yyTFkpzXRFKnj0uZBiaEYT4FzBqI6D4pkkLG7k5tkemwAqHnjZAhZCPQlLsR3SaiI5ZBDHhZBrS6b3ZCQuZBYQRnF4RRpaptiXwAPQZDZD"
        from_phone_number_id = '106821558718090'
        to = '91'+tracker.get_slot("number_sbCc4FE6")
        url = f"https://graph.facebook.com/v13.0/{from_phone_number_id}/messages"
        headers = {'Authorization': 'Bearer {}'.format(
            whatsapp_access_token), "Content-Type": "application/json"}
        template_welcome = {
            "messaging_product": "whatsapp",
            "to": to,
            "type": "template",
            "template": {
                    "name": "doctor_appointment",
                    "language": {"code": "en"},
                    "components": [{
                        "type": "body",
                        "parameters": [
                            {
                                "type": "text",
                                "text": name
                            },
                            {
                                "type": "text",
                                "text": tracker.get_slot("number_sbCc4FE6")
                            },
                            {
                                "type": "text",
                                "text": email
                            },
                            {
                                "type": "text",
                                "text": tracker.get_slot('department_sbCc4FE6')
                            },
                            {
                                "type": "text",
                                "text": doctor
                            },
                            {
                                "type": "text",
                                "text": str(appointment)
                            },
                            {
                                "type": "text",
                                "text": str(time)
                            }]
                    }]
            }
        }
        response2 = requests.post(
            url, data=json.dumps(template_welcome), headers=headers)
        print(response2.json())

        dispatcher.utter_message(
            text="**{0}** appointment is confirmed for **{1}** at **{2}AM** with **{3}**.".format(name.capitalize(), date, time, doctor))
        dispatcher.utter_message(
            text=" You will get a confirmation Email, SMS along with your appointment details shortly."
        )

        return [AllSlotsReset()]


class ActionBikesCarouselsbCc4FE6(Action):
    def name(self) -> Text:
        return "action_bikes_carousel_sbCc4FE6"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        test_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "KTM",
                        # "subtitle": "Our arts curriculum  includes a wide range of activities- painting, pottery, music , theatre and literary arts.",
                        "image_url": "https://i.ibb.co/NYGK2Ny/ktm-duke5fd45dd351563.jpg",
                        "buttons": [
                            {
                                "title": "Specifications",
                                "url": "https://www.mauvechat.io/appointment-bookings/",
                                "type": "web_url"
                            },
                            {
                                "title": "Get a quote",
                                "url": "https://www.mauvechat.io/appointment-bookings/",
                                "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Royal Enfield",
                        # "subtitle": "The school offers, well maintained sports infrastructure and offers 10 different activities from cricket to gymnastics.",
                        "image_url": "https://i.ibb.co/fXmC7WJ/20210901112431-2021-Classic-launch.jpg",
                        "buttons": [
                            {
                                "title": "Specifications",
                                "url": "https://www.mauvechat.io/appointment-bookings/",
                                "type": "web_url"
                            },
                            {
                                "title": "Get a quote",
                                "url": "https://www.mauvechat.io/appointment-bookings/",
                                "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Pulsar",
                        # "subtitle": "We offer a wide range of after school clubs to nurture essential skills in a student - drama, orators, science, culinary, photography and writing clubs.",
                        "image_url": "https://i.ibb.co/4gBCzSM/bajaj-pulsar-rs-2005fd991ddb5386.jpg",
                        "buttons": [
                            {
                                "title": "Specifications",
                                "url": "https://www.mauvechat.io/appointment-bookings/",
                                "type": "web_url"
                            },
                            {
                                "title": "Get a quote",
                                "url": "https://www.mauvechat.io/appointment-bookings/",
                                "type": "web_url"
                            }
                        ]
                    }
                ]
            }
        }

        dispatcher.utter_message(attachment=test_carousel)
        return []


class ActionDoctorSpecialityCarouselsbCc4FE6(Action):
    def name(self) -> Text:
        return "action_doctor_speciality_carousel_sbCc4FE6"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        test_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Cardiology",
                        # "subtitle": "MS, FICS, FIAGES 23 Years Of Experience",
                        "image_url": "https://i.ibb.co/6w94wbw/nm-ten-signs-cardiologist-preview.jpg",
                        "buttons": [
                            {
                                "title": "Read more",
                                "url": "https://www.mauvechat.io/appointment-bookings/",
                                "type": "web_url"
                            },
                            {
                                "title": "Book an appointment",
                                "type": "postback",
                                "payload": "/sbCc4FE6_doctor_book"

                            }
                        ]
                    },
                    {
                        "title": "Orthopedic",
                        # "subtitle": "MBBS, FICS 13 Years Of Experience",
                        "image_url": "https://i.ibb.co/g3w4w8g/ORTOPEDIC.png",
                        "buttons": [
                            {
                                "title": "Read more",
                                "url": "https://www.mauvechat.io/appointment-bookings/",
                                "type": "web_url"
                            },
                            {
                                "title": "Book an appointment",
                                "type": "postback",
                                "payload": "/sbCc4FE6_doctor_book"

                            }
                        ]
                    },
                    {
                        "title": "E&T",
                        # "subtitle": "MBBS, FICS 13 Years Of Experience",
                        "image_url": "https://i.ibb.co/3zn88t3/d76a34ae0907c4919a8392bb89f71bb5.jpg",
                        "buttons": [
                            {
                                "title": "Read more",
                                "url": "https://www.mauvechat.io/appointment-bookings/",
                                "type": "web_url"
                            },
                            {
                                "title": "Book an appointment",
                                "type": "postback",
                                "payload": "/sbCc4FE6_doctor_book"

                            }
                        ]
                    },
                    {
                        "title": "Dermatology",
                        # "subtitle": "MBBS, FICS 13 Years Of Experience",
                        "image_url": "https://i.ibb.co/zh06Bsm/der-1024x678.jpg",
                        "buttons": [
                            {
                                "title": "Read more",
                                "url": "https://www.mauvechat.io/appointment-bookings/",
                                "type": "web_url"
                            },
                            {
                                "title": "Book an appointment",
                                "type": "postback",
                                "payload": "/sbCc4FE6_doctor_book"

                            }
                        ]
                    }
                ]
            }
        }

        dispatcher.utter_message(attachment=test_carousel)
        return []


class ActionSpecialityCarouselsbCc4FE6(Action):
    def name(self) -> Text:
        return "action_speciality_carousel_sbCc4FE6"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        test_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Dr.Sanjeeva Alijarla",
                        "subtitle": "MS, FICS, FIAGES 23 Years Of Experience",
                        "image_url": "https://i.ibb.co/F43gGt1/doctor-character-background-1270-84.jpg",
                        "buttons": [
                            {
                                "title": "Read more",
                                "url": "https://www.mauvechat.io/appointment-bookings/",
                                "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Dr.Sreevalli",
                        "subtitle": "MBBS, FICS, BHMS  13 Years Of Experience",
                        "image_url": "https://i.ibb.co/NZmm4xN/F-dtr-1554191117.png",
                        "buttons": [
                            {
                                "title": "Read more",
                                "url": "https://www.mauvechat.io/appointment-bookings/",
                                "type": "web_url"
                            }
                        ]
                    }
                ]
            }
        }

        dispatcher.utter_message(attachment=test_carousel)
        return []


class ActionSelectCarouselsbCc4FE6(Action):
    def name(self) -> Text:
        return "action_select_carousel_sbCc4FE6"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        date = tracker.latest_message.get('text')
        date = date.replace("sbCc4FE6_", "")
        date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S%z')
        test_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Dr.Sanjeeva Alijarla",
                        "subtitle": "MS, FICS, FIAGES 23 Years Of Experience",
                        "image_url": "https://i.ibb.co/F43gGt1/doctor-character-background-1270-84.jpg",
                        "buttons": [
                            {
                                "title": "Confirm booking",
                                "type": "postback",
                                "payload": "sbCc4FE6_Dr.Sanjeeva sbCc4FE6_Alijarla"

                            },
                            {
                                "title": "Know your doctor",
                                "url": "https://www.mauvechat.io/appointment-bookings/",
                                "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Dr.Sreevalli",
                        "subtitle": "MBBS, FICS, FIAGES 13 Years Of Experience",
                        "image_url": "https://i.ibb.co/NZmm4xN/F-dtr-1554191117.png",
                        "buttons": [
                            {
                                "title": "Confirm booking",
                                "type": "postback",
                                "payload": "sbCc4FE6_Dr.Sreevalli"

                            },
                            {
                                "title": "Know your doctor",
                                "url": "https://www.mauvechat.io/appointment-bookings/",
                                "type": "web_url"
                            }
                        ]
                    }
                ]
            }
        }
        dispatcher.utter_message(
            text="Dr.Sanjeeva Alijarla & Dr.Sreevalli are available on {0}".format(date.date()))
        dispatcher.utter_message(attachment=test_carousel)
        return [SlotSet("date_sbCc4FE6", str(date.date()))]


# brundavan qFH0i9NeQv_
class ValidateContactFormqFH0i9NeQv(FormValidationAction):
    def name(self) -> Text:
        return "contact_form_qFH0i9NeQv"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["name_qFH0i9NeQv", "mobile_qFH0i9NeQv", "email_qFH0i9NeQv"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {"name_qFH0i9NeQv": [self.from_text()], "mobile_qFH0i9NeQv": [self.from_text()], "email_qFH0i9NeQv": [self.from_text()]}


class ValidateContactqFH0i9NeQv(FormValidationAction):
    def name(self) -> Text:
        return "validate_contact_form_qFH0i9NeQv"

    def validate_name_qFH0i9NeQv(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker,
                                 domain: Dict[Text, Any], ) -> Dict[Text, Any]:
        slot_value = slot_value.replace("qFH0i9NeQv_", "")
        if (re.search(r"^[a-zA-Z ]*$", slot_value)):
            return {"name_qFH0i9NeQv": slot_value}
        else:
            dispatcher.utter_message(text="Need your name to move forward.")
            return {"name_qFH0i9NeQv": None, "name_invalid_qFH0i9NeQv": 'True'}

    def validate_number_qFH0i9NeQv(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker,
                                   domain: Dict[Text, Any], ) -> Dict[Text, Any]:
        slot_value = slot_value.replace("qFH0i9NeQv_", "")
        if (re.search(r"^[6789]\d{9}$", slot_value)):
            return {"number_qFH0i9NeQv": slot_value}
        else:
            dispatcher.utter_message(
                text="Sorry, you've entered incorrect mobile number.")
            return {"number_qFH0i9NeQv": None, "number_invalid_qFH0i9NeQv": 'True'}

    def validate_email_qFH0i9NeQv(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker,
                                  domain: DomainDict, ) -> Dict[Text, Any]:
        slot_value = slot_value.replace("qFH0i9NeQv_", "")
        if (re.search(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", slot_value)):
            return {"email_qFH0i9NeQv": slot_value}
        else:
            dispatcher.utter_message(
                text="Sorry, you've entered incorrect email id.")
            return {"email_qFH0i9NeQv": None, "email_invalid_qFH0i9NeQv": 'True'}


class ActionAskNameqFH0i9NeQv(Action):
    def name(self) -> Text:
        return "action_ask_name_qFH0i9NeQv"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_slot("name_invalid_qFH0i9NeQv") == 'True':
            dispatcher.utter_message(text='Please enter your name.')
            return [SlotSet("name_invalid_qFH0i9NeQv", 'False')]
        else:
            dispatcher.utter_message(text='May I have your name?')
        return []


class ActionAskEmailqFH0i9NeQv(Action):
    def name(self) -> Text:
        return "action_ask_email_qFH0i9NeQv"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_slot("email_invalid_qFH0i9NeQv") == 'True':
            dispatcher.utter_message(text='Please enter your email id.')
            return [SlotSet("email_invalid_qFH0i9NeQv", 'False')]
        else:
            dispatcher.utter_message(text='May I have your Email Id?')
        return []


class ActionAskNumberqFH0i9NeQv(Action):
    def name(self) -> Text:
        return "action_ask_number_qFH0i9NeQv"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_slot("number_invalid_qFH0i9NeQv") == 'True':
            dispatcher.utter_message(text='Please enter your mobile number.')
            return [SlotSet("number_invalid_qFH0i9NeQv", 'False')]
        else:
            dispatcher.utter_message(text='May I have your Mobile number?')
        return []


class ActionWelcomeqFH0i9NeQv(Action):
    def name(self) -> Text:
        return "action_welcome_qFH0i9NeQv"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Welcome to Brundavan hospitals, The best gynec and pediatric care hospital in Secunderabad.")
        dispatcher.utter_message(
            text="Our treatments & pregnancy care packages are personalized to each patient fulfilling their needs.")
        dispatcher.utter_message(
            text="Our staff is trained to handle obstetric patients with love & care that they deserve.")
        dispatcher.utter_message(
            template="utter_qFH0i9NeQv_get_started")

        return [AllSlotsReset()]


def brundavanday():
    today = datetime.datetime.now(pytz.timezone(
        'Asia/Kolkata')).isoformat('T', 'seconds')
    one = datetime.datetime.strptime(
        today, '%Y-%m-%dT%H:%M:%S%z') + timedelta(days=1)
    two = datetime.datetime.strptime(
        today, '%Y-%m-%dT%H:%M:%S%z') + timedelta(days=2)
    three = datetime.datetime.strptime(
        today, '%Y-%m-%dT%H:%M:%S%z') + timedelta(days=3)
    four = datetime.datetime.strptime(
        today, '%Y-%m-%dT%H:%M:%S%z') + timedelta(days=4)

    buttons = []
    buttons.append({"title": one.strftime("%b-%d-%Y"),
                    "payload": "{0}".format(one)})
    buttons.append({"title": two.strftime("%b-%d-%Y"),
                    "payload": "{0}".format(two)})
    buttons.append({"title": three.strftime("%b-%d-%Y"),
                    "payload": "{0}".format(three)})
    buttons.append({"title": four.strftime("%b-%d-%Y"),
                    "payload": "{0}".format(four)})

    return buttons


class ActionAppointmentTimeqFH0i9NeQv(Action):
    def name(self):
        return "action_appointment_time_qFH0i9NeQv"

    def run(self, dispatcher, tracker, domain):
        buttons = brundavanday()
        department = tracker.latest_message.get('text')
        department = department.replace("qFH0i9NeQv_", "")
        dispatcher.utter_message(
            text="When would you like to visit us for consultation?", buttons=buttons)
        return [SlotSet("department_qFH0i9NeQv", department)]


class ActionAppointmentSubmitqFH0i9NeQv(Action):
    def name(self) -> Text:
        return "action_appointment_submit_qFH0i9NeQv"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Thank you, your appointment request has been received. Our team will call you to confirm your slot.")

        dispatcher.utter_message(
            text=" You can also call us at 9121612553."
        )

        return [AllSlotsReset()]


class ActionDoctorSpecialityCarouselqFH0i9NeQv(Action):
    def name(self) -> Text:
        return "action_doctor_speciality_carousel_qFH0i9NeQv"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        test_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Gynecology",
                        # "subtitle": "MS, FICS, FIAGES 23 Years Of Experience",
                        "image_url": "https://i.ibb.co/rd1Swqd/images-q-tbn-ANd9-Gc-RFo4k0-XLZJ6-Tw8w-JYCY52p0-Mdg-BG7-Anzin-Jw-usqp-CAU.jpg",
                        "buttons": [
                            {
                                "title": "Read more",
                                "url": "https://brundavanhospitals.in/our-services/gynecology/",
                                "type": "web_url"
                            },
                            {
                                "title": "Book an appointment",
                                "type": "postback",
                                "payload": "/qFH0i9NeQv_doctor_book"

                            }
                        ]
                    },
                    {
                        "title": "Pediatric",
                        # "subtitle": "MBBS, FICS 13 Years Of Experience",
                        "image_url": "https://i.ibb.co/vqt8nBH/images-q-tbn-ANd9-Gc-Tztehd-Ge-WYgbq6-NR1-Q13vkf-HMp4h-ZHQx6-Low-usqp-CAU.jpg",
                        "buttons": [
                            {
                                "title": "Read more",
                                "url": "https://brundavanhospitals.in/pediatric-services/childhood-asthma-and-allergies/",
                                "type": "web_url"
                            },
                            {
                                "title": "Book an appointment",
                                "type": "postback",
                                "payload": "/qFH0i9NeQv_doctor_book"

                            }
                        ]
                    }
                ]
            }
        }

        dispatcher.utter_message(attachment=test_carousel)
        return []


class ActionSpecialityCarouselqFH0i9NeQv(Action):
    def name(self) -> Text:
        return "action_speciality_carousel_qFH0i9NeQv"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        test_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Dr.Karthik",
                        "subtitle": "MBBS, MD Paediatrics, 14+ Years Of Experience",
                        "image_url": "https://brundavanhospitals.in/wp-content/uploads/2020/08/3-7.jpg",
                        "buttons": [
                            {
                                "title": "Read more",
                                "url": "https://brundavanhospitals.in/doctors/dr-karthik/",
                                "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Dr.Gitanjali",
                        "subtitle": "MBBS, DNB OBG, 10+ Years Of Experience",
                        "image_url": "https://brundavanhospitals.in/wp-content/uploads/2020/08/Doctor-image.jpg",
                        "buttons": [
                            {
                                "title": "Read more",
                                "url": "https://brundavanhospitals.in/doctors/dr-gitanjali/",
                                "type": "web_url"
                            }
                        ]
                    }
                ]
            }
        }

        dispatcher.utter_message(attachment=test_carousel)
        return []


class ActionSelectCarouselqFH0i9NeQv(Action):
    def name(self) -> Text:
        return "action_select_carousel_qFH0i9NeQv"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        date = tracker.latest_message.get('text')
        date = date.replace("qFH0i9NeQv_", "")
        date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S%z')
        test_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Dr.Karthik",
                        "subtitle": "MBBS, MD Paediatrics, 14+ Years Of Experience",
                        "image_url": "https://brundavanhospitals.in/wp-content/uploads/2020/08/3-7.jpg",
                        "buttons": [
                            {
                                "title": "Confirm booking",
                                "type": "postback",
                                "payload": "qFH0i9NeQv_Dr. qFH0i9NeQv_Karthik"

                            },
                            {
                                "title": "Know your doctor",
                                "url": "https://brundavanhospitals.in/doctors/dr-karthik/",
                                "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Dr.Gitanjali",
                        "subtitle": "MBBS, DNB OBG, 10+ Years Of Experience",
                        "image_url": "https://brundavanhospitals.in/wp-content/uploads/2020/08/Doctor-image.jpg",
                        "buttons": [
                            {
                                "title": "Confirm booking",
                                "type": "postback",
                                "payload": "qFH0i9NeQv_Dr. qFH0i9NeQv_Gitanjali"

                            },
                            {
                                "title": "Know your doctor",
                                "url": "https://brundavanhospitals.in/doctors/dr-gitanjali/",
                                "type": "web_url"
                            }
                        ]
                    }
                ]
            }
        }
        dispatcher.utter_message(
            text="Dr. Karthik & Dr. Gitanjali are available on {0}".format(date.date()))
        dispatcher.utter_message(attachment=test_carousel)
        return [SlotSet("date_qFH0i9NeQv", str(date.date()))]


# skipprz  JnLRTjwfPT_
class ActionGetStartedJnLRTjwfPT(Action):
    def name(self) -> Text:
        return "action_get_started_JnLRTjwfPT"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text='Hey there, welcome to Skipprz - India’s largest business solutions platform.')
        dispatcher.utter_message(
            template="utter_JnLRTjwfPT_get_started")
        return []


class ActionCloseJnLRTjwfPT(Action):
    def name(self) -> Text:
        return "action_close_JnLRTjwfPT"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text='Cool, Let me know if you would need any assistance. Happy to help!')
        dispatcher.utter_message(
            text='Just say "Hi" or Hello" to start our conversation.')
        return []


class ActionFundingJnLRTjwfPT(Action):
    def name(self) -> Text:
        return "action_funding_JnLRTjwfPT"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text='Raising funds has never been easier with Skipprz. Our network and domain expertise helps you raise funds quickly and efficiently.')
        dispatcher.utter_message(
            text='We are sector agnostic, all we look for is for startups with MVP. Our funding rounds range from $0.2mn upto $50mn. Are you the one? To know more about our funding process, [register](https://www.skipprz.com/funding-form) today.')
        dispatcher.utter_message(
            template="utter_JnLRTjwfPT_anythingelse")
        return []


class ActionCoFounderSearchJnLRTjwfPT(Action):
    def name(self) -> Text:
        return "action_co_founder_search_JnLRTjwfPT"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text='We intend to build a sustainable ecosystem for the startup community. Matching the right people with the right talent is what our platform enables you to do.')
        dispatcher.utter_message(
            text='Register today and find the right match for you. ')

        return []


class ActionMentorshipJnLRTjwfPT(Action):
    def name(self) -> Text:
        return "action_mentorship_JnLRTjwfPT"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text='Everyone needs mentors, we too have many. Our connections with industry experts help you cross the hurdle with the right guidance and motivation required to be successful.')
        dispatcher.utter_message(
            template='utter_JnLRTjwfPT_mentorship')

        return []


class ActionCareersJnLRTjwfPT(Action):
    def name(self) -> Text:
        return "action_careers_JnLRTjwfPT"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text='We are looking for bright young people to join our team. Below are the current job opportunities with Skipprz.')
        dispatcher.utter_message(
            text='Senior sales manager [Apply](https://www.linkedin.com/jobs/view/3011946070/?refId=RjLjx0433ffTIWVK6%2BVOjQ%3D%3D)')
        dispatcher.utter_message(
            template="utter_JnLRTjwfPT_anythingelse")
        return []


class ActionBuyerCommodityJnLRTjwfPT(Action):
    def name(self) -> Text:
        return "action_buyer_commodity_JnLRTjwfPT"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if (tracker.get_slot("number_counter_JnLRTjwfPT") > 1):
            dispatcher.utter_message(
                text='Here’s the link to our [registration form](https://www.skipprz.com/commodity-buyer). Request you to fill in the details and submit, our sales team will reach out to you shortly.')
        else:
            dispatcher.utter_message(
                text='Thank you. Here’s the link to our [registration form](https://www.skipprz.com/commodity-buyer). Request you to fill in the details and submit, our sales team will reach out to you shortly.')
        dispatcher.utter_message(
            template="utter_JnLRTjwfPT_anythingelse")
        return []


class ActionSellerCommodityJnLRTjwfPT(Action):
    def name(self) -> Text:
        return "action_seller_commodity_JnLRTjwfPT"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if (tracker.get_slot("number_counter_JnLRTjwfPT") > 1):
            dispatcher.utter_message(
                text='Here’s the link to our [registration form](https://www.skipprz.com/commodity-seller). Request you to fill in the details and submit, our sales team will reach out to you shortly.')
        else:
            dispatcher.utter_message(
                text='Thank you. Here’s the link to our [registration form](https://www.skipprz.com/commodity-seller). Request you to fill in the details and submit, our sales team will reach out to you shortly.')
        dispatcher.utter_message(
            template="utter_JnLRTjwfPT_anythingelse")
        return []


class ActionPartnershipJnLRTjwfPT(Action):
    def name(self) -> Text:
        return "action_partnership_JnLRTjwfPT"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text='We at Skipprz are always looking for opportunities and businesses to partner with. ')

        dispatcher.utter_message(
            image='https://i.giphy.com/media/oMByNTQjsXfVg1zY7X/200w.webp')
        dispatcher.utter_message(
            text='If you think we can collaborate and contribute towards each others growth, hit us with an email to hello@skipprz.com')
        dispatcher.utter_message(
            template="utter_JnLRTjwfPT_anythingelse")
        return []


class ActionAskNameJnLRTjwfPT(Action):
    def name(self) -> Text:
        return "action_ask_name_JnLRTjwfPT"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_slot("name_invalid_JnLRTjwfPT") == 'True':
            dispatcher.utter_message(text='Please enter your name.')
            return [SlotSet("name_invalid_JnLRTjwfPT", 'False')]
        else:
            dispatcher.utter_message(
                text='Before we go ahead, what do I call you?')
        return []


class ValidateNameFormJnLRTjwfPT(FormValidationAction):
    def name(self) -> Text:
        return "name_form_JnLRTjwfPT"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["name_JnLRTjwfPT"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {"name_JnLRTjwfPT": [self.from_text()]}


class ValidateNameJnLRTjwfPT(FormValidationAction):
    def name(self) -> Text:
        return "validate_name_form_JnLRTjwfPT"

    def validate_name_JnLRTjwfPT(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker,
                                 domain: Dict[Text, Any], ) -> Dict[Text, Any]:

        a = tracker.get_slot('name_invalid_JnLRTjwfPT')
        slot_value = slot_value.replace("JnLRTjwfPT_", "")
        if a != 'True':
            if (re.search(r"^[a-zA-Z ]*$", slot_value)):
                headers = {'Content-Type': 'application/json'}
                url = 'https://api.mauvechat.io/userLeads/'
                channel = tracker.get_latest_input_channel()
                if channel != 'socketio':
                    channel = 'Facebook'
                else:
                    channel = 'Website'
                data = {"Name": slot_value, "source": channel, "Company_id": "10", "Bot_id": "JnLRTjwfPT_",
                        "Session_id": tracker.sender_id}
                response = requests.post(
                    url, data=json.dumps(data), headers=headers)
                return {"name_JnLRTjwfPT": slot_value, "name_counter_JnLRTjwfPT": 1, "name_invalid_JnLRTjwfPT": "True"}
            else:
                dispatcher.utter_message(
                    text="Need your name to move forward.")
                return {"name_JnLRTjwfPT": None}
        return {"name_counter_JnLRTjwfPT": tracker.get_slot('name_counter_JnLRTjwfPT') + 1}


class ActionAskNumberJnLRTjwfPT(Action):
    def name(self) -> Text:
        return "action_ask_number_JnLRTjwfPT"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_slot("number_invalid_JnLRTjwfPT") == 'True':
            dispatcher.utter_message(text='Please enter your mobile number.')
            return [SlotSet("number_invalid_JnLRTjwfPT", 'False')]
        else:
            dispatcher.utter_message(text='May I have your Mobile number?')
        return []


class ValidateNumberFormJnLRTjwfPT(FormValidationAction):
    def name(self) -> Text:
        return "number_form_JnLRTjwfPT"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["number_JnLRTjwfPT"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {"number_JnLRTjwfPT": [self.from_text()]}


class ValidateNumberJnLRTjwfPT(FormValidationAction):
    def name(self) -> Text:
        return "validate_number_form_JnLRTjwfPT"

    def validate_number_JnLRTjwfPT(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker,
                                   domain: Dict[Text, Any], ) -> Dict[Text, Any]:
        a = tracker.get_slot('number_invalid_JnLRTjwfPT')
        slot_value = slot_value.replace("JnLRTjwfPT_", "")
        if a != 'True':
            if (re.search(r"^[6789]\d{9}$", slot_value)):

                headers = {'Content-Type': 'application/json'}

                url = 'https://api.mauvechat.io/userLeads/'
                channel = tracker.get_latest_input_channel()
                if channel != 'socketio':
                    channel = 'Facebook'
                else:
                    channel = 'Website'

                data = {"Mobile": slot_value, "Company_id": "10", "Bot_id": "JnLRTjwfPT_", "Session_id": tracker.sender_id,
                        "source": channel}
                response = requests.post(
                    url, data=json.dumps(data), headers=headers)
                print(response)
                return {"number_JnLRTjwfPT": slot_value, "number_counter_JnLRTjwfPT": 1, "number_invalid_JnLRTjwfPT": 'True'}
            else:
                dispatcher.utter_message(
                    text="Sorry, you've entered incorrect mobile number.")
                return {"number_JnLRTjwfPT": None}
        return {"number_counter_JnLRTjwfPT": tracker.get_slot('number_counter_JnLRTjwfPT') + 1}


class ActionSubmitJnLRTjwfPT(Action):
    def name(self) -> Text:
        return "action_submit_JnLRTjwfPT"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if ((tracker.get_slot("name_counter_JnLRTjwfPT") > 1) and (tracker.get_slot("number_counter_JnLRTjwfPT") > 1)):
            dispatcher.utter_message(
                text='We have your details already.Our sales team will get in touch with you within 24 hrs.')
        else:
            dispatcher.utter_message(
                text='Great, our sales team will reach out to you shortly. You can check out service offerings [here](https://www.skipprz.com/vendor-form).')
        dispatcher.utter_message(
            template="utter_JnLRTjwfPT_anythingelse")
        return []


class ActionMentorSubmitJnLRTjwfPT(Action):
    def name(self) -> Text:
        return "action_mentor_submit_JnLRTjwfPT"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if ((tracker.get_slot("name_counter_JnLRTjwfPT") > 1) and (tracker.get_slot("number_counter_JnLRTjwfPT") > 1)):
            dispatcher.utter_message(
                text='We have your details already.Our sales team will get in touch with you within 24 hrs.')
        else:
            dispatcher.utter_message(
                text='Great, our sales team will reach out to you shortly.')
        dispatcher.utter_message(
            template="utter_JnLRTjwfPT_anythingelse")
        return []


# Mauvetix Solutions oOwiLmXXsD
class ValidateNameFormoOwiLmXXsD(FormValidationAction):
    def name(self) -> Text:
        return "name_form_oOwiLmXXsD"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["name_oOwiLmXXsD"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {"name_oOwiLmXXsD": [self.from_text()]}


class ValidateEmailFormoOwiLmXXsD(FormValidationAction):
    def name(self) -> Text:
        return "email_form_oOwiLmXXsD"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["email_oOwiLmXXsD"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {"email_oOwiLmXXsD": [self.from_text()]}


class ValidateNumberFormoOwiLmXXsD(FormValidationAction):
    def name(self) -> Text:
        return "number_form_oOwiLmXXsD"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["number_oOwiLmXXsD"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {"number_oOwiLmXXsD": [self.from_text()]}


class ValidateNameoOwiLmXXsD(FormValidationAction):
    def name(self) -> Text:
        return "validate_name_form_oOwiLmXXsD"

    def validate_name_oOwiLmXXsD(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker,
                                 domain: Dict[Text, Any], ) -> Dict[Text, Any]:
        a = tracker.get_slot('name_bool_oOwiLmXXsD')
        slot_value = slot_value.replace("oOwiLmXXsD_", "")
        if a != 'True':
            if (re.search(r"^[a-zA-Z ]*$", slot_value)):
                headers = {'Content-Type': 'application/json'}
                url = 'https://api.mauvechat.io/userLeads/'
                channel = tracker.get_latest_input_channel()
                if channel != 'socketio':
                    channel = 'Facebook'
                else:
                    channel = 'Website'
                data = {"Name": slot_value, "source": channel, "Company_id": "1", "Bot_id": "oOwiLmXXsD_",
                        "Session_id": tracker.sender_id}
                response = requests.post(
                    url, data=json.dumps(data), headers=headers)
                return {"name_oOwiLmXXsD": slot_value, "name_bool_oOwiLmXXsD": 'True'}
            else:
                dispatcher.utter_message(
                    text="Need your name to move forward.")
                return {"name_oOwiLmXXsD": None, "name_invalid_oOwiLmXXsD": 'True'}


class ValidateEmailoOwiLmXXsD(FormValidationAction):
    def name(self) -> Text:
        return "validate_email_form_oOwiLmXXsD"

    def validate_email_oOwiLmXXsD(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker,
                                  domain: DomainDict, ) -> Dict[Text, Any]:
        a = tracker.get_slot('email_bool_oOwiLmXXsD')
        slot_value = slot_value.replace("oOwiLmXXsD_", "")
        if a != 'True':
            if (re.search(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", slot_value)):
                headers = {'Content-Type': 'application/json'}
                url = 'https://api.mauvechat.io/userLeads/'
                channel = tracker.get_latest_input_channel()
                if channel != 'socketio':
                    channel = 'Facebook'
                else:
                    channel = 'Website'

                data = {"Email": slot_value, "Company_id": "1", "Bot_id": "oOwiLmXXsD_", "Session_id": tracker.sender_id,
                        "source": channel}
                response = requests.post(
                    url, data=json.dumps(data), headers=headers)
                return {"email_oOwiLmXXsD": slot_value, "email_bool_oOwiLmXXsD": 'True'}
            else:
                dispatcher.utter_message(
                    text="Sorry, you've entered incorrect email id.")
                return {"email_oOwiLmXXsD": None, "email_invalid_oOwiLmXXsD": 'True'}


class ValidateNumberoOwiLmXXsD(FormValidationAction):
    def name(self) -> Text:
        return "validate_number_form_oOwiLmXXsD"

    def validate_number_oOwiLmXXsD(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker,
                                   domain: Dict[Text, Any], ) -> Dict[Text, Any]:
        a = tracker.get_slot('number_bool_oOwiLmXXsD')
        slot_value = slot_value.replace("oOwiLmXXsD_", "")
        if a != 'True':
            if (re.search(r"^[6789]\d{9}$", slot_value)):

                headers = {'Content-Type': 'application/json'}
                url = 'https://api.mauvechat.io/userLeads/'
                channel = tracker.get_latest_input_channel()
                if channel != 'socketio':
                    channel = 'Facebook'
                else:
                    channel = 'Website'

                data = {"Mobile": slot_value, "Company_id": "1", "Bot_id": "oOwiLmXXsD_", "Session_id": tracker.sender_id,
                        "source": channel}
                response = requests.post(
                    url, data=json.dumps(data), headers=headers)
                return {"number_oOwiLmXXsD": slot_value, "number_bool_oOwiLmXXsD": 'True', "business_oOwiLmXXsD": 1}
            else:

                dispatcher.utter_message(
                    text="Sorry, you've entered incorrect mobile number.")
                return {"number_oOwiLmXXsD": None, "number_invalid_oOwiLmXXsD": 'True'}
        return {"business_oOwiLmXXsD": tracker.get_slot('business_oOwiLmXXsD') + 1}


class ActionAskNameoOwiLmXXsD(Action):
    def name(self) -> Text:
        return "action_ask_name_oOwiLmXXsD"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_slot("name_invalid_oOwiLmXXsD") == 'True':
            dispatcher.utter_message(text='Please enter your name')
            return[SlotSet("name_invalid_oOwiLmXXsD", 'False')]

        else:
            dispatcher.utter_message(text='May I know your name?')
        return []


class ActionAskEmailoOwiLmXXsD(Action):
    def name(self) -> Text:
        return "action_ask_email_oOwiLmXXsD"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_slot("email_invalid_oOwiLmXXsD") == 'True':
            dispatcher.utter_message(text='Please enter your email id')
            return[SlotSet("email_invalid_oOwiLmXXsD", 'False')]

        else:
            dispatcher.utter_message(text='May I know your email id?')
        return []


class ActionAskNumberoOwiLmXXsD(Action):
    def name(self) -> Text:
        return "action_ask_number_oOwiLmXXsD"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_slot("number_invalid_oOwiLmXXsD") == 'True':
            dispatcher.utter_message(text='Please enter your mobile number')
            return[SlotSet("number_invalid_oOwiLmXXsD", 'False')]

        else:
            dispatcher.utter_message(text='May I know your mobile number?')
        return []


class ActionGreetoOwiLmXXsD(Action):
    def name(self) -> Text:
        return "action_greet_oOwiLmXXsD"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text='Hey there, welcome to Mauvetix Solutions- India’s leading business solutions platform enabling right tools for their digital transformation journey.')
        dispatcher.utter_message(
            text="We help our partners Attract, Engage and Delight customers through our suite of services.")
        dispatcher.utter_message(template="utter_oOwiLmXXsD_services")
        return []


class ActionChatbotoOwiLmXXsD(Action):
    def name(self) -> Text:
        return "action_chatbot_oOwiLmXXsD"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="More than 70% of your customer queries are repetitive, automate your customer interactions with AI driven conversation automation platform - Mauvechat.")
        dispatcher.utter_message(
            text="Our chabots support the following platforms with quick integration with your existing CRM. \n \n - WhatsApp \n \n - Website \n \n - Facebook \n \n - Instagram \n \n - Mobile Apps")
        dispatcher.utter_message(template="utter_oOwiLmXXsD_chatbots")
        return []


class ActionDigitalMarketingoOwiLmXXsD(Action):
    def name(self) -> Text:
        return "action_digital_marketing_oOwiLmXXsD"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text='Our skilled team with an ROI focussed approach has helped 100+ customers over the last 4 years to acquire, engage and retain customers effectively.')
        dispatcher.utter_message(
            text="Our services: \n \n - Lead Generation \n \n - Social Media Marketing \n \n - Pay per click Marketing \n \n - SEO \n \n - Branding \n \n - Email & Mobile Marketing")
        dispatcher.utter_message(template="utter_oOwiLmXXsD_digital")
        return []


class ActionWebsiteDevelopmentoOwiLmXXsD(Action):
    def name(self) -> Text:
        return "action_website_development_oOwiLmXXsD"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text='We take pride in developing and delivering wholesome solutions to our clients with the best technology at great prices.')
        dispatcher.utter_message(
            text="What you can expect is \n \n - Best in technology \n \n - Scalable and secure websites \n \n - Responsive for omnichannel experience \n \n - Complementary hosting and storage \n \n - Life long maintenance")
        dispatcher.utter_message(template="utter_oOwiLmXXsD_website")
        return []


class ActionRecruitmentoOwiLmXXsD(Action):
    def name(self) -> Text:
        return "action_recruitment_oOwiLmXXsD"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text='Mauvetix team brings in diversified skills which helps us to identify, screen and process the right candidate for the job.')
        dispatcher.utter_message(
            text="If you are looking to partner with us, drop us an email at hr@mauvetix.com and our team will reach out to you 🤘.")

        return []


class ActionSubmitoOwiLmXXsD(Action):
    def name(self) -> Text:
        return "action_submit_oOwiLmXXsD"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if (tracker.get_slot("business_oOwiLmXXsD") > 1):
            dispatcher.utter_message(
                text="We have your details already, one of our sales representative will call you in 24hrs.")
        else:
            dispatcher.utter_message(
                text="Thank you for the details, one of our sales representative will call you in 24hrs.")

        dispatcher.utter_message(template="utter_oOwiLmXXsD_anythingelse")

        return []

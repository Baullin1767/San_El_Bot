import requests
import config

body = {'fields': {'TITLE': 'Test',
                   'NAME': 'NAME',
                   'SECOND_NAME': 'SECOND_NAME',
                   'LAST_NAME': 'LAST_NAME',
                   'PHONE': [ { "VALUE": "555888", "VALUE_TYPE": "WORK" } ],
                   "CURRENCY_ID": "RUB",
                   "OPPORTUNITY": 1200,
                   "COMMENTS":'COMMENTS'}
}




def set_lead(body: dict):
    requests.post(config.WEBHOOK + 'crm.deal.add.json', json=body)

if __name__ == '__main__':
    set_lead(body)
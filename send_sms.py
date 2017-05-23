import sys
import os
import requests

msg = input("Enter the message: ")
number = input("Enter the phone number: ")

req = requests.post('https://textbelt.com/text', {
  'phone': number,
  'message': msg,
  'key': 'textbelt',
})

if req.json['success']:
	print('Message sent!')
else:
	print('Error')
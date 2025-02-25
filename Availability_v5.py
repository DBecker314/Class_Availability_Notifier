from bs4 import BeautifulSoup
from twilio.rest import Client
import requests
import time


account_sid ='twilio account sid'
auth_token ='twilio account token'
twilio_number = '+**********'
my_number = '+**********'
client_number = '+**********'

client = Client(account_sid, auth_token)

seats_rem1 = 0
seats_rem2 = 0
seats_rem3 = 0
seats_rem4 = 0

i = 1
while i == 1:
    time.sleep(4)
    page1 = requests.get(
        "https://usfonline.admin.usf.edu/pls/prod/bwckschd.p_disp_detail_sched?term_in=202501&crn_in=16064")
    soup1 = BeautifulSoup(page1.text, "html.parser")
    page2 = requests.get(
        "https://usfonline.admin.usf.edu/pls/prod/bwckschd.p_disp_detail_sched?term_in=202501&crn_in=16065")
    soup2 = BeautifulSoup(page2.text, "html.parser")
    page3 = requests.get(
        "https://usfonline.admin.usf.edu/pls/prod/bwckschd.p_disp_detail_sched?term_in=202501&crn_in=17862")
    soup3 = BeautifulSoup(page3.text, "html.parser")
    page4 = requests.get(
        "https://usfonline.admin.usf.edu/pls/prod/bwckschd.p_disp_detail_sched?term_in=202501&crn_in=11413")
    soup4 = BeautifulSoup(page4.text, "html.parser")

    table1 = soup1.find_all("table", attrs={"summary": "This layout table is used to present the seating numbers."})
    table2 = soup2.find_all("table", attrs={"summary": "This layout table is used to present the seating numbers."})
    table3 = soup3.find_all("table", attrs={"summary": "This layout table is used to present the seating numbers."})
    table4 = soup4.find_all("table", attrs={"summary": "This layout table is used to present the seating numbers."})

    for row1 in table1:
        n1 = 0
    if n1 > seats_rem1:
        good_message1 = client.messages.create(
            body='A seat in class 16064 has opened up!',
            from_=twilio_number,
            to=client_number
        )
        seats_rem1 = n1
    elif n1 < seats_rem1:
        if n1 == 0:
            worst_message1 = client.messages.create(
                body='A seat in class 16064 has been taken, the class is now closed.',
                from_=twilio_number,
                to=client_number
            )
        else:
            bad_message1 = client.messages.create(
                body='A seat in class 16064 has been taken, but the class is still open!',
                from_=twilio_number,
                to=client_number
            )
        seats_rem1 = n1

    for row2 in table2:
        n2 = int(row2.text[68])
    if n2 > seats_rem2:
        good_message2 = client.messages.create(
            body='A seat in class 16065 has opened up!',
            from_=twilio_number,
            to=client_number
        )
        seats_rem2 = n2
    elif n2 < seats_rem2:
        if n2 == 0:
            worst_message2 = client.messages.create(
                body='A seat in class 16065 has been taken, the class is now closed.',
                from_=twilio_number,
                to=client_number
            )
        else:
            bad_message2 = client.messages.create(
                body='A seat in class 16065 has been taken, but the class is still open!',
                from_=twilio_number,
                to=client_number
            )
        seats_rem2 = n2

    for row3 in table3:
        n3 = int(row3.text[68])
    if n3 > seats_rem3:
        good_message3 = client.messages.create(
            body='A seat in class 17862 has opened up!',
            from_=twilio_number,
            to=client_number
        )
        seats_rem3 = n3
    elif n3 < seats_rem3:
        if n3 == 0:
            worst_message3 = client.messages.create(
                body='A seat in class 17862 has been taken, the class is now closed.',
                from_=twilio_number,
                to=client_number
            )
        else:
            bad_message3 = client.messages.create(
                body='A seat in class 17862 has been taken, but the class is still open!',
                from_=twilio_number,
                to=client_number
            )
        seats_rem3 = n3

    for row4 in table4:
        n4 = int(row4.text[68])
    if n4 > seats_rem4:
        good_message4 = client.messages.create(
            body='A seat in class 11413 has opened up!',
            from_=twilio_number,
            to=client_number
        )
        seats_rem4 = n4
    elif n4 < seats_rem4:
        if n4 == 0:
            worst_message4 = client.messages.create(
                body='A seat in class 11413 has been taken, the class is now closed.',
                from_=twilio_number,
                to=client_number
            )
        else:
            bad_message4 = client.messages.create(
                body='A seat in class 11413 has been taken, but the class is still open!',
                from_=twilio_number,
                to=client_number
            )
        seats_rem4 = n4


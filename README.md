# Class Availability Project

### Overview

This is my first ever experience with python.  The goal of this project was to scrape class availability data from the University of South Florida class timetable in order to send updates on the availability of certain classes.

### Problem

This project started as an experiment to help my girlfriend get into a previously full statistics class.  Having no luck with the coursicle app due to a notification delay, she enlisted my help to solve the problem.

### Deliverables

The only deliverable for this project was a notification when a seat opened up in certain classes.
This notification had to be:
- Immediate (within a few seconds)
- Accurate
- Flexible (compatible with any USF class)

### Process

I broke this project down into three parts:
1. Scan the timetable
2. Detect availability updates
3. Send a notification

I started by trying to use selenium to login to the USF student portal so that I could look at the timetable.  This ended up being unnecessary since I was able to find urls for each course request number. Once I was able to access the CRNs, I used Beautifulsoup4 to scan the open seats section of each class, then using twilio I was able to send text message updates to my girlfriend.

### Results

I started running this program on the first day of drop-add week, and my girlfriend was able to get her class the same day as soon as the first person dropped.

# golfhub

Have you ever showed up to your tee time only to be paired with two 80 year old men, both named Jim? If you haven't, take my word, it's not fun. Golfhub is a web application that takes the guess work out of finding a 4 man team to golf with. Golfhub allows golfers to find golf groups before they even hit the course. This will prevent younger golfers from getting paired with people they simply can't connect with... aka boomers.

Django, Python, PostgreSQL

Installation Steps:
• clone down repository
• make sure you have python installed already
• install pip -> python get-pip.py
• create an environment ->
• install django in your environment -> pipenv install Django
• install dependencies -> pipenv install -r requirements.txt

User Stories:
- As a user I want to create an account
- As a user I want to log in
- As a user I want to create a golf group, define the scheduled tee time and golf course, have the ability to invite friends to the group, and have randoms request to join my group
- As a user I want to join other’s golf groups
- As a user I want to have a profile page
- As a user I want to edit my profile page
- As a user I want to view other people’s profile pages
- As a user I don’t want to see golf groups that are in the past
- As a user I want to be able to delete my golf group
- As a user I want to be able to leave a golf group I’m in

Wireframe:
<img width="1019" alt="Screen Shot 2021-11-20 at 10 49 09 AM" src="https://user-images.githubusercontent.com/1546543/142737821-2b232308-b7b0-4dd3-a357-a18559ca5a4f.png">

ERD:

<img width="465" alt="Screen_Shot_2021-11-06_at_4 26 19_PM" src="https://user-images.githubusercontent.com/1546543/142737981-af8b4c4a-97f2-4fc4-b1f6-b79da0abd737.png">

Unsolved Problems:
• The hardest thing for me was deploying on Heroku. Next time I attempt it, I'm defintely gonna take it slower and really read what i'm doing. Because I was in a rush, I pretty much followed a ton of different guides at once, downloaded everything I saw, and put myself in a whole so deep I didn't know which direction to go.
• I wasn't able to create a lot of important features simply because I managed my time poorly (spent too much time designing). Some of these features include: Golf group filters, golf group sort, search, friends list.

What's next?
• Add filters to group list
• Add functionality to search bar
• Add ability to add and remove friends
• Invite friends to your group
• Notifications
• Responsive design

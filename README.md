# Questioner
This is an application that crowd-sources question suggestions for meet-ups.

# Badges
[![Build Status](https://travis-ci.org/Gichia/questioner-v3.svg?branch=develop)](https://travis-ci.org/Gichia/questioner-v3)
[![Coverage Status](https://coveralls.io/repos/github/Gichia/questioner-v3/badge.svg?branch=develop)](https://coveralls.io/github/Gichia/questioner-v3?branch=develop)

# Summary
Questioner is an online platform that allows users to crowd-source interesting question suggestions for meetups posted on the site. The Admin creates and posts meetups, and then registered users can post questions they think can be interesting or beneficial to be discussed on a particular meetup.

The platform allows the meetup organizer to prioritize the questions to be aked or tackled during a meetup that he/she posted by going through the suggested question posted by users. A user is able vote on the asked questions suggested by other users, and as they do so, the questions bubble to the top or bottom of the log.

# Getting started
--------------------
1. Clone this repository
```
    https://github.com/Gichia/questioner-v3.git
```

2. Navigate to the cloned repository

# Pre-requisites
----------------------
1. Python 3
2. Flask
3. Postman
4. Git

# Installation
---------------------------------
1. Create a virtual environment
```
    virtualenv venv
```

2. Activate the virtual environment
```
    source venv/scripts/activate
```

3. Switch to 'develop' branch on git
```
    git checkout develop
```

5. Install requirements
```
    pip install -r requirements.txt
```

# Run the application
---------------------------------
```
    python run.py
```

### When you run this application, you can test the following api endpoints using postman
-----------------------------------------------

**Unrestricted endpoints**

| Endpoint | Functionality |
----------|---------------
GET /index | View all questions and answers
POST /auth/signup | Register a user
POST /auth/login | Login a user

**Restricted endpoints**

Endpoint | Functionality
---------|---------------
GET /questions | Fetch all questions
GET /questions/&lt;question_id&gt; | Fetch a specific question
POST /questions | Post a question
DELETE /questions/&lt;question_id&gt; | Delete a question
POST /questions/&lt;answer/question_id&gt; | Post an answer to a question


# Authors
-----------------------------
**Peter Gichia** -_Work By_-[Gichia](https:/github.com/Gichia)

# License
--------------------------
This project is licensed under the MIT license. See [LICENSE](https://github.com/Gichia/questioner-v3/blob/develop/LICENSE) for details.

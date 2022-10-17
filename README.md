# About the Project

# Project demonstration

Youtube link: https://youtu.be/XfyOGt8Ie6A

# Foreword

“I’m just not good at keeping in touch with people”...

We as human beings are not naturally endowed with the ability to remember and juggle many responsibilities at once. Some people get carried away with work, making their social lives almost non-existent. Some spend all their time expanding their network and advancing their careers, so they forget when is the last time they call their parents or their old friends. Some trap themselves in work and a few demanding relationships, missing out many opportunities to make new meaningful relationships with others. The list goes on …

It is this common experience - with some minor variations in shapes and forms - that motivates my final project. The project is a basic website that allows users to write quick journal entries and keep track of their time spent with others by relationship categories. To avoid putting users into the work mindset, the website only performs two functions: (1) record users’ journal entries from newest to oldest and (2) record users’ time spent on social activities along with some basic data analytics.

For more details about how to run and use the web, continue reading

# How to run the web

This website is created using Python, HTML & CSS , JavaScript, and SQLite on the CS50 IDE platform. The imported packages are: cs50 (import SQL only), os, JSON, Flask and Werkzeug. All files are included in a folder called “project”. To run the web application on CS50 IDE platform, use the following commands in the terminal:
```
$ cd project
$ flask run
```
Then follow the link the server provides to view the web

# How it works

The project is a website called EMoG - which allows users to save their journal entries and track time spent with their relationships. Due to its private nature, all visitors are required to REGISTER with an username and password by clicking “Join EMoG” in the homepage. Newly registered users are then prompted to LOG IN in the /login page.

After logging in, users will enter the /invitation page. Users are prompted “What do you want to do today?” and can click “Start” on either the card “Journaling” or the card “Relationship Tracker”.

If a user clicks the button “Start” on the card “Journal”, she will be directed to the /journal page. This is also equivalent to the “Activity” tab. Here, she is prompted to SUBMIT the subject of the entry, date and time, and a text box. The text box is designed to be relatively small, creating incentives for users to submit short texts. Mindful of the fact that users who would like to use the website are people who do not have time to journal, the intention behind the design for the journal entry is for users to make short updates like the ones usually made on Facebook or Twitter.

The user is noticed once her journal entry is submitted. She then can click on the “Activity” tab to choose another activity, or to visit the “Entry” tab. On clicking the “Entry” tab, the user is directed to the /history page. Here, she will see all her old posts in the order of the latest to the oldest.

If the user chooses to go back to the “Activity” tab and clicks the “Start” button on the card “Relationship Tracker”, she will be directed to the /relationship page. Here, she is prompted to answer “Whom did you hang out with today?”. She can then submit the form with name of the person she hanged out with, date, hours spent with that person, type of relationship, and activity. Upon clicking “Submit”, she will be directed back to the Activity tab.

To see how her social life dynamics are played out, the user can visit the tab “Tracker”, upon which she will be directed to the /tracker page. Here, she will see two graphs showing (1) the proportion of time she spent on each relationship category and (2) the people she spent most time with (capped at 10 people). Beneath is a table showing all the data she has submitted. She can search for any data input and have the relevant rows appearing upon her search.

One the user wishes to log out, she will clicks “Log Out” button at the top right of the webpage and be redirected to homepage.


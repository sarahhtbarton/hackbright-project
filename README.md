# Spelling Bee Solver
<img src="/static/images/homepage.png">  

***  


# Overview
Spelling Bee Solver is a full stack, single page web app that generates and displays the solutions to a daily NYTimes game called Spelling Bee. The app simply asks users to input the letters for the day's game, then hit submit. What they get in return is a list of all the words for the day’s game, with some extra queues about certain word attributes. Users are also able to give feedback on words, blacklisting them if the Spelling Bee game does not accept them, or whitelisting words to add them to the Solver database.


**Deployed App:** http://54.147.146.226/  
**Demo Video:** https://youtu.be/ebkL7hSwMUs  
**GitHub URL:** https://github.com/sarahhtbarton/hackbright-project  
**Learn more about the developer:** http://linkedin.com/in/SarahHTBarton  

### Technologies
**Languages:** Python, JavaScript (AJAX, JSON), HTML, CSS, SQL  
**Frameworks & Libraries:** Flask, jQuery, Bootstrap, Jinja, SQLAlchemy ORM  
**Database & Industry Tools:** PostgreSQL, Git, GitHub, Command Line  

# Table of Contents
- [About the Developer](#about)
- [Features](#features)
- [Installation](#installation)
- [References](#references)

## <a name="about"></a>About the Developer
Throughout her career, Sarah has reengineer manual processes into automated and scaled solutions. During her time in finance, this took the form of automating quarterly reporting using VBA and macros. At Amazon, Sarah paired VBA with SQL to build a tool that automated a seven step manual workflow. Most recently at Dropbox, Sarah led her team to build an automatic PowerPoint deck generator that saved the sales organization ~500 hours a quarter. Till recently, Sarah thought that these interests process improvement meant a career in Operations. At Dropbox, however, she worked closely with developers on internal tooling and learned a better word for the type of work she loves: software engineering.

## <a name="features"></a>Features
#### Input Letters from Today's Spelling Bee Game and See the Solutions
<img src="https://github.com/sarahhtbarton/hackbright-project/blob/master/static/images/readme-feature-1.jpeg" align="right" width="50%">
When a user navigates to Solver, they encounter a form that asks for the 7 letters of the day, and which letter is required. Once they hit submit, a JavaScript event listener grabs the data from the form and sends it to the server as a post request. The server then creates an entry in the letter_input table that contains the letters from the form. After, a regular expression is called and finds all the words that can be made up from the letters. As the regex pattern finds each word, the word is added to another table called letterword_assoc. What you end up with is a table that is now populated with all the valid word solutions for today’s game. SQLAlchemy retrieves the records from the letterword_assoc table, and uses the relationships with other tables to pull in the word, if it's a pentagram, and if it has been whitelisted or blacklisted. Finally, JAX executes the callback function, which appends the words to a div in the HTML, where CSS styles it to highlight certain word attributes.

#### Give Feedback on Words in Today's Solutions
<img src="https://github.com/sarahhtbarton/hackbright-project/blob/master/static/images/readme-feature-2.jpeg" align="right" width="50%">
Users also have the ability to give feedback on words and update the Solver database. This feature allows users to “blacklist” words that Solver returned but that are not accepted by Spelling Bee, or “whitelist” words that Spelling Bee accepts but that Solver did not return. Next time, blacklisted words will appear struckthrough to indicate that they might not be accepted by Spelling Bee, and whitelisted words will have an asterix to indicate that a user has added them to the Solver database.

## <a name="installation"></a>Installation
To run Spelling Bee Solver on your local machine:

Clone this repo:
```
https://github.com/sarahhtbarton/hackbright-project.git
```

Create and activate a virtual environment inside your Solver directory:
```
virtualenv env (Mac OS)
virtualenv env --always-copy (Windows OS)
source env/bin/activate
```

Install the dependencies:
```
pip3 install -r requirements.txt
```

Set up the database:

```
createdb solver
python3 seed.py
```

Run the app:

```
python3 server.py
```

You can now navigate to 'localhost:5000/' to access Spelling Bee Solver.

## <a name="references"></a>References
[NYTimes Spelling Bee](https://www.nytimes.com/puzzles/spelling-bee)
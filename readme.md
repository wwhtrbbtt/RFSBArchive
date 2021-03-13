# RFSBArchive

Hi!
This is a small project I threw together in a few hours. The code isn't good nor fast.Its purpose is to archive the Shoutbox on the website "raidforums.com", and to get some (imo) interesting statistics.

Please be aware that im not responsible for any admin punishments, this could be against the forum rules.

## What is what?

### main.py

This file is used to get the "raw" data. That means, the nickname is still in raw HTML, this is intended to be viewed in an webrowser.
It scrapes all of the messages it can get (seems to be roughly 360k), and saves them in a file called messages.html.

### cleanup.py

This file is used to parse the HTML into actual usernames, and to make everything a bit prettier.
This can take a few minutes to execute. It outputs a file called formatted.txt
This requires that you already executed the file above.

### leaderboard.py

This file is used to create a leaderboard for the accounts that send the most messages. It will just print them to the console. 
This requires that you already executed the file above.

### getAllMessages.py

This file is used to get all messages from one specific account. It will output a fille called {name}.txt.
This requires that you executed the cleanup file.
You have to set the name in the first line of the code. (default: badhou3a)

## Ok, how do I run this?

You first have to obtain your RF token and place it in the first line of the code in main.py.

0) Install the required libraries by executing `pip install -r requirements.txt`
1) Scrape the SB by executing `python3 main.py`. This can take a while.
2) Clean up the results by running `python3 cleanup.py`. This can also take a few minutes


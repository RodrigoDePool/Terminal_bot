# Terminal bot
---
This python script allows to execute commands remotely on a linux terminal from telegram.


## Setup
---
First we must create a telegram bot: Access telegram and look for the _user_
**@BotFather**, send him  the command "/newbot" and follow the instructions.
Please store the token given, we will use it later on.

Now let's setup the script. First we need to install the python wrapper 
[python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot).
Once installed we are almost ready to go. We need to open the _terminalbot.py_ and
change "A" for the token given by @BotFather:
```python
TOK = 'A'
```

Also we need to change 0 for our personal telegram id:
```python
usr_id = 0
```

If we do not know it we can execute the script, open a conversation with our bot in
telegram and send him the command "/userid". This will return us the telegram user id.
Now we may change it in the code and once again run the script. 
Done! You can now execute commands from telegram in your linux terminal.


To execute the script: **python terminalbot.py**

To kill the script: Ctrl+C




### Known bugs
---
We cannot execute _sudo_ commands or open new terminals of any kind (python, bash, ...). Possibly there are more commands that can't be executed through telegram.

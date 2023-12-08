# Swapper
> *Discord renamer*

# Setup
1. Download and extract this repository
2. Open a shell in the directory you extracted the repository to
3. In the shell run the command `pip install -r requirements.txt`
4. When it has finished run the command `python swapper.py` to run the script
5. Input the token you want to attack
6. Press enter and the script will do its jon
7. By default it will rename all users in the format `Global username | random IP`

# How it works
First it gets all the users friends and saves it to a file called `friends.txt`, 
it will then run through this list and split it at the seperater (The `|`) and will 
append the user ID, to the `friend_ids` list, the script will then run through this 
list and send a patch request to discord with the username and the token you are 
attacking, this will change the nick for everything in the `friend_ids` list to 
what the script tells it to.

# Footnotes
This was made in under 30 minutes, if their are bugs join my discord `https://discord.gg/b9bHM36968`
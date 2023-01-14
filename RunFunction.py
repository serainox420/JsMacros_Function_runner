# EXPERIMENTAL CLIENT SIDE FUNCTION RUNNER

with open("file.txt", "r") as f:
  # filepath in relation to /.minecraft/
    contents = f.read()
    lines = contents.split("\n")[0:3]
    for line in lines:
        Chat.say("/"+line)
        
# contents.split('\n')[0] - will only run first line
# contents.split('\n')[0],contents.split('\n')[1] - will run first n second lines
# contents.split("\n")[0:3] - will run entire function from line 0 to line 3

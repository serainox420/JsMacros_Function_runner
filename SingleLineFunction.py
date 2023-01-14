# EXPERIMENTAL CLIENT SIDE FUNCTION RUNNER
# Run single line specified by [0]
with open("file.txt", "r") as f:
    contents = f.read()
    # contents.split('\n')[0] - will only run first line
    # contents.split('\n')[0],contents.split('\n')[1] - will run first n second lines
    lines = contents.split("\n")[0],#contents.split("\n")[1],
    for line in lines:
        Chat.say("/"+line)

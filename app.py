from os import system
from random import randint

MAX_COMMITS = 4

def commit():
	system("echo $(date) >> commits.txt")
	system("git add commits.txt")
	system("git commit -m Update commits.txt")
	system("git push")

for i in range(randint(1, MAX_COMMITS)):
	commit()

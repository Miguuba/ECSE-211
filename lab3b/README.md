# Setting up git for file transfer

## From local machine (PC) to BrickPi
- We say BrickPi is a "remote repository" or "remote repo" in this situation. 

### On BrickPi (remote)
- Create your lab folder on the Pi
```bash
$ mkdir ecse211/lab3/ 
$ cd ecse211/lab3/ # change directory to your desired folder destination
```

- Set up git: Initialize, User configuration, allow push to branch
> NOTE for config user name and email: if you wish to use a GitHub repo at the same time as this local repo, set the user's name and email to your name (or anything tbh) and your GitHub email.
> 
> More instruction coming!
```bash
$ git init . # initialize git 
$ git config --local user.name "dpm-xx"
$ git config --local user.email "dpm-xx"
$ git config --local receive.denyCurrentBranch updateInstead # allowing PC to push to master branch
```
- You're set to go!!

### On your PC (local)

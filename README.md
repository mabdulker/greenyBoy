# Greeny Boy
Ever thought "how to look like a good coder without coding?", Greeny Boy to the rescue. 
Greeny Boy is a simple bot programme to stack your GitHub activity.

### The above code only executes the commit part, in order to make it execute every day you will have to create a *cron* task or equivalent:

- Grant full disk access to **cron** 
  - > /usr/sbin/cron on mac
- Save GitHub credentials on disk by running

  - > **git config credential.helper store**
- Create cron job
    - > crontab -e
    - > 45 12 * * * cd [PATH TO CLONE OF FOLDER] && python3 app.py  
    - >🕚 *sets the time of execution to whenever you think your computer will be on (e.g. 12:45)*

&emsp;
#### ⚠️ **WARNING:** granting full disk access and storing your GitHub on your disk compromises the security of your GitHub and computer




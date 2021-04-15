# schedule-python-script-in-heroku
### This is a workaround method to schedule jobs using python script on heroku for free.

#### For detailed explanation checkout : https://youtu.be/SH_KOHyU6Dg

### The job scheduled in here is to populate a remote mongodb collection after every 10 seconds with a dummy data.


Steps to push local git repo to heroku remote and start the application:

- Create a local git repo 

- Use the following commands to deploy and start application:
```
1.heroku login

2.heroku create <name_app>  #(create a new empty application on Heroku. If you run this command from your app’s root directory,
the empty Heroku Git repository is automatically set as a remote for your local repository.)

3.git remote -v   #(to view the remote heroku app)

4.git push heroku master  #(deploying the code)


#To start the worker process :
5.heroku ps:scale worker=1

#To view the logs
6.heroku logs --tail

#Later when we need to kill the worker process : 
7.heroku scale worker=0


```

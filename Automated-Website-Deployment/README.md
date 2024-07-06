# Automated WebSite Deployment using Docker,GitHub and Jenkins

In this Project I have used the Git/GitHub, Jenkins and Docker and integrated all these technologies to create an automated system for Auto Deployment.

# How it Works
The Project which I have created is a very basic integration in DevOps Domain. In this Project, when the developer will commit the code, it will automatically push the code in backend to the respective GitHub Repository. Using the WebHooks from GitHub, as soon as the developer pushes the code, it will be send to Jenkins Workspace automatically and then Jenkins Jobs will be triggered automatically as per the Jobs queue. Also I have used the concept of Build Pipeline so that it will be easy to monitor the Jobs.<br><br>
Job-1 - This Job will copy the Code which GitHub send to Jenkins to the required WorkSpace/folder.
Job-2 - This Job will Launch the Docker Container having the specifications to deploy the website within it.
Job-3 - This Job will be used to test the website weather it is working properly or not.

And the best thing about all these Jobs is that it all will be automatically triggered as soon as the developer pushes the code to GitHub Repository.

# How to Create this Project
Well it is not as typical as it looks like. If you have good hold in your concepts, then this project is nothing for you. The very 1st thing would be setting up Git, Jenkins and Docker in Your System. For Setting Up Jenkins and Git you can refer to my <a href="https://www.linkedin.com/posts/abhinavdubey26_dockers-dockerimage-automation-activity-6668859867073273856-P6D2">article<a>.Once You set Up Git, Jenkins and Docker you can easly go for creating Your Jobs and if you don't knwo how to create jobs you can read the above article where I have explained in a detailed way of creation of jobs in jenkins or you can watch this <a href="https://www.youtube.com/watch?v=CRvzphqTtU4">video</a>.<br>
In Job-1's execute shell write
  sudo cp -rvf * /name_of_your_WorkspaceFolder and then save it.
In Job-2's execute shell write,
  if sudo docker container ls | grep production
  then
  sudo docker conatiner rm -f production
  else
  sudo docker dun -dit -p 8081:80 -v/name_of_your_WorkspaceFolder:/usr/local/apache2/htdocs --name production httpd fi" and then save it and go and create Job-3
In Job-3's execute Shell write
  status=$(curl -o Your_SysIP:8081/)
  if[[ $status == 200 ]]
  then
  echo "Successfull"
  exit 0
  else
  echo "Error"
  exit 1
  fi and then save it and come out of Job-3
  
After Writing the codes, the next task will be to link all these using build Pipeline so that at one go all will Jobs run and and it will be easy to monitor. Before creating build ppipeline we need to set build triggers such that when Job1 will run, automatically it will triggered Job2 and Job3. Job1 --> Job2 --> Job3


Now as you have set the triggers, to each job, now it's time to create a pipeline so that we can easliy manage the whole CI/CD Pipeline. If you don't know how to set-up Build pipeline, then you just need to download the Build Pipeline Plugin from Plugin Manager in Jenkins and then I have uploaded the images for your convienent in image folder with names pipeline-1 and pipeline-2 for creating a pipeline for any project. If all the three Jobs will run succesfully then you will get green color.

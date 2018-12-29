title: Deploy A Flask App to Google App Engine
date: 2017-03-25
tags: [deployment, cloud, linux]
published: True
subtitle: Google provides a platform where you can quickly deploy apps. Getting to deploy our first python app on google appengine flexible environment should be easy. Follow this guide to deploy your Flask App to google appengine.

### Install Cloud components

    $ gcloud components install app-engine-python #

List the components to verify is you app is installed.

    $ gcloud components list

Proceed to login:

    $ gcloud login auth login

Follow your browser and login

### Project Setup

Visit your Google Cloud console and create an app. You can equally use an existing app. 
Retrieve your project name get ready for deployment:

    $ gcloud config set project [projectname]

Let's verify if our app is running locally.

    $ gcloud app browse

Deploy our app to app engine

    $ gcloud app deploy

Your app is now available here `http://[YOUR_PROJECT_ID].appspot.com`

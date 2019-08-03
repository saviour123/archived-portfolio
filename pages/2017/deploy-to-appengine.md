title: Deploy A Flask App to Google App Engine
date: 2017-03-25
tags: [deployment, cloud, linux]
published: True
subtitle: Google provides a platform where you can quickly deploy apps. Getting to deploy our first python app on google appengine flexible environment should be easy. Follow this guide to deploy your Flask App to google appengine.

### Install Google Cloud sdk and components

Head to [google cloud to install the gcloud-sdk](https://cloud.google.com/sdk/docs/quickstarts)
and install a compatible sdk for your system.
After that, there are many components you can install with `gcloud sdk`. But we would install only the python components for now.

    $ gcloud components install app-engine-python #

List the components to confirm the installed components.

    $ gcloud components list

Authenticate your gcloud setup:

    $ gcloud login auth login

The terminal would open your default browser and login with your activated Gmail.

### Project Setup

Visit your Google Cloud console and create an app. You can equally use an existing app.
Retrieve your project name get ready for deployment:

    $ gcloud config set project [projectname]

Then setup your project `app.yaml`. Sample below

    runtime: python37
    service: awesome-app
    api_version: 1

NB: Configure the one which is compatible with your project and test locally.
Let's verify if our app is running locally.

    dev_appserver.py app.yaml

Visit the address displayed on your console in the browser. Once everything looks fine.
We can then deploy our app.

Deploy our app to app engine

    $ gcloud app deploy

Wait patiently while your app builds and deploy to appengine.

    $ gcloud app browse

Your app is now available here `http://[YOUR_PROJECT_ID].appspot.com`

PS: If you have any issue on the way. Google is your friend.
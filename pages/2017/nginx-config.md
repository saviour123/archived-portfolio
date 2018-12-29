title: Serving Static Files With Nginx
date: 2017-03-13
tags: [nginx, server, linux]
published: True
subtitle: Let get into Linux servers and do some basic static sites deployment config with nginx. This is basic enough to get you going!



Getting the first static site runnning is quite simple. 
### Requirements
- Ubuntu 16.04
- [Bootstrap starter](https://github.com/BlackrockDigital/startbootstrap-freelancer.git)


### Lets begin with the installation of nginx

    $ sudo apt-get update && sudo apt-get install nginx

> _NB. In production, its recommended to compile your own nginx and add Web Application firewall which gives extra security to your app._

Point your browser to `127.0.0.1` to verify if **nginx** is
up and running properly. You can also verify the status from the terminal with

    $ sudo service status nginx 

### Add your configuration

The installation comes with a default template in the `/etc/nginx/sites-available/default`

Let edit this file and add our own content!

    $ cd /etc/nginx/sites-available
    $ cp sudo mv ./default ./awesome-site


Replace the content of `awesome-site` with the below

### Now we are ready to edit `awesome-site`

    $ vim /etc/nginx/sites-available/awesome-site

Replace the content with this

    server {
	    listen 8080;
	    # server_name _;
	    root /var/www/awesome-site;
	    index index.html;

	    location / {
                try_files $uri $uri/ =404;
            }
        }
    }

Few things: 

`listen` -> is the port for which our content would be served on.

`root` -> location of our static files **/var/www/** directory.

### Add the static contents
    
    $ cd /var/www/
    $ git clone https://github.com/BlackrockDigital/startbootstrap-freelancer.git
    $ sudo mv startbootstrap-freelancer awesome-site

### Create Symlinks

Nginx works with symlinks- hypothetical references to a config file. Let's create one for our site.

There are two important folders in `/etc/nginx/` we would work with.

> -  _sites-available_
- _sites-enabled_

    $ cd /etc/nginx/sites-enabled
    $ sudo ln -s /etc/nginx/sites-available/awesome-site .
    $ sudo service nginx reload

Your server is up! Point to `http://127.0.0.1:8080` and our site is up.
There are more powerful stuff to do with nginx, forward proxy, reverse proxy, 
compressing, load balancing and many others. Head to [Nginx Docs](http://nginx.org/en/docs)

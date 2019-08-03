title: Serving Static Files With Nginx
date: 2017-03-13
tags: [nginx, server, linux]
published: True
subtitle: Let get into Linux servers and do some basic static sites deployment setup. We would use Nginx. This is basic and there is more at [nginx](http://nginx.org/en/docs/beginners_guide.html)!


### Requirements

- Ubuntu 16.04
- nginx
- [Bootstrap starter](https://github.com/BlackrockDigital/startbootstrap-freelancer.git)


### Lets begin with the installation of Nginx

    $ sudo apt-get update && sudo apt-get install nginx -y

> _NB. In production, its recommended to compile your own Nginx version and install other components like modsecurity, Nginx-status, etc. for extra functionality and security._

Point your browser to `127.0.0.1` to verify if **nginx** web server is
up and running properly. You can also verify the status from the terminal with

    $ sudo service nginx status

### Add your configuration

On your Linux distribution, Nginx configurations are located in `/etc/nginx/`. The default `nginx.conf` is also located here. There two folders here we would work with. `/etc/nginx/sites-available/` and `/etc/nginx/sites-enabled`.
The installation comes with a default template in the `/etc/nginx/sites-available/default`

Let edit this file and add our own content!

    $ cd /etc/nginx/sites-available
    $ sudo cp default awesome-site

### Now we are ready to edit `awesome-site`

Edit `awesome-site`
   
    $ vim /etc/nginx/sites-available/awesome-site

Replace the content with this

    server {
   listen 80;
   server_name awesome-site.com;

   root /var/www/awesome-site;
   index index.html;

   location / {
                try_files $uri $uri/ =404;
            }
        }
    }

Few things:

`listen` -> is the port for which the webserver would be listening on. I am using `80`.

`root` -> location of our static files **/var/www/awesome-site** directory.

### Add the static contents
   
    $ cd /var/www/
    $ git clone https://github.com/BlackrockDigital/startbootstrap-freelancer.git
    $ sudo mv startbootstrap-freelancer awesome-site

### Create Symlinks

Nginx works with symlinks- hypothetical references to a file. Let's create one for our site.
This symlink must be created in Nginx `sites-enable` referencing the config in sites-available. This tells Nginx you have enabled the site.

There are two important folders in `/etc/nginx/` we would work with.
   
    $ cd /etc/nginx/sites-enabled
    $ sudo ln -s /etc/nginx/sites-available/awesome-site .
    $ sudo service nginx reload

Your server is up! Visit `http://127.0.0.1/` in your browser and our site is up.
There are more powerful stuff to do with Nginx, reverse proxy, CGI,
compressing, load balancing and many others. Head to [Nginx Docs](http://nginx.org/en/docs)


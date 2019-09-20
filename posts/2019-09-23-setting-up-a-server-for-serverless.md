---
type: post
title: Setting Up a Server for Serverless
excerpt: Even for serverless, you sometimes need a server!
date: 2019-09-23
dateText: 23rd September 2019
author: Martin Dawson
---

As of writing, it is 2019 and the buzzwords in the last year or two have been ‘JAMStack’ and 'serverless'. I too was transfixed by this concept when I first stumbled upon it, and the possibilities it offers are amazing. A big part of the JAMStack is the concept of everything being _serverless_ which appeals to me on many levels. The concept is deceptive in that there are still servers, but they are managed by other, more capable people, and I don’t have to get my hands dirty in the world of server management.

This is all well and good, but whilst the possibilities are continually expanding, depending on what your project is, you may need to spin up a server, make sure it’s secure, host your website or app on it. Incidentally I'm calling it a server which is synonymous with web host, but it's just a Linux machine, which has many other uses. The big advantage is that it is always on, so you can schedule jobs to run in it all day everyday, for data processing, or a development server, for example.

I had never done this before, but I decided to give it a go. It wasn’t nearly as scary as I thought it might be, and was actually pretty fun and I’d recommend that if you are technically minded in any way, you should try setting one up. It may show what is possible with a relatively uncomplicated set up.anyone do it at least once.

In case I need to do it again, here is what I did.

In order to do this it would be helpful if you were familiar or comfortable with the command line, as that is where most of this tutorial takes place. Also, I am doing all this from an Apple MacBook. If you are on Windows, you might need a different tutorial.

## Server

First things first, you need a server. A virtual server to be precise, and after hearing good things about [Linode](https://linode.com) from a number of different sources, I set up an account with them, and chose their smallest server (called a Nanode).

To set up a server, you need to choose:

* **a distribution** - this is the flavour of operating system you desire. If you have a particular flavour you love then choose that but as the foundation for this tutorial, you should know that I chose Ubuntu 18.04
* **Server location** - If this is to server customers, then choose a location near to them. I am European, and it’s for me, so I chose accordingly.
* **Linode Plan** - This is the size of server you want. I wanted to mess around on a development server, so I chose Linodes smallest size, a Nanode, which costs $5 per month and gives me 1 CPU, 25Gb of storage and 1 Gb of memory, which is plenty. If I outgrow this, I can easily resize my server.
You will also need to enter a root password which you’ll need later on to get in to the server.

So I’ve chosen my server, and after a short while it’s up and running. Now I need to get in to it. To do this I am going to SSH in to it. SSH stands for secure shell, and it provides a way to access a server from the command line of your local machine.

Your new server will have an IP address which can be found in the Networking tab of your Linode dashboard, e.g. 111.22.333.444. If you go to your command line and type ssh root@111.22.333.444 you will be asked to enter your root password you entered earlier. Once that’s done, you’re in! You should notice that your command line prompt will change. Now everything you do in that terminal window will be giving commands to the server, not your machine. For example, if you type _ls_ to list the directory, it will show the directory of your server, not your  local machine. You get the idea.
To return to your local machine, type exit.

First things first, make sure your server is up-to-date, by typing in the following:
    
    apt-get update && apt-get upgrade
`
Next, update the host name and set it to be the name you want to give to your server.
    
    hostnamectl set-hostname serverless-server-1

You can check that it has updated by typing `hostname`

And then the host file can be updated to associate the updated host name with the IP address of the server. Open the hosts file in a text editor, e.g. nano, by typing:
    
    nano /etc/hosts

and add a line with IP address and host name
    
    178.79.177.137  serverless-server-1

## Setting up a limited user

At the moment, we’re in the server as the root user, which is currently the only user able to login to the server. On top of this, the root user is the most powerful, having unlimited access to the server. Every server has a root user, and depending on how strong your password is, it may not be that hard to access the server if someone really wanted to.

To make things a bit more secure, the first thing to do is add a new user, with limited access rights.

    adduser prettystatic

… and add it to the sudo group to allow superuser access
    
    adduser prettystatic sudo

Easy! Now logout of root and login as the new limited user.

Next, instead of using a password to login, we can set up ssh key pairs that are exponentially more difficult to crack than a password.

## SSH Key Setup
Add ssh folder to server
    
    mkdir -p ~/.ssh

On **local** computer generate keys

    ssh-keygen -b 4096

… and copy the public one to the server

    scp ~/.ssh/id_rsa.pub prettystatic@178.79.177.137:~/.ssh/authorized_keys

Change some permissions on the server for the SSH

    sudo chmod 700 ~/.ssh/
    sudo chmod 600 ~/.ssh/*

Great. New user, with SSH key pair authentication.

Finally, the server configuration can be adjusted to only allow access via ssh key pairs, disable password authentication and to cover all bases, root login can be disabled.

    sudo nano /etc/ssh/sshd_config

Set `PermitRootLogin` to `no`

Uncomment `PasswordAuthentication` and set it to `no`

Now restart ssh for changes to take effect
    
    sudo systemctl restart sshd

This server is much more secure now that we can be almost certain that no-one else can access it.

## Setup Firewall

This server is going to be used to host and serve websites, and a firewall can be set up to dictate exactly what incoming and outgoing traffic is allowed. On Linux, there is a configuration tool called **ufw** which stands for uncomplicated firewall. Let’s install it.

    sudo apt-get install ufw

And set up some basic rules

* Allow outgoing traffic `sudo ufw default allow outgoing`
* Deny incoming traffic `sudo ufw default deny incoming`
* Allow ssh `sudo ufw allow ssh`

I’m going to be using this as a Jekyll development server which has a default port of 4000 that I want to allow traffic to and from

    sudo ufw allow 4000

And then http and https incoming traffic will be allowed

    sudo ufw allow http
    sudo ufw allow https

To enable all those changes…

    sudo ufw enable

… and check the status
    
    sudo ufw status

Done!

## Setup NGINX

Setting up nginx turns your linux server into something that will serve. It's worth having it set up and ready to be configured to be a development server. If you need to add a custom domain and SSL certificate and dedicate this server to serving production websites, then Nginx is what you want, but that is not covered in this post. For now, as long as Nginx is set up you can serve a website at the IP address of the server.

So, install nginx
    
    sudo apt install nginx

Check what configurations are available
    
    sudo ufw app list

You should have

    Nginx Full
    Nginx HTTP
    Nginx HTTPS

Set the firewall to accept the HTTP configuration seeing as this is a dev server
    
    sudo ufw allow 'Nginx HTTP'

Nginx sets the default server block to be served from `/var/www/html`



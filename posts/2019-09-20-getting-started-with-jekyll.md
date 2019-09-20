---
type: post
title: Getting Started with Jekyll
excerpt: Jekyll got me in to Static Site Generators, and remains a sensible choice for many types of website.
date: 2019-09-20
dateText: 20th September 2019
author: Martin Dawson
---

Jekyll is my first love of Static Site Generators, and of building websites in general. It's a good mix of code, templates and logic which can generate simple websites pretty easily. I do not really make complex websites, and it is not the right tool for everything, but it provides power, speed and security which would suit a large variety of use cases.

But it hasn't always been easy, and sometimes getting some momentum going can feel a bit like hard work. For the record, I do not think the problem is with Jekyll in particular. You see, by day, I don’t build websites. I do other stuff, and to be honest that stuff takes up a lot of my time, and on top of other commitments it leaves precious little time to explore other pursuits, one of which is building websites.

So I thought I would write a beginners guide together, to try and show what can be done, and also to serve as a refresher for me, when I have not used it for a while. 

## Why Static Site Generators?

Jekyll is a Static Site Generator. When I first heard of it around the year 2013, I had never heard of Jekyll or of Static Site Generators. When I realised what they were - a mechanism to combine templates and markdown files to generate static pages of HTML, I found it fascninating. The advantages of this appealed to me:

* **They are cheap** - If I put in the effort and pick up a cheap domain name, the hosting can be free, and after all, this is a hobby.
* **They are secure** - There is very little to compromise in terms of security, and I can rest easy knowing that no-one os going to silently invade my database or server.
* **They are customisable** - I can pick up a theme someone else has made, or write my own simple one pretty easily, and (try to) make it look exactly as I want.
* **They scratch an itch** - I can code a little or a lot. Just build some basic HTML and CSS, or go bonkers getting data with Python or Javascript. Im not a developer, but I can code and I like keeping my skills relatively fresh.

## Why Jekyll?

I'm writing this in 2019, and since my discovery of Jekyll 6 years ago, there are lots of other Static Site Generators, and many of them are superior in certain areas.

Jekyll is often critisised for being slow, and there are many of Jekyll's contemporaries that leave it for dust in the performance stakes. But I think that Jekyll gives the beginner and more advanced user a good variety of tools to work with, and as each version rolls round, performance improves, even if it isn't blisteringly fast. Off the shelf, you get a lot - compiling Sass, code minification, decent templating engine, theme support. It is incredibly versatile and for the kind of websites that are suited to Static Site Generators, Jekyll is a robust tool that should not disappoint.

But, there is a problem. Everytime I want to start a new project with Jekyll, it feels like learning it again. The documentation is good, but I always have the same sort of problems, and I start a project so infrequently that I always forget where to start the next time. So, this doc aims to be a step by step approach to kicking things off.

## Goals

The aim of this article is to:

* Explain how to install Jekyll
* Explain a few of the basic concepts of Jekyll
* Show how to make a website for blogging from scratch with a basic skeleton on which to build

## Pre-requisites

If you want to have a go, it would be useful if you had:

* Basic knowledge of using the command line
* Basic knowledge of HTML and CSS

It's worth mentioning that this is not for everybody. Jekyll is something to explore if you don't mind getting your hands dirty in a bit of code, so if that's not for you, maybe look for a different way to build your website. 


## Installation

**I’m doing all of this on a Mac. If you use something else, then maybe you need a slightly different tutorial**

I can give you instructions here, but when ever I've tried to install or update Jekyll, more often than not I run in to unexpected problems. I am not going to claim to be the man to solve all those problem with installation, so if these instructions do not work, consult your good friend Google to try and overcome them.

As I am on a Mac, the first thing to do is to make sure Xcode Command Line Tools are installed. The check this type `gcc -v`, and if you need to install them, then do so using `xcode-select --install`.

To make a website with Jekyll, you need to install it, and to install it you need Ruby. Check your version of Ruby first. The latest version at time of writing is 2.6.3, but you can find out [here](https://www.ruby-lang.org/en/downloads/) what the latest version is if you don’t know. Jekyll needs at least version 2.4.0 of Ruby.

    ruby -v

If you don’t have Ruby, install it using Homebrew

    brew install ruby

You want the latest version of Ruby probably so if you have it and don’t have the latest version then upgrade it using Homebrew

    brew upgrade ruby

Great, you’ve got Ruby!

Now you want Bundler which is a package manager for Ruby that will do a lot of the heavy lifting when trying to install Jekyll

    sudo gem install bundler

Done!

Now let’s install Jekyll

    sudo gem install jekyll

Everything should now be ready, so we’re going to start a new site. One way that this can be done is by setting up the default Jekyll website by typing

    jekyll new my-website-name

This will create a website in the folder ‘my-website-name’ and you can go and play with it and tweak it as much as you like.  It gives you a lot, and if you’re planning on building a website based on a theme, then this is the quickest way to get going. But in other ways it gives you too much, especially if you want to build things as you go, or are working off a site you’ve already designed. Sometimes I find it better to just create things as you go, and this also helps understand the concept behind Jekyll and Static Site Generators, so that is what I am going to talk through.

## Creating a website 

We’ll call our website first-site, and so we can create a folder for this and navigate to it via the command line

    mkdir first-site && cd first-site

This is our **root** folder.
To work in the folder, drag it to your code editor, and we can begin making files and folders there.
In the root folder, create an index.html file and we will add some html to it

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>First Site</title>
    </head>
    <body>
        <h1>Hi, my name is Martin</h1>   
        <p>This is a website that has been created using Jekyll!</p>
    </body>
    </html>

Now to build this we can utilise Jekyll’s own built-in development server by typing

    jekyll serve

What this command does is:

1. Builds the website and stores the built site in a folder called `_site`. This could also be achieved by typing `jekyll build`
2. Serves this from port 4000 on your local host
3. Rebuilds and republishes the site every time a file is saved

For reference, never make any changes in the `_site` folder, because it will be overwritten next time you build the site.

So far, so good. But it feels a bit heavy handed to set up Ruby, Bundler, and Jekyll to generate this page, right? Spot on. But the power comes when you start using templating, layouts and front-matter.

## Front Matter and Templating

Jekyll uses a templating language called Liquid which allows the user to use variables and logic at build time to make generating pages more efficient.

We’re going to change our index.html file a bit to add something called **front matter**. In the simplest terms, front matter are pieces of data that can sit at the top of the file, to be referenced by Liquid. They sit between two sets of three dashes like so.

    ---
    author: Martin
    ---
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>First Site</title>
    </head>
    <body>
        <h1>Hi, my name is {{ page.author }}</h1>   
        <p>This is a website that has been created using Jekyll!</p>
    </body>
    </html>

In addition to the front matter, the h1 tag has replaced the word ‘Martin’ with `{{ page.author }}`. This is an object in Liquid templating, and it says ‘look on this page for the front matter item called author and grab the value’.

Front matter is one place to store variables, but a more global set of variables can be stored in the configuration file.

## Configuration

The aim of the configuration file is to set global site values that will not change too often, like the URL, SEO description, social media usernames, Google Analytics reference and contact email .

The default configuration should be called `_config.yml`. You can create config files with different names and they can be referenced at build time. For example if you had a development configuration file called `_devconfig.yml` you would build the site using

    jekyll build --config _devconfig.yml

Everything in the config file can be referenced under the site object. Let us create ours:

    title: First Site
    email: hello@first-site-example.com
    description: A tutorial website that we set up to demonstrate how Jekyll works


If we want the title to be used as the title of every page, we could reference `site.title` in the head tag.

It is worth noting that if the development server is running and you make config changes, you have to press Ctrl-C and then serve the site again for the changes to take effect. That will save you hours of wondering why you can’t see your page title.

## Layouts

You can see that so much of our index.html file is actually information we would want on every page, so if we add a link to a stylesheet, we would not want to add it to every page individually. So we can use a layout which is a template that can be used for each page.

First we need a layouts folder - so we’ll create `_layouts` and within there, we can add a file called default.html

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>{{ site.title }}</title>
    </head>
    <body>
    {{ content }}
    </body>
    </html>

And our index file can be changed to…

    ---
    layout: default
    author: Martin
    ---
    <h1>Hi, my name is {{ page.author }}</h1>   
    <p>This is a website that has been created using Jekyll!</p>


When the site gets built, Jekyll takes the layout ‘default’ and replaces the {{ content }} object with the contents of the index file.

## Includes

The other area which helps us to modularise and build our website, is to have **includes**. These are small pieces of html stored in files that can be added in to other pages. Let me demonstrate by adding a footer to our page.
Create a folder in the root called `_includes` and add a file called footer.html which looks like this

    <footer>
        Made by Martin
    </footer>

We want this footer to appear on every page we eventually have, so we can add it to the default layout like this:

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>{{ site.title }}</title>
    </head>
    <body>
        {{ content }}

        {% include footer.html %}
    </body>
    </html>

and we can even create a head.html include file that contains all the HTML held within the \<head\> tag in so the default layout will look like this:

    <!DOCTYPE html>
    <html lang="en">
    {% include head.html %}
    <body>
        {{ content }}

        {% include footer.html %}
    </body>
    </html>

It’s much easier to read, and much easier to update, and sets us up nicely to add more pages. But let’s add a different type of page. A **markdown** page, called about.md. Markdown is a markup style that makes it easier to write html. Jekyll handles it without any fuss, right out of the box. Just make your file extension **.md** and the rest takes care of itself.

    ---
    layout: default
    ---
    # About
    This is an about page written in [Markdown](https://daringfireball.net/projects/markdown/syntax)

    It is much easier to write HTML when markdown is going to convert everthing when it builds!

    Now if you visit http://localhost:4000/about.html, you can see the result.

## Blogging

Hopefully you can start to see the power that Jekyll holds. It can be used for so many types of websites, but the one type that crops up again and again is blogging. To demonstrate this, we’re going to create a folder called `_posts` and in there we will create a file called 2018-05-10-first-blog-post.md

    ---
    layout: post
    author: Martin
    title: First Blog Post
    ---
    This is my very first blog post and i think it will be really good to read.

Also a new layout needs to be created called ‘post.html’

    ---
    layout: default
    ---
    <h1>{{ page.title }}</h1>
    <p>{{ page.date | date_to_string }} - {{ page.author }}</p>

    {{ content }}

In fact, I’ve created another two posts as well. Seeing as Jekyll is a tool that is popular for its bloggin prowess, it casn recognise all posts in the `_posts` folder, and holds them is a collection, which can be iterated through. On a new page called `blog.html`, the following code will generate a list of the blog posts that have been created and can be linked to, so as the whole post can be read.

    ---
    layout: default
    title: Blog
    ---
    <h1>Latest Posts</h1>

    <ul>
    {% for post in site.posts %}
        <li>
        <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
        <p>{{ post.excerpt }}</p>
        </li>
    {% endfor %}
    </ul>

This is a lot more code than everything else I’ve shown you so far. In summary, Jekyll knows that people will be using this for blogging and will recognise that all items in the posts folder are a collection of posts, held in a list called **site.posts**. You can loop through each item in the list using a for loop block. Each item of front matter can be referenced by their name using Liquid tags within the html.

Each post has a number of attributes as standard.

* **post.url** - the location of the whole post, and nice and easy to link to.
* **post.date** - This is derived from the file name. E.g. 2010-05-10-first-blog-post.md has a post date of 10th May 2019. It can be formatted with a filter in the Liquid templating.
* **post.excerpt** - This is the first paragraph of the body of the post

Now with this page of all blog posts, we have the bare bones of a blog without too much fuss.

## Conclusion

It’s all terribly clever and there is so much more to it. Your sites can become really powerful, and there are many concepts I have not even mentioned.

I decided to write this to give myself some reminders of how everything works and how to get started with Jekyll. For anyone else reading it, hopefully this article will provide you with somewhere to jump off. I may write more articles around other aspects and the next stages, but in the mean time there is plenty of documentation around, not least the actual Jekyll documentation. Here are some useful links for further reading:

* [Jekyll Website](https://jekyllrb.org)
* [Liquid Templating Website](https://shopify.github.io/liquid/)



Title: Adventures in AWS: Part 1
Date: 2014-1-6 20:39
Category: Projects
Tags: aws, operations
Slug: adventures-in-aws-1
Summary: My first experiences with AWS

# Why AWS

I've used a Linode server to host my various services for a few years now.
It's been pretty good. My mumble server has only had a few
hiccups from Linode issues (network hardware failure, DOS), and the
specs on the box have gotten better over time.

With AWS lowering its pricing, and the fact that so many people use AWS
and value experience using it, I wanted to start using it for my personal
servers.

# My current setup

* 4 t2.micro instances
  * NAT instance
  * openvpn server
  * nginx server
  * mumble server
* vpc with 2 subnets: one public, one private
* deployed using cloudformation
* configured using masterless salt

# Getting to today

I had a lot of missteps and days spent digging through documentation to
figure out exactly what my final state should be and how to get there.
Not to mention many thrown away ideas.

First I started setting up a Vagrant environment I thought would emulate
AWS EC2. Vagrant is really helpful testing configuration management.
When I start working on a project I branch my config and spin up
vagrant instances to make sure things are applied correctly.

I was going to try switching from masterless salt, which I had been
configuring my servers, both Linode and home, with, but halfway
through getting things set up I scrapped that idea. I don't really
need central management for my servers, especially not with using
EC2 and openvpn for the first time.

I decided to cut my scope back and focus on what I really needed, 
duplication of my Linode stack and adding an openvpn connection between
AWS and home so I could access files from my NAS server. So I finished
the changes I needed to make to split my services onto different servers
and started the interesting bit, AWS.

I had looked into some AWS documentation, so I knew I wanted to have
a NAT and have services behind it so I could share one IP address
between servers, but there are not many full guides to getting started
on Amazon. There are many snippets of things that I had to piece together
and modify to even get running.

First I reserved two micro instances in the same zone and started
playing with the NAT tutorial. It was fairly easy to follow. I had a few
slip ups, but I can't remember what they were now.

Then I started looking at Cloudformation. This is where interesting took
on the Chinese proverb meaning. I found a guide for a over-engineered
(for my needs) high availability NAT Instances. I dumbed the guide down
to be a simple NAT and added info for the Ubuntu AMIs for my other
servers.

I realized very quickly that Cloudformation JSON is ugly. Not just wow
this JSON is big, or it's unplesant to write. No, it's almost as bad as
XML. I've already committed to moving to something, anything else for
Cloudformation template generation. There have been several times
where my template hasn't validated or I wrote something incorrectly
that wasn't caught by the template validator.

It took me roughly a week to get my Cloudformation template working
properly. The biggest trip ups I had were incorrect security groups,
forwarding ports twice for fun and profit, and VPC dependencies on
the gateway to the internet. The final version is in my git repo.

During that time I was also wrapping my head around Route 53, which
I think I understand now, but I haven't done my DNS move yet, so
results are out on that.

# Afterthoughts

AWS is really cool, but there's a lot of ramp up time needed to
understand how to do things with it. With the added terror of
accidentally running up charges, the learning curve is very steep
for something that's *the* major provider of cloud computing resources.

Maybe having more previous operations experience might have made this
easier, but I'd expect this to be easier having messed around with
servers and Vagrant.

# What's next

* Pointing DNS records at AWS
* Openvpn testing
* Cloudformation template improvements
* Update salt on all nodes
* Move IRC bot to AWS
* downtimeless Cloudformation deploys

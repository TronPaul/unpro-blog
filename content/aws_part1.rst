Adventures in AWS: Part 1
#########################

:date: 2015-1-6 20:39
:category: Projects
:tags: aws, operations
:slug: adventures-in-aws-1
:summary: My first experiences with AWS

Why AWS
=======

I've used a Linode server to host my various services for a few years now.
It's been pretty good. My mumble server has only had a few
hiccups from Linode issues (network hardware failure, DOS attacks), and the
specs on the box have gotten better over time.

With AWS lowering its pricing, and the fact that so many people use AWS
and value experience using it, I wanted to start using it for my personal
servers.

My current setup
================

* 4 t2.micro instances

  * NAT instance
  * Openvpn server (unfinished)
  * Nginx server
  * mumble server

* VPC with 2 subnets: one public, one private
* deployed using Cloudformation
* configured using masterless salt

Getting to today
================

I had a lot of missteps and days spent digging through documentation to
figure out exactly what my final state should be and how to get there.
Not to mention many thrown away ideas.

First I started setting up a Vagrant_ environment I thought would emulate
AWS EC2. Vagrant is really helpful testing configuration management.
When I start working on a project I branch my configuration and spin up
vagrant instances to make sure things are applied correctly.

.. _Vagrant: https://www.vagrantup.com/

I was going to try switching from `masterless salt`_, which I had been
configuring my servers, both Linode and home, with, but halfway
through getting things set up I scrapped that idea. I don't really
need central management for my servers, especially not with using
EC2 and Openvpn for the first time.

.. _masterless salt: http://docs.saltstack.com/en/latest/topics/tutorials/quickstart.html

I decided to cut my scope back and focus on what I really needed, 
duplication of my Linode stack and adding an Openvpn connection between
AWS and home so I could access files from my NAS server. So I finished
the changes I needed to make to split my services onto different servers
and started the interesting bit, AWS.

I had looked into some AWS documentation, so I knew I wanted to have
a NAT and have services behind it so I could share one IP address
between servers, but there are not many full guides to getting started
on Amazon. There are many `snippets`_ `of`_ `things`_ that I had to 
piece together and modify to get running.

.. _snippets: http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_NAT_Instance.html#EIP_Disable_SrcDestCheck
.. _of: http://serverfault.com/questions/406351/how-to-configure-a-custom-nat-for-use-in-amazon-vpc
.. _things: http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/t2-instances.html#t2-instances-hvm-support

First I reserved two micro instances in the same zone and started
playing with the NAT tutorial. It was fairly easy to follow. I had a few
slip ups, but I can't remember what they were now.

Then I started looking at Cloudformation. This is where interesting took
on the Chinese proverb meaning. I found a `guide`_ for a over-engineered
(for my needs) high availability NAT Instances. I dumbed the guide down
to be a simple NAT and added info for the Ubuntu AMIs for my other
servers.

.. _guide: https://aws.amazon.com/articles/6079781443936876

I realized very quickly that Cloudformation JSON is ugly. Not just wow
this JSON is big, or it's unpleasant to write. No, it's almost as bad as
XML. I've already committed to moving to something, anything else for
Cloudformation template generation. There have been several times
where my template hasn't validated or I wrote something incorrectly
that wasn't caught by the `template validator`_.

.. _template validator: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-validate-template.html

It took me roughly a week to get my Cloudformation template working
properly. The biggest trip ups I had were incorrect security groups,
forwarding ports twice for fun and profit, and VPC dependencies on
the gateway to the internet. The `current version`_ is in my `git repository`_.

.. _current version: https://github.com/TronPaul/unpro-salt/blob/fe6b60fc5761f10f240ba47ee57ccb512e50212f/unpro.template
.. _git repository: https://github.com/TronPaul/unpro-salt

During that time I was also wrapping my head around Route 53, which
I think I understand now, but I haven't done my DNS move yet, so
results are out on that.

Afterthoughts
=============

AWS is really cool, but there's a lot of ramp up time needed to
understand how to do things with it. With the added terror of
accidentally running up charges, the learning curve is very steep
for something that's **the** major provider of cloud computing resources.

Maybe having more previous operations experience might have made this
easier, but I'd expect this to be easier having messed around with linux
servers and Vagrant.

What's Next
===========

* Pointing DNS records at AWS
* Openvpn testing
* Cloudformation template improvements
* Update salt on all nodes
* Move IRC bot to AWS
* downtimeless Cloudformation deploys

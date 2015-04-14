Adventures in AWS: Part 2
#########################

:date: 2015-4-13 22:55
:category: Projects
:tags: aws, operations
:slug: adventures-in-aws-2
:summary: Returning to AWS

Building Your Own AMI
=====================

Is fairly annoying. If you want to build a AMI for instances in your
VPC, you need to build them in a VPC. If you want to build them
without modifying your NAT setup, you need to be VPN'd into your VPC.
Good thing I have a VPN set up I guess, though it was a bit of a pain
even then. Looking back. I could've created a VPC just for AMI
building. Whoops.

The other issue I ran into is the Go library I've been using to
make VM images, packer_. It enjoys to error out talking to EC2--for no
good reason. It constantly times out or errors on creating and getting
info about resources. I had to patch_ and build packer manually (not a
fun process). It was my first experience with Go. I was not impressed.

.. _Packer: https://www.packer.io

.. _patch: https://github.com/mitchellh/packer/issues/1539#issuecomment-75150399

Otherwise having my own AMI speeds things up slightly. All my base
image is, is my salt configuration on disc, and the base salt
configuration applied (install vim, hooray...). When I get to my next
project, monitoring. This will be a lot more helpful.

CloudFormation Templating (Cloudforge)
======================================

I wrote a tool for myself called Cloudforge_. It takes a yaml
definition of stack(s) that can use and render templates for similar
resources. In my use case, all of my instances are very similar so I
abstracted them into a template that I pass variables into.

.. _Cloudforge: https://github.com/TronPaul/cloudforge

When I started using CloudFormation I found myself copy pasting many
definitions. My library helps prevent me from forgetting to apply
changes to all resources with the same type across my stacks.

I still need to add some unit testing I skipped while JFDI'ing, pretty
up the logging output, and release it to pypi, but it's what I use to
create and destroy my stacks now. I hope someone else ends up liking
it.

What's Next
===========

I think I want to try out monitoring with sensu (even though it's ruby,
bleh). Sounds a lot more interesting in Nagios, which is the only other
option that seems like a good idea. Along with that I plan with getting
a Soekris_ router to make having a VPN gateway easier/cooler. Physical
toys are pretty fun.

.. _Soekris: http://soekris.com/

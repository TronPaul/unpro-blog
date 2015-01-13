AWS Port Forwarding NAT Guide
#############################

:date: 2015-1-13 08:00
:category: Guide
:tags: aws, operations
:slug: port-forward-NAT-guide
:summary: How to create a port forwarding NAT for your private subnet

Motivation
==========

My current AWS set up uses port forwarding so that different services
(mumble, website, and a VPN) share the same IP address. AWS doesn't have
any guides that go into setting up a port forwarding NAT. When I was
setting up my VPC it wasn't obvious how I could set it up in AWS.

Assumptions
===========

This guide assumes:

* You have an AWS account
* You know how to launch instances
* You know some basic networking concepts

Creating Your VPCs
==================

Creating Your NAT Instance
==========================

Port Forwarding
===============



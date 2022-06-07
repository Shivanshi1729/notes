---
layout: default
title: PHP Session
parent: Web Development
---

# PHP Sessions

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## What is a session?

In general, session refers to a frame of communication between two medium. A PHP
session is used to store data on a server rather than the computer of the user.
Session identifiers or SID is a unique number which is used to identify every
user in a session based environment. The SID is used to link the user with his
information on the server like posts, emails etc.

## How are sessions better than cookies?

Although cookies are also used for storing user related data, they have serious
security issues because cookies are stored on the user’s computer and thus they
are open to attackers to easily modify the content of the cookie. Addition of
harmful data by the attackers in the cookie may result in the breakdown of the
application. Apart from that cookies affect the performance of a site since
cookies send the user data each time the user views a page.Every time the
browser requests a URL to the server, all the cookie data for that website is
automatically sent to the server within the request.

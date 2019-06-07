# Project 3

# Web Programming with Python and JavaScript


#Project Overview



Build  web application for handling a pizza restaurant’s online orders. Users will be able to browse the restaurant’s menu, add items to their cart, and submit their orders. Meanwhile, the restaurant owners will be able to add and update menu items, and view orders that have been placed.


# The project have 3 Apps


1. accounts App


Most of the functionality and models are built in here.
User Registration, login and Logout is implemented here.
Used Django forms to caputre user information.
orders and Purchase confirmation is implemented within the Accounts app to avoid having to import the user to other models and views.

2. orders App


Orders App works as a get way for index and a static file. No models created under orders App.


3. menu App


It include menu models and the views for those models.

Personal Touch 


1. Ability to import CSV and Excel format reports from orders and confirmation models.

2. Admin customization to filter results by date and Added columns on the Models' display in the admin dashboard for the site owner.


2. Stripe checkout gateway.

Summary


If the user have not checkout with Stripe yet, the order items will be reflected under orders having 'Unpaid Status.'

Once the user clicked checkout with stripe, the orders will be cleared and the data will reflect as confirmation with the status 'Confirmed'

#How to use the project

1. clone repo in github

2. cd into it and run pip install -r requirements.txt.

3. setup your your stripe account details  accounts.views and views/templates/menu.html

4. run django command to create superuser as python manage.py createsuper.

5. I can't wait to get started with final project... i will be building music streaming services like that of Amazon Studios.


Strip test card
https://stripe.com/docs/testing
4000000560000004

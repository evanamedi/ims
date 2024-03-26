# IMS (Inventory Management System)

## Objective

This was initially just a small project to reinforce working with databases, and OOP. However, I kept thinking of things to make it better, and what started out as just a basic terminal interface is now turning into a full stack web app. This is not intended for commercial use. I just like building stuff. I will document the entire process step by step and post it on this repo once it gets closer to being "finished". If you find any issues, or ways to improve it- let me know. Here is a few of the things it currently has, followed by some nice to haves:

### Current Implementations

-   MySql database set up for managing inventory (suppliers, products (inventory), customers, orders, sales)
-   Python business logic for interacting with the database. Was originally bloated In terms of redundant code, but now runs through a single interface. However, I am still tinkering with whether or not this approach is best. For the time being I enjoy how modular it is, and simple in terms of adding/maintaining logic.
-   RESTful and independent API using Flask. I was considering approaching this with the same interface design as the database logic. I decided against it for two reasons: First, I wanted to make sure each set of routes were truly independent of each other, and straight forward to add/maintain. And second, building on to that, my experience with API development is limited- so I wanted to reinforce what I was doing. There is some pattern of redundancy- but I would argue it's warranted, and makes sense in this case.
-   Client side webapp for manipulating inventory, with responsive and welcoming interface.
-   The web app is designed for overview, and root access for any changes that need to be made.

### Nice to have down the road

#### Things i'm currently working on

#### Some known issues

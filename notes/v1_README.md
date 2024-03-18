# Thoughts Regarding Different Parts of This Project

## Business Logic

currently have all of the basic business side logic written for reading, writing, updating, and deleting (only supliers/products atm of this writing). It generally works as it should but to be more robust it could use a few more things:

-   better logging
-   better error catching
-   possibly rethinking how it is implemented

my main area of concern is that it was not initially implemented in the best way- which is fine can i can certainly go back and refactor it. it is pretty much modular in terms of other aspects of this project- with the exception of 1 or 2 key points of the api routing. id like to make sure these two things are complexly separate before going forward so that i can refactor the logic without disrupting the api. concerns regarding the business logic:

-   repetition in code: each module of the logic pretty much has the same layout and i believe this could be refactored into one single module that can be called regardless of what table it is interacting with. so one interface for interacting with the database, and its implementation can change dynamically based on what operation- but more importantly, which table is being interacted with. this could significancy reduce code and ensure easier debugging.
-   possibly create a module that can be the delegator of issues between different interfaces. for example: there is an issue on the database side or business side, and an arbitrary error code (or i suppose ones currently existing) that could be sent up each layer of the chain to better relay to the user what is going on. the current implementation is not really working together.
-   immanently need unit testing. however, i believe a prior focus should be integrating the business logic as noted above. that way i can focus unit testing to a few main components that control the main logic- rather than the current setup of pretty much repeated code in each module of business logic
-   could possibly have each act of logic being implemented, appended to a dictionary, that then can be passed to a class module for interacting with the database

## API

could possibly do the same thing for the api as mentioned above about the business logic. regarding having one main interface for interaction instead of all the currently (generally) repeated code in each routing module.

i would also like to abstract away the variable names used for the api- to be a bit more distant from the ones being used in the database.

## GUI Design

yeah this is terrible right now, but its enough to work for now- this is probably be something i will work towards slowly, and closer to the end.

## Database

its okay. but one concern is the the attachment of table ids that are connected in other tables. for example: each product is assigned a supplier id that is attached to the supplier that provides the product. if a delete command is sent to the supplier table- once this supplier is deleted, its products in the product table will also be deleted. this is implemented intentionally. but i am not so sure if this really makes any sense. i may change it to still correlate- but not make it locked in as it currently is.

# Monty & Turner's Tie Emporium

## Code Institute Milestone Project 4

![Portfolio Mockup](markdown-files/readme-files/mockup.png)
[Click here to view the live project]()

- [M&T Tie Emporium](#monty--turners-tie-emporium)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [UX](#ux)
  - [Development Planes](#development-planes)
  - [Features](#features)
  - [Issues and Bugs](#issues-and-bugs)
  - [Technology Used](#technologies-used)
  - [Testing](#testing)
  - [Deployment](#deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

## Introduction

Welcome to my README for Monty & Turner's Tie Emporium, an excellent place to find a great selection of high quality ties. The purpose of this website is to allow new and existing customers to browse a range of ties in an intuitive way and easily find information regarding the ties. 

The customers will of course be able to purchase a tie and this will involve signing up and logging into their personal account. Ease of use is very important as a frustrated customer is less likely to make a purchase. The aim was to allow the purchase of a tie in as few steps as possible.

This was the fourth Milestone Projects as part of my course at the Code Institute. The main requirements were to make a full stack django project, with multiple apps, use of stripe payment, at least one form of validation, an authentication method, some frontend javascript and finally at least two custom django models.

---

## UX

### Demographics

The aim for me is to create a website that appeals to:

- New users
- Current users
- Store Owner

### User Stories

#### New Users

- As a new user I want to be able to browse relevant products
- As a new user I want to be able to contact the site owner
- As a new user I want to be able to sign up and create a personal account
- As a new user I want to be able to connect with the business via social sites

#### Current Users

- As a current user I want to be able view products as I did as a new user
- As a current user I want to be able to log in to my personal account and view my personal data
- As a current user I want to be able to securely edit my data
- As a current user I want to be able to add products I am interested in to my cart for later
- As a current user I want to be able to edit the items in my cart by either removing them or changing the quantity
- As a current user I want to be able to securely checkout the items in my cart to complete an order
- As a current user I want an order confirmation sent to my email to give me details of that order

#### Store Owner

- As a store owner, I want to be able to login to a secure store owner account
- As a store owner, I want to be able to add new products to my store
- As a store owner, I want to be able to edit and remove unwanted products
- As a store owner, I want to be able to edit some of the content of the site

---

## Development Planes



#### Strategy

To design a site that fits the users needs, the following development planes were consulted to assist with answering the user stories.

- roles

  - Current users
  - New Users


- Demographic
  - Interested in menswear
  - Adults
  - Seeking high quality men's accessories
  - Western demographic, focus on united kingdom

- Psychographic
  - Lifestyles
    - Potential office workers
    - Users who frequently adpot formal attire

- Personality and Attitudes 
  - Professionals
  - Attention to detail
  - Social

- Values
  - Focus on maintaining smart appearance
  - Appreciates high quality 
  - Appreciates wide choice of selective items

This website needs to enable the user to:

- Create an account and login
- Purchase a tie or multiple ties
- Edit and save user info (email, physical address)
- Contact the site owner
- visit site social links

This website needs to enable the owner to:

- Display available products
- Provide a point of contact
- Provide information about the site


With this in mind I have produced a short diagram representing the viability of elements versus importance within the site.

<details>

<summary>Viability chart</summary>

![viability](markdown-files/readme-files/tie_shop_viability.jpg)

</details>

[Back to top](#monty--turners-tie-emporium)

---

### Scope

Based on the requirements of the Strategy plane, I have identified two categories.

- Content Requirements:
  - Products (ties)
    - categories will be colour and material 
    - images of each product
  - Contact form for emailing site owner
  - Login/sign up form
  - User dashboard 
    - Edit user email and physical address
    - View past orders
    - User wishlist
- Function Requirements:
  - Users can search for key words via a search bar
  - Users can select a category of ties
    -Categories will be colour and material
  - Sign in page and sign up page
  - User dashboard
    - Edit user data
    - User wishlist (add and remove products)
  - Cart for items selected to buy
    - Edit quantity and remove items from cart
    - Complete checkout from cart
  - Contact site owner via form
  - Edit/Add/Delete products



---

### Structure

Based on the information so far, 

The intended path will be as follows:

#### Path for first visit account creation and sign in

 <details>

<summary>Expand for map</summary>

![Map](markdown-files/readme-files/structure_map_2.jpg)

</details>
 

#### Path for finding and adding product to basket

 <details>

<summary>Expand for map</summary>

![Map](markdown-files/readme-files/structure_map_1.jpg)

</details>


 #### Path for purchasing an item

<details>

<summary>Expand for map</summary>

![Map](markdown-files/readme-files/structure_map_3.jpg)

</details>


---

### Skeleton

Wireframes were produced using balsamiq. These will showcase the site as intended on mobile and desktop. I created these wireframes at the beginning of the project as an approximate guideline on positioning of elements on the pages. 
I knew that a lot of pages would be very similar in their layout and so generic pages were created to accomodate those designs.

<details>

<summary>Home Page</summary>

![home](markdown-files/wireframe_1.png)

</details>

<details>

<summary>Shop all</summary>

![shop](markdown-files/wireframe_2.png)

</details>

<details>

<summary>Product info</summary>

![shop](markdown-files/wireframe_3.png)

</details>

<details>

<summary>Form</summary>

![form](markdown-files/wireframe_4.png)

</details>


---

### Surface

The colour palette will consist of two shades of green for the navigation bar and modals, white for text over green elements and a shade of blue for buttons.
This is to differentiate the buttons as active easily and enable easy navigation through the site.

I believe a simple colour palette is appropriate for this site, please see below the palette:

<details>
<summary>Colour Palette</summary>

![Colour](markdown-files/readme-files/Colours.png)

</details>

### Typography

The typography I will use will be Playfair Display, with serif as a backup. Its a formal font thats easy to read but is unique enough to add some flair to the website. I chose this font to be displayed sitewide as it will maintain a consistent look while also help build character for the style elements.

### Imagery



[Back to top](#monty--turners-tie-emporium)

---

### Information Architecture

### Database

Many models were created for this website, see below the content of the models:

#### Data Models


#### `User Profile - Profiles app`
- Data for storing user profiles

| Name      | Database Key  | Field Type | Type Validation |
|--------------|--------------|--------------|--------------|
| User    | user | OneToOneField(User) | on_delete=models.CASCADE |
| Phone Number | default_phone_number | Charfield | max_length=20,<br /> null=True,<br /> blank=True|
| Country | default_country | CountryField | blank_label='Country',<br /> null=True,<br /> blank=True|
| Postcode | default_postcode | Charfield | max_length=20,<br /> null=True,<br /> blank=True|
| Town Or City | default_town_or_city | Charfield | max_length=40,<br /> null=True,<br /> blank=True|
| Street Address 1 | default_street_address1 | Charfield | max_length=80,<br /> null=True,<br /> blank=True|
| Street Address 2 | default_street_address2 | Charfield | max_length=80,<br /> null=True,<br /> blank=True|
| County | default_county | Charfield | max_length=80,<br /> null=True,<br /> blank=True|

#### `Order - Checkout app`

- Data for storing orders to be presented to users and site owner

| Name      | Database Key  | Field Type | Type Validation |
|--------------|--------------|--------------|--------------|
| Order Number | order_number | Charfield | max_length=32,<br /> null=False,<br /> editable=False|
| User | user_profile | ForeignKey(UserProfile) | null=True,<br /> blank=True,<br/> on_delete=models.SET_NULL,<br />r elated='orders' |
| Full Name | full_name | Charfield | max_length=50,<br /> null=False,<br /> blank=False|
| Email Address | email | EmailField | max_length=254,<br /> null=False,<br/> blank=False| 
| Phone Number | phone_number | Charfield | max_length=20,<br /> null=False,<br /> blank=False|
| Country | country | CountryField | blank_label='Country*',<br /> null=False,<br /> blank=False|
| Postcode | postcode | Charfield | max_length=40,<br /> null=False,<br /> blank=False|
| Town Or City | town_or_city | Charfield | max_length=40,<br /> null=False,<br /> blank=False|
| Street Address 1 | street_address1 | Charfield | max_length=80,<br />null=False,<br /> blank=False|
| Street Address 2 | street_address2 | Charfield | max_length=80,<br /> null=True,<br /> blank=True|
| County | county | Charfield | max_length=80,<br /> null=False,<br /> blank=False|
| Date | date | DateField | auto_now_add=True |
| Delivery Cost | delivery_cost | DecimalField | max_digits=6,<br /> decimal_places=2,<br /> null=False,<br /> default=0|
| Order Total | order_total | DecimalField | max_digits=10,<br /> decimal_places=2,<br /> null=False,<br /> default=0|
| Grand Total | grand_total | DecimalField | max_digits=10,<br /> decimal_places=2,<br /> null=False,<br /> default=0|
| Original Cart | original_cart | TextField | null=False,<br /> blank=False,<br /> default=''|
| Stripe Payment Intent ID | stripe_pid | CharField | max_length=254,<br /> null=False,<br /> blank=False,<br /> default=''|

#### `Order Line Item - Checkout app`

| Name      | Database Key  | Field Type | Type Validation |
|--------------|--------------|--------------|--------------|
| Order | order | ForeignKey(Order) | null=False,<br /> blank=False,<br/> on_delete=models.CASCADE,<br /> related_name='lineitems' |
| Product | product | ForeignKey(Product) | null=False,<br /> blank=False,<br/> on_delete=models.CASCADE |
| Quantity | quantity | IntegerField | null=False,<br /> blank=False,<br/> default=0 |
| Lineitem Total | lineitem_total | DecimalField | max_digits=6,<br/> decimal_places=2,<br/> null=False,<br /> blank=False,<br/> editable=False |

#### `Product - Products app`

- Data for building products and ManyToMany field for wishlist at end of model

| Name      | Database Key  | Field Type | Type Validation |
|--------------|--------------|--------------|--------------|
| Name | name | Charfield | max_length=90 |
| Price | price | DecimalField| default=0, decimal_places=2, max_digits=5 |
| Category | category | ForeignKey | Category, on_delete=models.CASCADE, default=1 |
| Colour | colour | ForeignKey| Colour, on_delete=models.CASCADE, default='' |
| Description | description | TextField | max_length=750, default='', blank=True, null=True |
| Image | image | ImageField| upload_to='uploads/product/' |
| Image 2 | image_2 | ImageField| upload_to='uploads/product/' |
| Product ID | product_id | CharField| max_length=10, default='' |
| SKU | sku | CharField | max_length=254, null=True, blank=True |
| Favourited By | favourited_by | ManyToManyField | UserProfile, related_name='user_wishlist', blank=True |

#### `Category - Products app`

- Category key (tie material) for filtering shop page

| Name      | Database Key  | Field Type | Type Validation |
|--------------|--------------|--------------|--------------|
| Name | name | Charfield | max_length=40 |
| Friendly Name | friendly_name | CharField| max_length=254, null=True, blank=True |

#### `Colour - Products app`

 - Colour key for filtering shop page

| Name      | Database Key  | Field Type | Type Validation |
|--------------|--------------|--------------|--------------|
| Name | name | Charfield | max_length=20 |

#### `Subject - Info app`

- FAQ subject to be presented and edited/new entries added or deleted

| Name      | Database Key  | Field Type | Type Validation |
|--------------|--------------|--------------|--------------|
| Subject | subject | Charfield | max_length=100 |
| Friendly Name | friendly_name | CharField| max_length=254, null=True, blank=True |

#### `Question - Info app`

- Questions and answers for the FAQ

| Name      | Database Key  | Field Type | Type Validation |
|--------------|--------------|--------------|--------------|
| Subject | subject | ForeignKey | Subject, on_delete=models.CASCADE, default='' |
| Question | question | CharField| max_length=600 |
| Answer | answer | TextField| () |


[Back to top](#monty--turners-tie-emporium)

---

## Features

The website features a set of consistent and intuitive functions.


### Sign Up

Sign up is available on the home page. From the link in the navigation bar, you can find the form to enter a new username, email and password. From there you will be able to login to explore the other functions.


---

### Sign In

Signing in will give the user access to saving their details for future orders, updating details, viewing items in their wishlist and viewing their past orders. Many features on the site are only available when logged in.

---

### Logout

Logging out is confirmed with a seperate page asking if you are ready to sign out. The logout button is found on the user dashboard.


---

### Add product to cart

After finding a product that the user likes, they can add this product to the cart. A quantity can be selected, up to 10 per tie per customer. Once added to the cart, they can be seen again in the cart, and quantity can also be changed.

---

### Remove product from cart

Of course it is essential to be able to remove items from the cart, and this is done on the cart page. A message is displayed to let the user know that the item has been removed.

---

### Checkout

Checkout is a page that completes the order using stripe payment systems. After an order is complete, an email confirmation is sent to the user.

---


### Home page features

From the home page features a banner image which links to the store page displaying all products.
The home page is where the user will first encounter the navigation and footer, where the user can access the sign in / sign up, user dashboard and cart on navigation, and FAQ, contact and about pages on the footer.

The home page also features a search bar that is available sitewide for easy searching for products.

---

### User page

User pages, also known as the user dashboard, is where the user is presented with their details which can be updated, their user wishlist and their past orders. Users can click through to view their wishlist and remove items from said list.
Users can also view their order history.

---

### Owner features

On the user dashboard, if logged in as super user, the links to the add FAQ and add product pages appear. From here the site owner will be presented with forms to fill to complete these actions.

On product information pages the options to delete and edit products will appear for the site owner.
Edit FaQ buttons will appear next to FaQ's.

---

### Site modals

On pages where the site owner can remove content from the site, modals have been installed as a verification to ensure that the user wants to complete this irreversible act.

---

### Contact page

The contact page enables the user to contact the site owner via EmailJs javascript. On completing the form, they will be redirected to a thank you page.

---

### FAQ

The FAQ page is a simple question and answer section, but is created using a model.
The data is editable by the site owner, and new entries can also be added.

--- 
### Shop all

Shop all is where all products will be displayed. 
From there, users can select a product to view the full info for and filter the page by the material category and by the colour category.

---

### Product info

Once a product has been clicked, user will be presented with all of the information regarding this product, as well as the options to add the product to their cart. The quantity of the product can also be selected at this stage.

---

### Future features

Due to time constraints I was unable to implement the following functions, however the would make a nice addition to the website:

- FAQ questions tailored to users - the FAQ page is built using a model, so could be customised to present different questions depending on the users location for shipping, if they were authenticated, if they had orders in progress or if they had an order in progess. I feel that this part of the site has a lot of potential that I would have loved to explore if I had more time.
- Pagination -  the product shop all page could use pagination for when more products were added.
- Filter by price and alphabet for the shop all page. Although I added category and colour filters, price and alphabetical filters would have also been desirable.

[Back to top](#monty--turners-tie-emporium)

---

## Issues and Bugs

### -- Image format not recognised
At many points during the build, I added images with various types of file to the project. At some points the images would not load through the static folder, and with some research I found that I had to be very carefult with the file types I was using.

### -- Modal confirm delete issue

When iterating through the FAQ model in the FAQ page, I found that the modal for confirming the deletion of the FAQ entries was not being assigned to the correct entry and would instead always delete the top entry. For FAQ I worked around this by adding the delete button to the edit FAQ page.

I came accross this issue again, however, when creating the wishlist. I found that I was able to fix this issue by applying the product.id into the modal class using jinja, and this meant that individual modals were being assigned to their correct entry, and when the modal confirmed deletion, the correct entry was deleted.

### -- Building wishlist
I first attempted to build a wishlist with a seperate model, containing two foreign keys. I found it difficult to get the data I wanted from this, partly because of my own naming of the fields. I did a lot of research and eventually found that the best approach was to use a ManyToMany field on an existing model. This worked in a much more elegant way than my first approach.

When creating the wishlist I was unsure of where to build the pages, as it could have been made in the products app or profile app. I am happy with it in the profile app but I did need to create an additional view for linking back to the product info page.

---

## Technologies Used

### Main Languages Used

- HTML5
- CSS
- JavaScript
- Python
- Jinja templating

### Frameworks, Libraries and Programs

- Bootstrap was used to implement the responsiveness of the site, using bootstrap classes.
- jQuery was used to simplify the JavaScript code used.
- Google fonts was used to import the fonts.
- Jinja templating language was used to simplify and display backend data.
- EmailJs was used to implement the email contact form.
- Crispy Forms
- Pillow
- Authy
- Stripe payment

---

## Testing

Please view full testing document [here]()

---

## Deployment

---
The site was deployed using GitHub and is hosted on Heroku and was deployed as below -

### How to clone the repository

 - Go to the repository at https://github.com/JPBiddle/Tie-Shop on GitHub.
 - Click on the code button and copy the https URL under Clone.
 - Open a terminal on GitBash and locate the folder you want to store the cloned repository.
 - In the terminal type git clone, paste the URL of the cloned repository after it then press Enter.
 - Successfully cloned!

 ### Deploying to Heroku

 - Sign into your heroku account.
 - Select "New" > "Create New App".
 - Create a unique app name and select the server region closest to you.
 - Select "Create App".
 - In the new app, select "Settings" and Select "Reveal Config Vars".
 - Enter your environment variables.
 - Create the Procfile in the terminal: echo web: python app.py > Procfile.
 - Create the requirements.txt file in the terminal: pip3 install -r requirements.txt.

 You will need to connect he GitHub repository to your Heroku app:

  - Go to the app in Heroku and locate the deploy tab.
  - Under "connect to GitHub" search for your repository and click "Connect".
  - To update the app every time you commit to GitHub, select "Automatic Deployment".

### Amazon web services


---

### Setting up Datatbase

- Sign up for ElephantSQL and create a new instance.
- Give the database a meaningful name (your project name for example).
- Use the Tiny Turtle plan.
- Select your nearest region and click Review.
- Select Create Instance.
- Go into your database instance, copy the URL of the database and add it to the DATABASE_URL Config variable in Heroku.
- In your terminal, enter the following to install apps to connect to your database:
  - "pip3 install dj_database_url==0.5.0 psycopg2
  pip freeze > requirements.txt"
- In the settings.py file add 
  - "import os
  import dj_database_url"
- Add the following (TEMPORARILY) to settings.py with your DATABASE URL copied above: 
  - "DATABASES = {
     'default': dj_database_url.parse('your-database-url-here')
  }"
- In the terminal add the following:
  - "python3 manage.py showmigrations
  python3 manage.py migrate
  python3 manage.py loaddata categories
  python3 manage.py loaddata products"
- Create a superuser in the terminal by adding a username and password after entering python3 manage.py createsuperuser.
- Replace the (TEMPORARILY) DATABSES code from above with:
  - "DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
     }
 }"
---


## Credits

---
- Images for products were gathered from https://brunaticomo.com/.
- Credits for assistance in building my code is referenced on relevant code pages.

---

## Acknowledgements

Developer would like to thank the following -

  - Friends and family for their feedback during development.
  - My mentor, tutor Koko, for her help with ideas for the project functions.
  - The Code Institute slack community.
---


[Back to top](#monty--turners-tie-emporium)

---
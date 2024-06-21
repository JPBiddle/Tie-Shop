# Monty & Turner's Tie Emporium

## Code Institute Milestone Project 4

![Portfolio Mockup]()
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

Wireframes were produced using balsamiq. These will showcase the site as intended on mobile and desktop.

<!-- <details>

<summary>Wireframes</summary>

<details> -->

<summary>Home</summary>

![Home]()


---

### Surface


<details>
<summary>Colour Palette</summary>

![viability]()

</details>

### Typography

The typography I will use will be 

### Imagery



[Back to top](#monty--turners-tie-emporium)

---

### Information Architecture

#### Database

- 

#### Data Models


#### `User Profile - Profiles app`

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

| Name      | Database Key  | Field Type | Type Validation |
|--------------|--------------|--------------|--------------|
| Name | name | Charfield | max_length=40 |
| Friendly Name | friendly_name | CharField| max_length=254, null=True, blank=True |

#### `Category - Products app`

| Name      | Database Key  | Field Type | Type Validation |
|--------------|--------------|--------------|--------------|
| Name | name | Charfield | max_length=20 |

#### `Subject - Info app`

| Name      | Database Key  | Field Type | Type Validation |
|--------------|--------------|--------------|--------------|
| Subject | subject | Charfield | max_length=100 |
| Friendly Name | friendly_name | CharField| max_length=254, null=True, blank=True |

#### `Question - Info app`

| Name      | Database Key  | Field Type | Type Validation |
|--------------|--------------|--------------|--------------|
| Subject | subject | ForeignKey | Subject, on_delete=models.CASCADE, default='' |
| Question | question | CharField| max_length=600 |
| Answer | answer | TextField| () |


[Back to top](#monty--turners-tie-emporium)

---

## Features

The website features
---

### Sign Up




---

### Sign In



---

### Logout



---

### Add product to cart



---

### Remove product from cart

---

### Checkout
---

### Home page features

From the home page, 

---

### User page

---

### Future features

Due to time constraints I was unable to implement the following functions, however the would make a nice addition to the website:

- 

[Back to top](#monty--turners-tie-emporium)

---

## Issues and Bugs

### --
Issue with added to cart javascript and python redirect not allowing user to read 'Added to bag' for long enough.



### --




### --



---

## Technologies Used

### Main Languages Used

- HTML5
- CSS


### Frameworks, Libraries and Programs


---

## Testing

Please view full testing document [here]()

---

## Deployment

---



### Deploying

---



---

## Credits

---


---

## Acknowledgements

---


[Back to top](#monty--turners-tie-emporium)

---
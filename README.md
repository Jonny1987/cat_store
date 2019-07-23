# cat_store

This is a demo website to showcase what I have learned with Django and the Django REST Framework.

Site consists of a homepage which displays the products, although there is no way to order a product yet.

There is also a product request feature where the customer can request that the store orders a product that it doesn't yet have. 
I added this feature because I wanted to use django ModelForm and a shopping cart wouldn't give me an opportunity to do that.

I have also added authentication and resticted creating, updating, and deleting of products to admin users, and of 
product_requests to the owner (creator) of that product_request.

I have made use of viewsets and the Router class when creating API endpoints.

I used class based views DetailView and ListView for the home page (list of products) and product detail view.

I added tests for the home page and product detail view, but have not yet added tests for the product_request page or the api.

# Cuboid

Brief description or introduction to your project.

## Table of Contents

- [Installation](#installation)
- [Live Demo](#live)
- [APIs](#Apis)


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/DhruvDutta/cuboid.git
2. Install requirements
   ```bash
   pip install -r requirements.txt
3. run migrations
   ```bash
   python manage.py makemigrations
   python manage.py migrate

4. Run Server
   ```bash
   python manage.py runserver

## Live
1. Go to: [click here](https://dhruvdutta1802.pythonanywhere.com/)
## Apis
1. Get Token:
   ```bash
   curl --location 'https://dhruvdutta1802.pythonanywhere.com/api/token/' \
   --header 'Content-Type: application/x-www-form-urlencoded' \
   --data-urlencode 'username=dhruv' \
   --data-urlencode 'password=Dhruvmi777'
2. Create:
   ```bash
   curl --location 'https://dhruvdutta1802.pythonanywhere.com/create/' \
   --header 'Authorization: Token yourtoken' \
   --form 'length="3"' \
   --form 'width="10"' \
   --form 'height="3"'
3. Update:
   ```bash
   curl --location --request PUT 'https://dhruvdutta1802.pythonanywhere.com/update/1/' \
   --header 'Authorization: Token yourtoken' \
   --form 'length="3"' \
   --form 'width="2.5"' \
   --form 'height="2"'
4. List:
   ```bash
   curl --location 'https://dhruvdutta1802.pythonanywhere.com/list_boxes/?area__gt=6' \
   --header 'Authorization: Token yourtoken'
5. My Boxes List:
   ```bash
   curl --location 'https://dhruvdutta1802.pythonanywhere.com/my_boxes/?volume__gt=50' \
   --header 'Authorization: Token yourtoken'
6. Delete Box:
   ```bash
   curl --location --request DELETE 'https://dhruvdutta1802.pythonanywhere.com/delete_box/1/' \
   --header 'Authorization: Token 94d7331cde27a8b66fbee2981b3b19a55963b143'
   

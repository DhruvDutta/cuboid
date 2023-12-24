# Cuboid

Brief description or introduction to your project.

## Table of Contents

- [Installation](#installation)
- [Live Demo](#live)


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
1. Create:
   ```bash
   curl --location 'https://dhruvdutta1802.pythonanywhere.com/create/' \
   --header 'Authorization: Token yourtoken' \
   --form 'length="3"' \
   --form 'breadth="10"' \
   --form 'height="3"'
2. Update:
   ```bash
   curl --location --request PUT 'https://dhruvdutta1802.pythonanywhere.com/update/1/' \
   --header 'Authorization: Token yourtoken' \
   --form 'length="3"' \
   --form 'breadth="2.5"' \
   --form 'height="2"'
3. list:
   ```bash
   curl --location 'https://dhruvdutta1802.pythonanywhere.com/list_boxes/?area__gt=6' \
   --header 'Authorization: Token yourtoken'
4. My Boxes List:
   ```bash
   curl --location 'https://dhruvdutta1802.pythonanywhere.com/my_boxes/?volume__gt=50' \
   --header 'Authorization: Token yourtoken'
5. Delete Box:
   ```bash
   curl --location --request DELETE 'https://dhruvdutta1802.pythonanywhere.com/delete_box/1/' \
   --header 'Authorization: Token 94d7331cde27a8b66fbee2981b3b19a55963b143'
   

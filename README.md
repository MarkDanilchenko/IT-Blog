## Description

This is a project 'IT_Blog' using:

- MySQL;
- Django Rest Framework;
- NuxtJS (Nuxt2);
- Bootstrap;
- Webpack;
- Docker;
- CSS/SCSS/HTML.

## Launch instructions

1. Clone repository to your local folder;
2. Copy dev.env to .env file in the same root directory:

    `cp dev.env .env`

3. Open and follow the instructions properly in the new created .env file. *EMAIL_HOST_USER* and *EMAIL_HOST_PASSWORD* for Email sending *are expiremental*;
4. For this step you should already have installed Docker and docker-compose on your PC:

- make sure You are in project folder:

  `cd '.../project_folder'`

- Run docker-compose:

  `docker-compose up --build`

- Installation can take some time, it depends on your PC resources;
- After the installation is completed, the client-server will start automatically on 0.0.0.0:3000;
- Open app using <http://0.0.0.0:3000/> in your browser;

5. The superuser (admin) has been already created;

- You can login under current superuser using standart credentials:

  `login: admin; pass: admin`

- For password change use:

   `cd '.../project_folder' && python3 manage.py changepassword admin`

- Or You can manually create superuser for Your own purpose:

   `cd '.../project_folder' && python3 manage.py createsuperuser`

- Note, that:
  - Add/edit/delete posts only via admin-panel (Users can not to do that);
  - Add comments only for registered and authenticated Users.

6. Note that DataBase in project - MySQL;
7. To stop the server: `Ctrl+C`;
8. To completely remove all created docker containers, images and volumes:

   `docker-compose down --volumes`.

**p.s.:**

--> **error.log**: contains **backend-server error messages** that may cause the application to be interrupted or lead to undesirable results.

--> **error.log** is available in root folder after successfull app launch.

### Screenshots

1. *Main page (white & dark themes)*

![Main page(white theme)](screenshots/ScrShot_1.png)
![Main page(dark theme)](screenshots/ScrShot_2.png)
  
2. *Sign Up form*

<div align="center">
  <img src="screenshots/ScrShot_3.png" width="100%" height="100%" alt='Sign up form'>
</div>

3. *Forms validation in real time input*

![Sign In form](screenshots/ScrShot_4.png)

4. *Sign In form*

![Post details](screenshots/ScrShot_5.png)

5. *Main page (authenticated User)*
![Main page (authenticated User)](screenshots/ScrShot_6.png)

6. *Feedback page*
![Feedback page](screenshots/ScrShot_7.png)

7. *Search result page*
![Search result page](screenshots/ScrShot_8.png)

8. *Tags navigation page*
![Tags navigation page](screenshots/ScrShot_9.png)

9. *Comments block for authenticated and not authenticated Users*

![Comments block - Auth. Users](screenshots/ScrShot_10.png)
![Comments block - Not Auth. Users](screenshots/ScrShot_11.png)

10. *Sign Out page*

![Sign Out page](screenshots/ScrShot_12.png)

11. *Mobile look like*

<div align="center">
  <img src="screenshots/ScrShot_13.png" width="50%" height="50%" alt='Mobile look 1'>
  <img src="screenshots/ScrShot_14.png" width="50%" height="50%" alt='Mobile look 2'>
  <img src="screenshots/ScrShot_15.png" width="50%" height="50%" alt='Mobile look 3'>
  <img src="screenshots/ScrShot_16.png" width="50%" height="50%" alt='Mobile look 4'>
  <img src="screenshots/ScrShot_17.png" width="50%" height="50%" alt='Mobile look 5'>
</div>

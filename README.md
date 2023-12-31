## Description

This is a Django test project using MySQL, DRF, NuxtJS, Bootstrap, Webpack and Docker.

## Launch instructions

1. Clone repository to your local folder;
2. Copy dev.env to .env file: `cp dev.env .env`;
3. Open and follow the instructions properly in the new created .env file. Note, that for the all functions You should fill all fields;
4. For this step you should already have installed Docker and docker-compose on your PC:

- make sure You are in project folder: `cd '.../project_folder'`;
- Run docker-compose: `docker-compose up --build`;
- Installation can take some time, it depends on your PC resources;
- After the installation is completed, the server will start automatically on 0.0.0.0:8900;
- Open app using <http://0.0.0.0:8900/> in your browser;

5. The superuser has been already created;

- You can login under current superuser using standart credentials: `login: admin; pass: admin`;
- For password change use: `cd '.../project_folder' && python3 manage.py changepassword admin`;
- Or You can manually create superuser for Your own purpose: `cd '.../project_folder' && python3 manage.py createsuperuser`;
- Note, that:
  - Add/edit/delete posts only via admin-panel;
  - Add comments only for registered Users.

6. Note that DataBase - MySQL;
7. To stop the server: `Ctrl+C`;
8. To completely remove all created docker containers, images and volumes: `docker-compose down --volumes`.

**p.s.:**

--> error.log <-- : contains error messages that may cause the application to be interrupted or lead to undesirable results.
Available in root folder after successfull app launch.

### Screenshots

1. *Main page (white & dark themes)*

![Main page(white theme)](screenshots/ScrShot_1.png)
![Main page(dark theme)](screenshots/ScrShot_2.png)
  
2. *Mobile look page*

<div align="center">
  <img src="screenshots/ScrShot_3.png" width="50%" height="80%">
</div>

3. *Sign In/Out forms*

![Sign In form](screenshots/ScrShot_4.png)

4. *Post details*

![Post details](screenshots/ScrShot_5.png)

5. *Side bar with related posts*

<div align="center">
  <img src="screenshots/ScrShot_6.png" width="50%" height="80%">
</div>

6. *Comments block*

![Comments block](screenshots/ScrShot_7.png)

7. *Tags navigation*

![Tags navigation](screenshots/ScrShot_8.png)

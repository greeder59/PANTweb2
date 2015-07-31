# Web site for Portland Area N-trak.
Impementing the new PANT web site with Django.

## 14 July 2015
The first real commit with actual work.
- The project and the pant app are created.
- URLs.py exist and are updated in both the project and app directories.
- Views are created. But most of them are stubbed off.
- Base.html and index.html are created and serve up properly.
- index_full.html is available in the pant/templates directory. It doesn't do anything. But it is there as an HTML5 page that the rest of the project is based on. It may not properly reference it's css file.
- static files for the django app are handled.
- An initial database model is created and the admin interface can update the database.

## 30 July 2015
Commit number 2
- The index page template and view are working and retrieve staff announcements from the database.
- The Links page template and view are implemented and display links from the data base.
- The directions page template and view are implemented and display a Google map.
- Contact Us page template, view and form are implemented. Although the view needs some tweeking.
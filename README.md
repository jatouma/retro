# final-project
I've implemented the retro board as I mentioned in my outline.
I use python (with Django)
I use Javascript in actions.js, where I use AJAX to send a request to mark an action item complete, and
instantly delete the action item from the incomplete list, and add it to the complete list (no need for a refresh)
important files:
views.py has all the views and models.py has the models
admin.py has the admin models. the BoardAdmin ModelAdmin has inlines where you can edit all posts in a particular sprint.
submit.html to submit new comments. Submitting anonymously drops the user object before creating a new post.
login.html for login (I ended up using Django's built in 
index.html for new user registration
home.html for the latest retro board, and an export button to export that board (to simplified text)
actions.html for a view of all action items, incomplete and complete. You can mark action items complete
actions.js, the js behind the functionality for marking action items complete.
base.html for the base html file (all other html files extend it)
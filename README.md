# Mooviest

Mooviest is movie recommendation platform open to use by anyone that takes into account all the movies you've seen and your emotions and context. Quickly start marking the movies you've seen, want to see, or your favourites to enjoy Mooviest's intelligent and personalised recommendations ASAP.

You can also:
  - Receive recommendations based on your profile and even include the profile of others (girlfriend, boyfriend, group of friends, ...)
  - Check out movie ratings from top sites like IMDb, Rotten Tomatoes, FilmAffinity, etc. and get a global view of them with an average.
  - Compare movies side-by-side to choose between 2 o 3 three movies.
  - Tag movies based on the emotions they made you feel so we can recommend you other movies based on the way you feel and your context at that moment.


### Version
0.0.1


### Tech
Mooviest uses a number of open source projects to work properly:

* [Python] - a programming language that lets you work quickly and integrate systems more effectively.
* [Django] - a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
* [PostgreSQL] - an advanced open source database
* [Twitter Bootstrap] - great UI boilerplate for modern web apps
* [jQuery] - duh


### Installation
Mooviest requires [Python] v3+ to run.

First clone the repository:
```sh
$ git clone https://github.com/JoseAntpr/mooviest.git
$ cd mooviest
```

Install [Gitflow] to make use of the different branches:
```sh
# macOS
$ brew install git-flow
# Linux
$ sudo apt-get install git-flow
```

You need virtualenv installed to work in a virtual environment:
```sh
$ pip install virtualenv
# Create virtual environment
$ virtualenv venv
# Activate virtual environment
$ source venv/bin/activate
# Install the required Python packages
$ virtualenv install -r requirements.txt
```
Optional commands for virtualenv:
```sh
# Disable Python virtualenv
$ deactivate
# Add a requirement to the virtualenv requirements
$ pip freeze > requirements.txt
```

You need PostgreSQL database installed:
```sh
# macOS
$ brew install postgresql
# Linux
$ sudo apt-get install postgresql
# Create the database (as root)
$ createdb mooviest
$ createuser -P
# Activate the PostrgreSQL CLI to grant privileges to the user root
$ psql
>> GRANT ALL PRIVILEGES ON DATABASE mooviest TO root;
```

### settings.py
We can't include the settings.py file in the repo because it contains important information like user information and passwords. Instead there is a template.settings.py which acts as a template in which you'll have to modify the database section with your password (and user if you haven't used root):
```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mooviest',
        'USER': 'root',
        'PASSWORD': '********',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```


License
----
MIT


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [Python]: <https://www.python.org/>
   [PostgreSQL]: <https://www.postgresql.org/>
   [Django]: <https://www.djangoproject.com/>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [Gitflow]: <http://danielkummer.github.io/git-flow-cheatsheet/>

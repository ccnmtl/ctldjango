`ctldjango` is a standard Django project template tuned to
implement CTL specific functionality and configuration.

## What's Included

[![Greenkeeper badge](https://badges.greenkeeper.io/ccnmtl/ctldjango.svg)](https://greenkeeper.io/)

* Default to Python3
* Django Wind (a Django bridge to Columbia's central auth service -
  http://www.jasig.org/cas/deployments/columbia-university)
  is included and configured by default so our apps can use WIND
  for auth automatically. Ie, anyone with a Columbia UNI by
  default will have an account. The CCNMTL developer UNIs are
  automatically set up as superusers, and the group affil that
  CCNMTL staff all have gets automatically mapped to staff. These
  are generally useful defaults for us.
* virtualenv and pip setup
* a nice Makefile for common build, test, and run tasks
* settings split for dev/prod/staging
* gunicorn configuration
* media dirs for dev/prod/staging configured
* `/stats/` page wired up to display basic traffic stats for the app
* 'main' app with templated index view wired up and ready to go
* jQuery included
* base templates included
* database defaulted to postgresql
* timezone set
* `flake8` (http://pypi.python.org/pypi/flake8), `bandit` (https://pypi.org/project/bandit/) and `eslint` (https://eslint.org/) installed and configured for code linting
* layout based on twitter bootstrap4
* Google Analytics ready to go
* See [ccnmtlsettings](https://github.com/ccnmtl/ccnmtlsettings) for more information on CTL settings setup.


## How to use


### Generate the project
```bash
$ django-admin.py startproject \
  --template=https://github.com/ccnmtl/ctldjango/archive/master.zip \
  --name=Dockerfile,Makefile,package.json,stats.html \
  --extension=py,yml \
  project_name
```

`project_name` should be a python module name (ie, lowercase,
no punctuation, etc). It will create a directory called
`project_name` that has a django project in it.

### Setup hidden files
* `mv travis.yml .travis.yml` to activate Travis CI integration
* `mv gitignore .gitignore` to configure git ignore
* `mv eslintrc.js .eslintrc.js` to configure eslint
* `mv bandit .bandit` to configure bandit security linting

### Check it in
* Check the project into version control now.

### Build
We use containment for django, with virtualenv:

    $ make

That will create a `ve` directory which contains a virtualenv and has
had all the libraries specified in the `requirements.txt` file
installed into it (this includes django itself). The `ve` directory
should never be checked in. If you need
other libraries for your application, update `requirements.txt` then re-run `make`.

Keep in mind that with virtualenv, there's no need to `activate` an
environment. Instead, a ve has a `bin` directory which contains a
python executable. If you use that instead of the system python
executable, it uses the libraries in that virtualenv.

ctldjango assumes that your project will use a postgresql database
with the same name as your project. So, for our example, you would
then do:

    $ createdb myprojectname

and it is all set to use it:

    $ make migrate

will install the tables that django needs for it's common apps (sites,
sessions, admin, flatpages, etc).

Tests should pass out of the box:

    $ make test

They can be run via Jenkins as well and generate the right reports in
a `reports` directory (which you will want to gitignore).

    $ make jenkins

Your application is ready to run now:

    $ make runserver

will start a server on `http://localhost:8000/`. The admin app should
be accessible (via a user account created with 
`manage.py createsuperuser`, or via WIND to tlc users (or ones specified 
in the `WIND_SUPERUSER_MAPPER_GROUPS` list in `settings_shared.py`). 
So go ahead and login to `http://localhost:8000/admin/`

Even without any application specific code, `flatpages` is included so
you can put content on the web right away.

From this point out, it's basic django development. You'll probably
want to do a `./manage.py startapp` to create your own application
within the project and so on.

### A few loose ends
* Update the README.md
* Update the `Project Name` string in `base.html` with your application's display name.

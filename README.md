

# learn

learn is a _e-learning platform, to enable instructors to create courses online and train students, students may enrol to various courses_. It is built with [Python][0] using the [Django Web Framework][1].

This project has the following basic apps:

* Course (Displaying course lists)

## Installation

### Quick start

Clone Repository

    1. git clone https://github.com/sacids/acdc-el.git
    2. cd acdc-el

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ python3 -m venv learn`
    2. `$ . learn/bin/activate`

Install all dependencies:

    pip install -r requirements.txt

Update Database settings
    1. Install your database driver (for postgress: pip install psycopg2-binary)
    1. Create database
    2. open for editing src/learn/setting/local.env 
    3. DATABASE_URL=postgres://<usernamme>:<password>@127.0.0.1:5432/<database>

Run migrations:

    cd src/
    python manage.py makemigrations
    python manage.py migrate

### Detailed instructions

Take a look at the docs for more information.

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/

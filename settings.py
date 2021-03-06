from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'tobias_first_app',
        'display_name': "My first oTree app",
        'num_demo_participants': 1,
        'app_sequence': ['tobias_first_app'],
    },
    {
        'name': 'guess_app',
        'display_name': "Guess game",
        'num_demo_participants': 1,
        'app_sequence': ['guess_app'],
    },
{
        'name': 'dictator_game',
        'display_name': "Dictator game",
        'num_demo_participants': 2, #number of partcipants who participate in the specific day (time)
        'app_sequence': ['dictator_game'],
        'treatment_gender':False,
    },
{
        'name': 'dictator_game_withGender',
        'display_name': "Dictator game with gender",
        'num_demo_participants': 2, #number of partcipants who participate in the specific day (time)
        'app_sequence': ['dictator_game'],
        'treatment_gender':True,
    },
{
        'name': 'Ultimatum_game',
        'display_name': "Ultimatum Game",
        'num_demo_participants': 2, #number of partcipants who participate in the specific day (time)
        'app_sequence': ['ultimatum_game'],
    },
{
        'name': 'political_opinion',
        'display_name': "Political Opinion Game",
        'num_demo_participants': 1, #number of partcipants who participate in the specific day (time)
        'app_sequence': ['political_opinion'],
    },
{
        'name': 'charity_game',
        'display_name': "Charity Game",
        'num_demo_participants': 1, #number of partcipants who participate in the specific day (time)
        'app_sequence': ['charity_game'],
    },
{
        'name': 'public_goods_game',
        'display_name': "Public Goods Game",
        'num_demo_participants': 4, #number of partcipants who participate in the specific day (time)
        'app_sequence': ['public_goods_game'],
    },
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'CHF' #The money which is shown
USE_POINTS = False #does not use virtual currency, instead uses real money

ROOMS = []


# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


# Consider '', None, and '0' to be empty/false
DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})

DEMO_PAGE_INTRO_HTML = """ """

# don't share this with anybody.
SECRET_KEY = '))h$z&2#vevnq8+o*b#t-vjt6!lj=hon5q+of1azu9rvu7(qv%'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

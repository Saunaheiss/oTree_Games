from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'guess_app'
    players_per_group = None #when one player should be None
    num_rounds = 1
    endowment = 100
    minguess= 0
    maxguess = 100
    filipp_constant = 444


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    guess = models.IntegerField(min = Constants.minguess,
                                max=Constants.maxguess,
                                )
    # age = models.IntegerField()
    toguess = models.IntegerField(min = Constants.minguess,
                                max=Constants.maxguess,
                                )
    #payoff is by default here


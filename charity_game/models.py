from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Tobias T.'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'charity_game'
    players_per_group = None
    num_rounds = 1
    minEnd = 20
    maxEnd = 50


class Subsession(BaseSubsession):
    def creating_session(self): #this code is exectued before running the game. Therefore we have radical non radical player
        for p in self.get_players(): #get_players() otree function takes the player
            p.generalA = random.choice((True, False))
            p.generalB = random.choice((True, False))
            p.endowment = random.randint(Constants.minEnd, Constants.maxEnd)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    generalA = models.BooleanField()
    generalB = models.BooleanField()
    endowment = models.IntegerField()
    charity = models.StringField( widget=widgets.RadioSelectHorizontal,choices =["Charity A", "Charity B"])
    views = models.IntegerField(choices= list(range(11)), widget=widgets.RadioSelectHorizontal)


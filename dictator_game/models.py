from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'dictator_game'
    players_per_group = 2  # two players
    num_rounds = 1
    endowment = 100
    minsend = 0
    maxsend = 100


class Subsession(BaseSubsession):
    pass





class Group(BaseGroup):
    dictator_decision = models.CurrencyField(min=Constants.minsend,
                                             max=Constants.maxsend,
                                             verbose_name="How much money would you like to give?",
                                             doc="dictator's decision"
                                             )

    def set_payoffs(self):
        dictator = self.get_player_by_role(
            'dictator')  # get_player_by_role() function in group needs role function of Player class
        receiver = self.get_player_by_role('receiver')
        dictator.payoff = Constants.endowment - self.dictator_decision
        receiver.payoff = self.dictator_decision


class Player(BasePlayer):
    def role(self):
        if self.id_in_group == 1:  # otree function
            return 'dictator'
        else:
            return 'receiver'

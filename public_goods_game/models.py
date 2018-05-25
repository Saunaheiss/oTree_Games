from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'public_goods_game'
    players_per_group = 4
    num_rounds = 10
    endowment = 100
    mininvest = 0
    maxinvest = 100
    multiplicator = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_invest = models.IntegerField()
    total_output = models.IntegerField()
    individual_share = models.IntegerField()

    def set_payoffs(self):
        self.total_invest = sum([p.invest_decision for p in self.get_players()])
        self.total_output = self.total_invest * Constants.multiplicator
        self.individual_share = self.total_output / Constants.players_per_group
        for p in self.get_players():
            p.payoff = self.individual_share + Constants.endowment - p.invest_decision


class Player(BasePlayer):
    invest_decision = models.CurrencyField(min=Constants.mininvest,
                                           max=Constants.maxinvest,
                                           verbose_name="How much money would you like to invest?",
                                           doc="player's invest decision"
                                           )

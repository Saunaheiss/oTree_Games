from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Tobias T.'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'ultimatum_game'
    players_per_group = None
    num_rounds = 1
    endowment = 100
    minsend = 1
    maxsend = 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    sender_decision = models.CurrencyField(min=Constants.minsend,
                                             max=Constants.maxsend,
                                             verbose_name="How much money would you like to give?",
                                             doc="sender's decision"
                                             )
    receiver_decision = models.BooleanField(widget=widgets.RadioSelectHorizontal)
    def set_payoffs(self):
        sender = self.get_player_by_role('sender')
        receiver = self.get_player_by_role('receiver')
        if self.receiver_decision:
            sender.payoff = Constants.endowment - self.sender_decision
            receiver.payoff = self.sender_decision
        else:
            sender.payoff = 0
            receiver.payoff = 0


class Player(BasePlayer):
    control_question1 = models.IntegerField()
    def role(self):
        if self.id_in_group == 1:  # otree function
            return 'sender'
        else:
            return 'receiver'

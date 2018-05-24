from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    pass

class DecisionSender(Page):
    form_model = 'group'  # makes oTree to store it in data
    form_fields = ['sender_decision']  # makes oTree to store it in data

    def is_displayed(self):
        return self.player.role() == 'sender'

class DecisionReceiver(Page):
    form_model = 'group'  # makes oTree to store it in data
    form_fields = ['receiver_decision']  # makes oTree to store it in data

    def is_displayed(self):
        return self.player.role() == 'receiver'

    def vars_for_template(self):
        sender = self.group.get_player_by_role('sender')
        receiver = self.group.get_player_by_role('receiver')
        return {'sender_payoff': sender.payoff,
                'receiver_payoff': receiver.payoff
                }


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    pass


page_sequence = [
    Intro,
    DecisionSender,
    WaitPage,
    DecisionReceiver,
    ResultsWaitPage,
    Results
]

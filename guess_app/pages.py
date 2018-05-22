import random

from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Intro(Page):
    def before_next_page(self):
        toguess = random.randint(Constants.minguess, Constants.maxguess)
        self.player.toguess = toguess

class Decision(Page):
    form_model = 'player'
    form_fields = ['guess']
    def before_next_page(self):
        self.player.payoff = Constants.endowment - abs(self.player.toguess - self.player.guess)


class Results(Page):
    def vars_for_template(self):
        return {'difference': abs(self.player.toguess - self.player.guess)}


page_sequence = [
    Intro,
    Decision,
    Results
]

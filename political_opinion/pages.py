from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


class Decision(Page):
    form_model = 'player'
    form_fields = ['polopinion', 'views']
    def polopinion_choices(self): #polopinion is taken from form_fields. oTree is that clever
        #rand = random.choice([False, True])

        #if rand:
        if self.player.radical:
            return ["SVP", "ARBEIT"]
        else:
            return ["CVP", "FDP"]

    def vars_for_template(self):
        if self.player.radical:
            return {'image1': "charity_game/SVP.svg",
                'image2': "charity_game/Arbeit.jpg",}

        else:
            return {'image1': "charity_game/CVP.png",
                'image2': "charity_game/FDP.png"}



page_sequence = [
    Decision,
    MyPage,
    ResultsWaitPage,
    Results
]

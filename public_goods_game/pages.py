from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Intro(Page):
    def vars_for_template(self):
        series=[{
            'name':'Hello guys',
            'type':'line',
            'data':[100, 20, 3,46],
        }
        ]
        return {'series': series}
    def is_displayed(self):
        return self.round_number == 1 #round_number is a hidden variable like payoff

class Decision(Page):
    form_model = 'player'
    form_fields = ['invest_decision']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()

class Results(Page):
    def vars_for_template(self):
        ddd = [j.invest_decision for i in self.group.get_players() for j in i.in_all_rounds()]
        print("DDDDDD", ddd)
        test = {
            'name': 'Individual share per round',
            'type': 'line',
            'data': [g.individual_share for g in self.group.in_all_rounds()],
        }
        series = [{
            'name': 'Average Contributions of all players',
            'type': 'line',
            'data': [g.total_invest/Constants.players_per_group for g in self.group.in_all_rounds()],
        },
            {
                'name': 'Contribution of you',
                'type': 'line',
                'data': [p.invest_decision for p in self.participant.get_players()],
            }, test,
        ]
        return {'player_payoff': self.player.payoff,
                'series': series

                }







page_sequence = [
    Intro,
    Decision,
    ResultsWaitPage,
    Results,
]

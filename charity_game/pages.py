from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class MyPage(Page):
    def vars_for_template(self):
        companies = ['Apple', 'Microsoft', 'Google', 'Facebook']
        return {'companies': companies}



class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


class Decision(Page):
    form_model = 'player'
    # form_fields = ['polopinion', 'views']
    form_fields = ['donationA', 'donationB']
    timeout_seconds = 5
    def before_next_page(self):
        if self.timeout_happened:
            self.player.donationA = random.randint(0, self.player.endowment)
            self.player.donationB = self.player.endowment - self.player.donationA

    # def polopinion_choices(self): #polopinion is taken from form_fields. oTree is that clever
    #     #rand = random.choice([False, True])
    #
    #     #if rand:
    #     if self.player.radical:
    #         return ["Radical/Individual1", "General1"]
    #     else:
    #         return ["Radical/Individual2", "General2"]

    # def vars_for_template(self):
    #     if self.player.radical:
    #         if self.player.general:
    #             return {'image1': "charity_game/kids1.jpg", 'image2': "charity_game/general1.jpg"}
    #
    #         else:
    #             return {'image1': "charity_game/kids1.jpg", 'image2': "charity_game/general2.jpeg"}
    #     else:
    #         if self.player.general:
    #             return {'image1': "charity_game/kids2.jpg", 'image2': "charity_game/general1.jpg"}
    #
    #         else:
    #             return {'image1': "charity_game/kids2.jpg", 'image2': "charity_game/general2.jpeg"}

    def vars_for_template(self):
        if self.player.generalA:
            image1 ="charity_game/general1.jpg"
        else:
            image1 ="charity_game/kids1.jpg"

        if self.player.generalB:
            image2 ="charity_game/general2.jpeg"
        else:
            image2 = "charity_game/kids2.jpg"

        return {'image1': image1,
                'image2': image2}
    def donationA_max(self):
        return self.player.endowment
    def donationB_max(self):
        return self.player.endowment

    def error_message(self, values):
        print('vales is', values)
        if values['donationA'] + values['donationB'] != self.player.endowment:
            return 'The numbers must add up to {}'.format(self.player.endowment)

page_sequence = [
    MyPage,
    Decision,
    ResultsWaitPage,
    Results
]

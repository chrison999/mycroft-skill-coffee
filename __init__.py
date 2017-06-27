from os.path import dirname
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'forslund'

LOGGER = getLogger(__name__)


class ResponseTestSkill(MycroftSkill):
    def __init__(self):
        super(ResponseTestSkill, self).__init__(name="ResponseTest")
        self.sugar_offer_given = False

    def initialize(self):
        
        coffee_intent = IntentBuilder('CoffeeIntent'). \
            require("CoffeeKeyword").build()
        no_intent = IntentBuilder('NoIntent'). \
            require("NoKeyword").build()
        yes_intent = IntentBuilder('YesIntent'). \
            require("YesKeyword").build()

        self.register_intent(coffee_intent, self.handle_coffee_intent)
        self.register_intent(no_intent, self.handle_no_intent)
        self.register_intent(yes_intent, self.handle_yes_intent)

    def handle_coffee_intent(self, message):
        self.sugar_offer_given = True
        self.speak('Very well, would you like some sugar with that',
                   expect_response=True)

    def handle_yes_intent(self, message):
        if self.sugar_offer_given:
            self.speak('all right, here you go')
            self.sugar_offer_given = False

    def handle_no_intent(self, message):
        if self.sugar_offer_given:
            self.speak('very well, striaght up it is')
            self.sugar_offer_given = False


def create_skill():
    return ResponseTestSkill()

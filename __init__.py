from mycroft import MycroftSkill, intent_file_handler


class RulesOfAcquisition(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('acquisition.of.rules.intent')
    def handle_acquisition_of_rules(self, message):
        self.speak_dialog('acquisition.of.rules')


def create_skill():
    return RulesOfAcquisition()


from bot.label_action.create_gui_issue import CreateGUIIssue
from bot.label_action.create_backport import CreateBackport
from bot.action import Action

ALL_LABEL_ACTIONS = [
    CreateBackport,
    CreateGUIIssue
]

class ActionLabel(Action):
    def __init__(self):
        pass
    
    def isMatched(self, actionRequest):
        if actionRequest.event_type not in ['issue']:
            return False
        if actionRequest.action not in ['labeled']:
            return False
        return True
    
    def action(self, request):
        run = False
        
        for label_action in ALL_LABEL_ACTIONS:
            __label_action = label_action()
            if __label_action.isMatched(request):
                run = True
                __label_action.action(request)

        if not run:
            return "No label action matched"
        
        return "labeled related actions succeed"


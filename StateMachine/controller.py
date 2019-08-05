from time import sleep
from Core.masterController import MasterController

class StateMachine(MasterController):
    def __init__(self, states, variables, initState, *args):
        MasterController.__init__(self)
        self.stateIndex = initState # string
        self.states = states        # dict
        self.variables = variables  # dict
        self.actualState = initState 
        self.initVariables = variables.copy()
        self.initState = initState
        self.nextState = initState
        self.debug = True
        self.timer = 1
        if 'debug' in args:
            self.debug = args['debug']
        if 'timer' = args:
            self.timer = args['timer']

    def run(self):
        if self.debug:
            print('Starting state machine...\r')
        
        while True:
            self.resetVariablesIfInitState()
            self.getActualState()
            if self.debug:
                print('Actual state: {0}\r'.format(self.actualState.name))
                print('Running state...\r')

            self.executeState()
            self.checkConditions()
            if self.debug:
                print('Changing state...\r')

            self.changeState()
            sleep(self.timer)

    def resetVariablesIfInitState(self):
        if self.stateIndex == self.initState:
            self.variables = self.initVariables.copy() 

    def getActualState(self):
        self.actualState = self.states[self.stateIndex]

    def executeState(self):
        self.variables = self.actualState.func(self.variables)        

    def checkConditions(self):
        self.nextState = self.actualState.name
        for nextStateCondition in self.actualState.nextStateConditions:
            for key, value in nextStateCondition['conditions'].iteritems():
                if not self.variables[key] == value:
                    break
            else:
                self.nextState = nextStateCondition['nextState']
                return
            
    def changeState(self):
        self.stateIndex = self.nextState

class State:
    def __init__(self, name, func, nextStateConditions):
        self.name = name                # string
        self.func = func                # function
        self.nextStateConditions = nextStateConditions    # dict
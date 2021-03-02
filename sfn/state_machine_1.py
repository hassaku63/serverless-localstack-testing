

def state1(event, context):
    pass


def state2(event, context):
    pass


"""
functions:
    sm1_state1:
        type: lambda-functions
        handler: sfn/state_machine_1.state1

StateMchine1:
    definitions:
        startAt: state1
        states:
            state1:
                - Type: task
                  resource: arn of sm1_state1
                  next: state2
            state2:
                - type: task
                  resource: arn of sm1_state2
                  end: true
"""
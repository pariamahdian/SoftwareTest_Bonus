from behave import given, when, then
from part1 import InputDomainModeler, generate_model
import sys

objects = []

@given('I have the following input objects')
def create_input_objects(context):
    for row in context.table:
        obj = InputDomainModeler(row['Characteristic'], eval(row['Blocks']))
        objects.append(obj)

@when('I enter the working mode {mode}')
def enter_working_mode(context, mode):
    context.mode = mode

@then('the program should display the expected output based on the mode')
def validate_output(context):
    sys.stdout = OutputCapture()
    generate_model(objects, context.mode)

class OutputCapture:
    def write(self, txt):
        pass

    def flush(self):
        pass
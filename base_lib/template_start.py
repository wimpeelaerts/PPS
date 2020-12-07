"""template start implementes the start of a test.

Using this template enfoces some pre and post procedures 

"""
import uuid 

class template_start:

  runid = uuid.uuid1()

  def __init__(self, user, testbench):
    self.user = user
    self.testbench = testbench

  def start_test(self):
    print(f"Test started: {self.runid}.")
    print(f"Test started by {self.user} @ {self.testbench}.")
    # Start timer 
    # Acutal start command

  def get_runid(self):
    return self.runid

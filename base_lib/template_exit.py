"""template exit implementes the stopping of a certain test.

Using this template enfoces some pre and post procedures on stopping the test. 

"""
class template_exit:
  def __init__(self, test_id):
    """[summary]

    Args:
        test_id ([type]): [description]
    """
    self.test_id = test_id

  def exit_test(self):
    print(f"Stop the test with run_id {self.test_id}")
    #Actual Stop

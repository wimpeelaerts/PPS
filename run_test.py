"""Run a test based on the templates provided in base lib.

Therefor we reuse the templatefiles by using class objects and if neccecary inheritance

"""

from base_lib.template_start import template_start
from base_lib.template_exit import template_exit


class better_template_start(template_start):
  def __init__(self, user, testbench, software_version):
    super().__init__(user, testbench)
    self.software_version = software_version

  def start_test(self):
    super().start_test()
    print(f"With software version {self.software_version}")
  
  

print("Start local run")
test = template_start("Wim", "Bench1")
print(f"Running with id {test.get_runid()}")
test_id = test.start_test()
exit = template_exit(test_id)
exit.exit_test()

print("Start better local run")
test = better_template_start("Hans", "Bench5", "1.0.2")
print(f"Running with id {test.get_runid()}")
test_id = test.start_test()
exit = template_exit(test_id)
exit.exit_test()



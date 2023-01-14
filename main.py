# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main

print(add_time("11:06 PM", "2:02"))
# the tests I'm currently failing
print(add_time("11:55 AM", "3:12")) # needs to be AM, not PM
print(add_time("8:16 PM", "466:02")) # needs to be AM, not PM
print(add_time("8:16 PM", "466:02", "tuesday")) # needs to be AM, not PM
print(add_time("9:15 PM", "5:30")) # must return (next day)

# Run unit tests automatically
main(module='test_module', exit=False)
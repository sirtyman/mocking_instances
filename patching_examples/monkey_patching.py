""""…the term monkey patch only refers to dynamic modifications of a class or module at runtime, motivated by the
intent to patch existing third-party code as a workaround to a bug or feature which does not act as desired.
Other forms of modifying classes at runtime have different names, based on their different intents.
"""

import math

print(math.pi)
original = math.pi
math.pi = 3
print(math.pi)
math.pi = original
print(math.pi)
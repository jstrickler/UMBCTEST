#!/usr/bin/env python
#
from unittest.mock import Mock

m1 = Mock(return_value=[1, 2, 3]) # <1>

mock_result = m1('a', 'b') # <2>

print("mock result:", mock_result) # <3>



m2 = Mock()  # <4>

m2.spam('a', 'b') # <5>
m2.ham('wombat') # <5>
m2.eggs(1, 2, 3) # <5>

print("mock calls:", m2.mock_calls)

m2.spam.assert_called_with('a', 'b') # <6>

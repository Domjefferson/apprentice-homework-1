from collections import namedtuple
from unittest import TestCase

from tasks.part1_task1 import add_numbers, multiply_numbers

Case = namedtuple('Case', ['input', 'result'])

class TestPartOne(TestCase):
    """Part 1: Math Operations"""

    def test_task_one_addition(self):
        """Task 1: Basic Math - Addition"""
        cases = [
            Case((28, 315), 343),
            Case((369, 928), 1297),
            Case((129, 193), 322),
            Case((178, 950), 1128),
        ]
        for case in cases:
            self.assertEqual(add_numbers(*case.input), case.result)

    def test_task_two(self):
        pass

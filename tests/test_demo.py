import pytest

# All tests should be written in a class **without an __init__**
class TestClass:
	# Test functions alwasy start with "test_"
	def test_one(self):
		# assert boolean
		assert 1 == 1

	def test_two(self):
		assert "one" == "one"

	def test_three(self):
		a = [1, 2, 3, 4]
		assert 1 in a

# Run tests in terminal using "pytest <filename.py>"

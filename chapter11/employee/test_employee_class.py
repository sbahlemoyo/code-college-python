import pytest
from employee_class import Employee

def test_give_default_raise():
    """Test if give raise works"""
    employee1 = Employee('Sbahle', 'Moyo', 25000)
    assert employee1.give_raise() == 30000

def test_give_custom_raise():
    employee2 = Employee('Zama', 'Chiya', 35000)
    assert employee2.give_raise(2000) == 37000
    
    
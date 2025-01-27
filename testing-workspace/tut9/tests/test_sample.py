from myapp.sample import guess_number
from unittest import mock


@mock.patch("myapp.sample.roll_dice")
def test_guess_number(mock_roll_dice) :
    mock_roll_dice.return_value = 3 
    assert guess_number(3) == "You won"
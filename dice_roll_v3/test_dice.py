from dice import Dice, Hand, NoMoreRerolls
import pytest


def test_create_dice():
    dice = Dice(8, 4)
    assert dice.sides == 8
    assert dice.rerolls == 4


def test_dice_invalid_sides():
    with pytest.raises(ValueError):
        Dice(3, 2)


def test_dice_invalid_rerolls():
    with pytest.raises(ValueError):
        Dice(4, -2)


def test_dice_roll(monkeypatch):
    dice = Dice(8, 4)

    def result_two(f, s):
        return 2

    monkeypatch.setattr("dice.randint", result_two)
    result = dice.roll()
    assert result == 2


def test_dice_reroll(monkeypatch):
    dice = Dice(8, 4)

    def result_two(f, s):
        return 2

    monkeypatch.setattr("dice.randint", result_two)
    result = dice.reroll()
    assert result == 2


def test_dice_reroll_zero():
    dice = Dice(8, 0)
    with pytest.raises(NoMoreRerolls):
        dice.reroll()


def test_get_dice_type():
    dice = Dice(8, 0)
    result = dice.get_dice_type()
    assert result == "D8"


def test_create_hand():
    dice1 = Dice(8, 4)
    dice2 = Dice(6, 1)
    dice3 = Dice(4, 2)
    dice4 = Dice(4, 3)
    dices = [dice1, dice2, dice3, dice4]
    hand = Hand(dices)
    assert hand.dices == [dice1, dice2, dice3, dice4]


def test_hand_roll_dices(monkeypatch):
    dice1 = Dice(8, 4)
    dice2 = Dice(6, 1)
    dice3 = Dice(4, 2)
    dice4 = Dice(4, 3)
    dices = [dice1, dice2, dice3, dice4]
    hand = Hand(dices)

    def roll_result_three(s, t):
        return 3

    monkeypatch.setattr("dice.randint", roll_result_three)
    hand.roll_dices()
    assert hand.scores == [["D8", 3], ["D6", 3], ["D4", 3], ["D4", 3]]


def test_hand_reroll_one_dice(monkeypatch):
    dice1 = Dice(8, 4)
    dice2 = Dice(6, 1)
    dice3 = Dice(4, 2)
    dice4 = Dice(4, 3)
    dices = [dice1, dice2, dice3, dice4]
    hand = Hand(dices)

    def roll_result_three(s, t):
        return 3

    monkeypatch.setattr("dice.randint", roll_result_three)
    scores = [["D8", 6], ["D6", 1], ["D4", 2], ["D4", 2]]
    hand.set_scores(scores)
    hand.reroll_dice([2])
    assert hand.scores == [["D8", 6], ["D6", 1], ["D4", 3], ["D4", 2]]


def test_hand_reroll_multiple_dices(monkeypatch):
    dice1 = Dice(8, 4)
    dice2 = Dice(6, 1)
    dice3 = Dice(4, 2)
    dice4 = Dice(4, 3)
    dices = [dice1, dice2, dice3, dice4]
    hand = Hand(dices)

    def roll_result_three(s, t):
        return 3

    monkeypatch.setattr("dice.randint", roll_result_three)
    scores = [["D8", 6], ["D6", 1], ["D4", 2], ["D4", 2]]
    hand.set_scores(scores)
    hand.reroll_dice([0, 1, 2])
    assert hand.scores == [["D8", 3], ["D6", 3], ["D4", 3], ["D4", 2]]


def test_hand_sum_scores():
    dice1 = Dice(8, 4)
    dice2 = Dice(6, 1)
    dice3 = Dice(4, 2)
    dice4 = Dice(4, 3)
    dices = [dice1, dice2, dice3, dice4]
    hand = Hand(dices)
    scores = [["D8", 6], ["D6", 1], ["D4", 2], ["D4", 2]]
    hand.set_scores(scores)
    assert hand.sum_scores() == 11


def test_hand_compare_hands():
    dice1 = Dice(8, 4)
    dice2 = Dice(6, 1)
    dice3 = Dice(4, 2)
    dice4 = Dice(4, 3)
    dices = [dice1, dice2, dice3, dice4]
    hand1 = Hand(dices)
    hand2 = Hand(dices)
    scores1 = [["D8", 6], ["D6", 1], ["D4", 2], ["D4", 2]]
    scores2 = [["D8", 1], ["D6", 1], ["D4", 1], ["D4", 2]]
    hand1.set_scores(scores1)
    hand2.set_scores(scores2)
    result = hand1.compare_hands(hand2)
    assert result == "Player 1 wins by 6 points"


# def hand_roll_raport():
#     dice1 = Dice(8, 4)
#     dice2 = Dice(6, 1)
#     dice3 = Dice(4, 2)
#     dice4 = Dice(4, 3)
#     dices = [dice1, dice2, dice3, dice4]
#     hand = Hand(dices)
#     scores = [["D8", 6], ["D6", 1], ["D4", 2], ["D4", 2]]
#     hand.set_scores(scores)
#     hand.roll_raport()


# if __name__ == "__main__":
#     hand_roll_raport()

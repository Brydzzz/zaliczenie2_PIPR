from random import randint


class NoMoreRerolls(Exception):
    def __init__(self):
        super().__init__("No more rerolls left for this dice")


class Dice:
    def __init__(self, sides: int, rerolls: int):
        if sides % 2 != 0 or sides <= 2:
            raise ValueError("Sides have to be even and bigger than 2")
        if rerolls < 0:
            raise ValueError("Rerolls cannot be negative")
        self._sides = sides
        self._rerolls = rerolls

    @property
    def sides(self):
        return self._sides

    @property
    def rerolls(self):
        return self._rerolls

    def roll(self):
        return randint(1, self.sides)

    def reroll(self):
        if self.rerolls > 0:
            self._rerolls -= 1
            return self.roll()
        else:
            raise NoMoreRerolls

    def get_dice_type(self):
        return "D" + str(self.sides)


class Hand:
    def __init__(self, dices: list[Dice]):
        self._dices = dices
        self._scores = []

    @property
    def dices(self):
        return self._dices

    @property
    def scores(self):
        return self._scores

    def set_scores(self, new_scores):
        self._scores = new_scores

    def roll_dices(self):
        for dice in self.dices:
            dice_type = dice.get_dice_type()
            rolled_number = dice.roll()
            roll_result = [dice_type, rolled_number]
            self._scores.append(roll_result)

    def reroll_dice(self, dice_indexes: list):
        for dice_index in dice_indexes:
            selected_dice = self.dices[dice_index]
            rerolled_score = selected_dice.reroll()
            self._scores[dice_index][1] = rerolled_score

    def sum_scores(self):
        return sum(dice[1] for dice in self.scores)

    def compare_hands(self, other):
        sum1 = self.sum_scores()
        sum2 = other.sum_scores()
        if sum1 > sum2:
            return f"Player 1 wins by {sum1 - sum2} points"
        elif sum1 < sum2:
            return f"Player 2 wins by {sum2 - sum1} points"
        else:
            return "It's a tie"

    def roll_raport(self):
        score_sum = self.sum_scores()
        max_points = sum(dice.sides for dice in self.dices)
        for dice in self.scores:
            print(f"* {dice[0]}: {dice[1]}")
        print(f"Total roll value: {score_sum} / {max_points}")

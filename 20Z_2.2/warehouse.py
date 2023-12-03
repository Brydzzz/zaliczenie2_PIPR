class NotEnoughResourcesError(Exception):
    def __init__(self):
        super().__init__("Not enough resources to make and order")


class Warehouse:
    def __init__(self):
        self._glycerine = 20000
        self._aloes = 15000
        self._alcohol = 80000
        self._preservative = 17000

    def generate_raport(self):
        print(f"| {f'Zasób':10}\t| Ilość w magazynie [l] |")
        print(f"| {'-' * 13} | {'-'*21}:|")
        print(f"| {'glycerine':13} |{int(self._glycerine/1000):>22} |")
        print(f"| {'aloes':13} |{int(self._aloes/1000):>22} |")
        print(f"| {'alcohol':13} |{int(self._alcohol/1000):>22} |")
        print(f"| {'preservative':13} |{int(self._preservative/1000):>22} |")

    def check_order(self, aloe_gel, hand_sanitizer, surface_sanitizer, mask):
        glycerine_cost = (
            aloe_gel * 100 + hand_sanitizer * 30 + surface_sanitizer * 5
        )  # nq:501
        aloes_cost = aloe_gel * 350
        alcohol_cost = (
            aloe_gel * 600 + hand_sanitizer * 720 + surface_sanitizer * 800
        )  # nq:501
        preservative_cost = mask * 50
        if glycerine_cost >= self._glycerine:
            raise NotEnoughResourcesError
        if alcohol_cost >= self._alcohol:
            raise NotEnoughResourcesError
        if aloes_cost >= self._aloes:
            raise NotEnoughResourcesError
        if preservative_cost >= self._preservative:
            raise NotEnoughResourcesError
        return (
            f"Resources needed: \n glycerine: {glycerine_cost}ml, "
            f"aloes: {aloes_cost}ml, alcohol: {alcohol_cost}ml, "
            f"preservative: {preservative_cost}ml"
        )


if __name__ == "__main__":
    abc_warehouse = Warehouse()
    abc_warehouse.generate_raport()
    print(abc_warehouse.check_order(3, 7, 6, 1))

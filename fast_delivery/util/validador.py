class Validador:
    @staticmethod
    def num(val):
        try:
            return float(val) > 0
        except ValueError:
            return False

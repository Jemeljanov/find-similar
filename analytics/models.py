from find_similar import TokenText


class ReportUnit:
    def __init__(self, request: TokenText, best_find: TokenText, rating: int):
        self.request = request
        self.best_find = best_find
        self.rating = rating

    def __eq__(self, other):
        return self.rating == other.rating
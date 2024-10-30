from logging import exception


class InsufficientFundsError (Exception):
    pass

class WithdrawalTimeRestrictionError(exception):
    pass
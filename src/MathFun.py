class MathFun:

    @classmethod
    def execute(cls, math_request):
        operator = math_request.get_operator()
        ope1 = math_request.get_ope1()
        ope2 = math_request.get_ope2()

        match operator:
            case 'max':
                # help : https://www.geeksforgeeks.org/ternary-operator-in-python/
                if ope1 == ope2:
                    raise EqualityException
                return ope1 if ope1 > ope2 else ope2
            case 'is_sum_even':
                res = ope1 + ope2
                mod = res % 2
                return True if mod == 0 else False
            case _:
                raise FunOperatorNotSupportedException

class MathFunException(Exception):
    pass

class FunOperatorNotSupportedException(MathFunException):
    pass

class EqualityException(MathFunException):
    pass
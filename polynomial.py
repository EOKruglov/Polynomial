class Polynomial:
    coeffs = None

    def __init__(self, args):

        if isinstance(args, int):
            self.coeffs = [args]
        elif isinstance(args, list) or isinstance(args, tuple):
            if args:
                for arg in args:
                    if not isinstance(arg, int):
                        raise TypeError("Unsupported data type: {}!".format(type(arg)))
                self.coeffs = list(args)
            else:
                raise ValueError("Argument with type {} is empty!".format(type(args)))
        elif isinstance(args, Polynomial):
            self.coeffs = args.coeffs.copy()
        else:
            raise TypeError('Unsupported data type: {}! {}, {}, {}, {} are expected!'.format(type(args), int, list,
                                                                                             tuple, Polynomial))

    def __add_sub_pattern__(self, p2, op):
        if not isinstance(p2, int) and not isinstance(p2, Polynomial):
            raise TypeError('Unsupported operand type: {}!'.format(type(p2)))

        result = None
        operations_dict = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y
        }
        if isinstance(p2, int):
            result = self.coeffs.copy()
            result[-1] = operations_dict[op](self.coeffs[-1], p2)
        else:
            p1_reverse_coeffs = self.coeffs[::-1]
            p2_reverse_coeffs = p2.coeffs[::-1]

            if len(p1_reverse_coeffs) > len(p2_reverse_coeffs):
                result = p1_reverse_coeffs
                p2_reverse_coeffs += [0] * (len(p1_reverse_coeffs) - len(p2_reverse_coeffs))
            else:
                result = p2_reverse_coeffs
                p1_reverse_coeffs += [0] * (len(p2_reverse_coeffs) - len(p1_reverse_coeffs))

            for i in range(len(p1_reverse_coeffs)):
                result[i] = operations_dict[op](p1_reverse_coeffs[i], p2_reverse_coeffs[i])

            result = result[::-1]

        return Polynomial(result)

    def __add__(self, other):
        return self.__add_sub_pattern__(other, '+')

    def __radd__(self, other):
        other = Polynomial(other)
        return other.__add__(self)

    def __sub__(self, other):
        return self.__add_sub_pattern__(other, '-')

    def __rsub__(self, other):
        other = Polynomial(other)
        return other.__sub__(self)

    def __mul__(self, other):
        if not isinstance(other, int) and not isinstance(other, Polynomial):
            raise TypeError('Unsupported operand type: {}!'.format(type(other)))

        result = None

        if isinstance(other, int):
            result = self.coeffs.copy()
            for i in range(len(result)):
                result[i] *= other
        else:
            result = [0] * (len(self.coeffs) + len(other.coeffs) - 1)
            for i, coeff_1 in enumerate(self.coeffs[::-1]):
                for j, coeff_2 in enumerate(other.coeffs[::-1]):
                    result[i + j] += coeff_1 * coeff_2

            result = result[::-1]

        return Polynomial(result)

    def __rmul__(self, other):
        other = Polynomial(other)
        return other.__mul__(self)

    def __eq__(self, other):
        if not isinstance(other, int) and not isinstance(other, Polynomial):
            raise TypeError('Unsupported operand type: {}!'.format(type(other)))

        if isinstance(other, Polynomial):
            return self.coeffs == other.coeffs
        else:
            return self.coeffs == [other]

    def __str__(self):
        result = []
        for i, coeff in enumerate(self.coeffs[::-1]):
            if coeff == 0:
                continue
            if i != 0 and i != 1:
                if coeff == 1:
                    result.append('x^{}'.format(i))
                else:
                    result.append('{}x^{}'.format(coeff, i))
            elif i == 1:
                if coeff == 1:
                    result.append('x^{}'.format(i))
                else:
                    result.append('{}x'.format(coeff))
            else:
                result.append('{}'.format(coeff))
        return '+'.join(result[::-1])

    def __repr__(self):
        return 'Polynomial({})'.format(self.coeffs)
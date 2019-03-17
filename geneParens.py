# -*- coding: utf-8 -*
def generateParenthesis(n):
    def generate(p, left, right, parens=[]):
        if left:
            generate(p + '(', left-1, right)
        if right > left:
            generate(p + ')', left, right-1)
        if not right:
            parens += p,
        return parens
    return generate('', n, n)


res = generateParenthesis(1)
print(res)

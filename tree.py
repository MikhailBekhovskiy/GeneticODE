from math import exp, sin, cos, pi
from random import randint

class Node():
    def __init__(self, name, args = []):
        if type(name) is float:
            self.name = float(name)
            self.left = None
            self.right = None
        elif name == 'x':
            self.name = name
            self.left = None
            self.right = None
        else:
            # in case of unary argument function the only child is left
            self.name = name
            self.left = args[0]
            if len(args) == 2:
                self.right = args[1]
            else:
                self.right = None
    
    def evaluate(self, x_val: float) -> float:
        if self.name == 'x':
            return x_val
        elif type(self.name) is float:
            return self.name
        else:
            foo = self.name
            if foo == '+':
                return self.left.evaluate(x_val) + self.right.evaluate(x_val)
            if foo == '*':
                return self.left.evaluate(x_val) * self.right.evaluate(x_val)
            if foo == 'exp':
                return exp(self.left.evaluate(x_val))
            if foo == 'sin':
                return sin(self.left.evaluate(x_val))
            if foo == 'cos':
                return cos(self.left.evaluate(x_val))
            if foo == '-':
                return self.left.evaluate(x_val) - self.right.evaluate(x_val)
            if foo == 'u-':
                return -self.left.evaluate(x_val)
            
    def printout(self) -> str:
        if self.name == 'x':
            return self.name
        elif type(self.name) is float:
            return str(self.name)
        else:
            if self.right is not None:
                if self.name == '-':
                    return self.left.printout() + self.name + '(' + self.right.printout() + ')'
                else:
                    return self.left.printout() + self.name + self.right.printout()
            else:
                if self.name == 'u-':
                    name = '-'
                    return '(' + name + '(' + self.left.printout() + '))'
                else:
                    name = self.name
                    return name + '(' + self.left.printout() + ')'
            
class Tree():
    def __init__(self, starting_node=Node('x'), random=False, max_depth=5, funcs = ['+', '*', '-', 'u-', 'exp', 'cos', 'sin']):
        if not random:
            self.start = starting_node
        else:
            if max_depth == 1:
                i = randint(0,1)
                if i == 0:
                    self.start = Node('x')
                else:
                    num = randint(1,100) * pi
                    self.start = Node(num)
            else:
                i = randint(0, len(funcs) + 1)
                if i < len(funcs):
                    name = funcs[i]
                    left = Tree(random=True, max_depth = max_depth - 1, funcs = funcs)
                    if name in {'+', '*', '-'}:
                        right = Tree(random=True, max_depth=max_depth - 1, funcs = funcs)
                        self.start = Node(name, [left,right])
                    else:
                        self.start = Node(name, [left])
                elif i == len(funcs):
                    self.start = Node('x')
                else:
                    num = randint(1, 100) * pi
                    self.start = Node(num)
    
    def evaluate(self, x_val: float) -> float:
        return self.start.evaluate(x_val)
    
    def printout(self) -> str:
        return self.start.printout()

if __name__ == "__main__":
    T1 = Tree(random=True)
    foo = T1.printout()
    print(foo)
    x = float(input())
    val = T1.evaluate(x)
    print(val)
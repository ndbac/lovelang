class Node:
    pass

class NumberNode(Node):
    def __init__(self, value):
        self.value = value

class StringNode(Node):
    def __init__(self, value):
        self.value = value

class BinOpNode(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class VariableNode(Node):
    def __init__(self, name):
        self.name = name

class AssignNode(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value

class PrintNode(Node):
    def __init__(self, expr):
        self.expr = expr

class IfNode(Node):
    def __init__(self, condition, kiss_block, hug_block=None):
        self.condition = condition
        self.kiss_block = kiss_block
        self.hug_block = hug_block

class WhileNode(Node):
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block

class BlockNode(Node):
    def __init__(self, statements):
        self.statements = statements

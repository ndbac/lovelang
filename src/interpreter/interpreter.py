from src.lexer.tokens import TokenType
from src.parser.ast import *

class Interpreter:
    def __init__(self):
        self.variables = {}

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.no_visit_method)
        return method(node)

    def no_visit_method(self, node):
        raise Exception(f'No visit_{type(node).__name__} method defined')

    def visit_NumberNode(self, node):
        return node.value

    def visit_StringNode(self, node):
        return node.value

    def visit_BinOpNode(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)

        operations = {
            TokenType.PLUS: lambda: left + right,
            TokenType.MINUS: lambda: left - right,
            TokenType.MULTIPLY: lambda: left * right,
            TokenType.DIVIDE: lambda: left / right,
            TokenType.EQ: lambda: left == right,
            TokenType.NEQ: lambda: left != right,
            TokenType.LT: lambda: left < right,
            TokenType.GT: lambda: left > right,
            TokenType.LTE: lambda: left <= right,
            TokenType.GTE: lambda: left >= right,
        }

        if node.op.type in operations:
            return operations[node.op.type]()
        else:
            raise Exception(f"Unknown operator: {node.op.type}")

    def visit_VariableNode(self, node):
        if node.name not in self.variables:
            raise NameError(f"Variable '{node.name}' is not defined")
        return self.variables[node.name]

    def visit_AssignNode(self, node):
        value = self.visit(node.value)
        self.variables[node.name] = value
        return value

    def visit_PrintNode(self, node):
        value = self.visit(node.expr)
        print(value)
        return value

    def visit_IfNode(self, node):
        condition = self.visit(node.condition)
        if condition:
            return self.visit(node.kiss_block)
        elif node.hug_block:
            return self.visit(node.hug_block)

    def visit_WhileNode(self, node):
        while self.visit(node.condition):
            self.visit(node.block)

    def visit_BlockNode(self, node):
        result = None
        for statement in node.statements:
            result = self.visit(statement)
        return result

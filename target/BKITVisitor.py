# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_declare.
    def visitVar_declare(self, ctx:BKITParser.Var_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#ids_list.
    def visitIds_list(self, ctx:BKITParser.Ids_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#id_declare.
    def visitId_declare(self, ctx:BKITParser.Id_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_declare.
    def visitArray_declare(self, ctx:BKITParser.Array_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_declare.
    def visitFunc_declare(self, ctx:BKITParser.Func_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#header_stm.
    def visitHeader_stm(self, ctx:BKITParser.Header_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#paramater_stm.
    def visitParamater_stm(self, ctx:BKITParser.Paramater_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#body_stm.
    def visitBody_stm(self, ctx:BKITParser.Body_stmContext):
        return self.visitChildren(ctx)



del BKITParser
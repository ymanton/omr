#!/usr/bin/env python

from pyparsing import *

__all__ = ("Method", "Block", "Assignment", "Node")

LParen, RParen, LSqBr, RSqBr, Eq = map(Suppress, "()[]=")
Base10 = Regex(r"[+-]?\d+")
Base16 = Combine("0x" + Word(hexnums))
Integer = Base16 | Base10
Real = Regex(r"[+-]?\d+\.\d*")
Number = Real | Integer
Identifier = Word(alphas + "_", alphanums + "_")
String = dblQuotedString

Flag = Identifier("flag")
Flags = Group(LSqBr + ZeroOrMore(Flag) + RSqBr)("flags")
Symbol = Combine(Suppress("S") + String)("sym")
Label = Combine(Suppress("L") + String)("label")
Payload = (Symbol | Label | Number)("payload")
Node = Forward()
NodeDef = Combine(Suppress("$") + Identifier)("nodedef")
NodeRef = (LParen + Combine(Suppress("$") + Identifier) + RParen)("noderef")
Assignment = Group(LParen + Node + Eq + NodeDef + RParen)("assign")
ILOpCode = Identifier("opcode")
Children = Group(ZeroOrMore(NodeRef | Node | Assignment))("children")
Node <<= Group(LParen + ILOpCode + Optional(Payload) + Optional(Flags) + Children + RParen)("node")
Trees = Group(ZeroOrMore(Node | Assignment))("trees")
Frequency = (Suppress(Keyword("freq")) + Eq + Integer)("freq")
Block = Group(LParen + Suppress(Keyword("block")) + Optional(Label) + Optional(Flags) + Optional(Frequency) + Trees + RParen)("block")
Blocks = Group(ZeroOrMore(Block))("blocks")
MethodName = Symbol("name")
Parameters = Group(LParen + ZeroOrMore(Symbol) + RParen)("parms")
Method = (LParen + Suppress(Keyword("method")) + MethodName + Parameters + Blocks + RParen)("method")

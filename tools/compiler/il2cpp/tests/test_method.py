import unittest

from il2cpp import *

method = """
(method S"example" (S"x" S"y" S"z")
    (block freq=10000
        (bbstart)
        (ificmple L"x_is_zero"
            ((iload S"x") = $xReg)
            (iconst 0)
        )
        (bbend)
    )
    (block [extbb] freq=5000
        (bbstart)
        (istore S"modifiedX"
            (iadd [nodeIsNonZero nodeIsNonNegative]
                ($xReg)
                (iconst 99)
            )
        )
        (ificmpeq L"x_and_y_somefield_equal"
            (iloadi S"SomeStruct.someField"
                (aload S"y")
            )
            ($xReg)
        )
        (bbend)
    )
    (block L"x_is_zero" freq=100
        (bbstart)
        (ireturn
            (iconst -1)
        )
        (bbend)
    )
    (block L"x_and_y_somefield_equal"
        (bbstart)
        ((icall S"Int32 someFunction(Int32, Float)"
            (iload S"modifiedX")
            (fload S"z")
        ) = $retVal)
        (ireturn
            ($retVal)
        )
        (bbend)
    )
)
"""

class TestMethod(unittest.TestCase):
    def test_method(self):
        self.assertTrue(Method.runTests(("# Simple method", method))[0])

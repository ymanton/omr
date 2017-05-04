import unittest

from il2cpp import *

class TestNode(unittest.TestCase):
    def test_node(self):
        self.assertTrue(
            Node.runTests("""
            # Simple node
            (bbstart)
            # Node with base10 number payload
            (iconst 99)
            # Node with base16 number payload
            (iconst 0x99)
            # Node with real number payload
            (fconst 0.99)
            # Node with label payload
            (goto L"foo")
            # Node with symbol payload
            (vcall S"foo()")
            # Node with empty flags
            (iconst 99 [])
            # Node with one flag
            (iconst 99 [nodeIsNonZero])
            # Node with multiple flags
            (iconst 99 [nodeIsNonZero nodeIsNonNegative])
            """)[0]
        )
    def test_node_with_assignment(self):
        self.assertTrue(
            Assignment.runTests("""
            # Simple node with assignment
            ((bbstart) = $x)
            # Node with base10 number payload with assignment
            ((iconst 99) = $x)
            # Node with base16 number payload with assignment
            ((iconst 0x99) = $x)
            # Node with real number payload with assignment
            ((fconst 0.99) = $x)
            # Node with label payload with assignment
            ((goto L"foo") = $x)
            # Node with symbol payload with assignment
            ((vcall S"foo()") = $x)
            # Node with empty flags with assignment
            ((iconst 99 []) = $x)
            # Node with one flag with assignment
            ((iconst 99 [nodeIsNonZero]) = $x)
            # Node with multiple flags with assignment
            ((iconst 99 [nodeIsNonZero nodeIsNonNegative]) = $x)
            """)[0]
        )

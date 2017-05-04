import unittest

from il2cpp import *

class TestBlock(unittest.TestCase):
    def test_block(self):
        self.assertTrue(
            Block.runTests("""
            # Simple block
            (block)
            # Block with one node
            (block (bbstart))
            # Block with two nodes
            (block (bbstart) (bbend))
            """)[0]
        )
    def test_block_with_freq(self):
        self.assertTrue(
            Block.runTests("""
            # Simple block with freq
            (block freq=99)
            # Block with one node with freq
            (block freq=100 (bbstart))
            # Block with two nodes with freq
            (block freq=101 (bbstart) (bbend))
            """)[0]
        )
    def test_block_with_flags(self):
        self.assertTrue(
            Block.runTests("""
            # Simple block with empty flags
            (block [])
            # Simple block with one flag
            (block [_isCold])
            # Block with one node with one flag
            (block [_isCold] (bbstart))
            # Block with two nodes with one flag
            (block [_isCold] (bbstart) (bbend))
            """)[0]
        )
        self.assertTrue(
            Block.runTests("""
            # Simple block with multiple flags
            (block [_isCold _doNotProfile])
            # Block with one node with multiple flags
            (block [_isCold _doNotProfile] (bbstart))
            # Block with two nodes with multiple flags
            (block [_isCold _doNotProfile] (bbstart) (bbend))
            """)[0]
        )

import pytest
from typing import List
from crosstl.backend.Vulkan.VulkanLexer import VulkanLexer


def tokenize_code(code: str) -> List:
    """Helper function to tokenize code."""
    lexer = VulkanLexer(code)
    return lexer.tokenize()


def test_mod_tokenization():
    code = """
        int a = 10 % 3;  // Basic modulus
    """
    tokens = tokenize_code(code)

    # Find the modulus operator in tokens
    has_mod = False
    for token in tokens:
        if token == ("MOD", "%"):
            has_mod = True
            break

    assert has_mod, "Modulus operator (%) not tokenized correctly"


if __name__ == "__main__":
    pytest.main()

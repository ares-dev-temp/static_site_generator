import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text", TextType.BOLD)
        self.assertNotEqual(node, node2)

        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.mylink.com")
        self.assertNotEqual(node, node2)

    #def test_assertEqual(self, first, second, msg = None):
    #    return self.assertEqual(first, second, msg)
    
    #def test_assertNotEqual(self, first, second, msg = None):
    #    return self.assertNotEqual(first, second, msg)

if __name__ == "__main__":
    unittest.main()
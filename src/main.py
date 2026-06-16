from textnode import TextNode, TextType

def main():
    textNode = TextNode("some text", TextType.LINK, "https://www.mylink.org")
    print( textNode )

main()
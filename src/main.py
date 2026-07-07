from textnode import TextNode, TextType
from copy_static import *
from generate_page import *

def main():
    textNode = TextNode("some text", TextType.LINK, "https://www.mylink.org")
    #print( textNode )

    copy_static( "static", "public" )
    #generate_page( "content/index.md", "template.html", "public/index.html" )
    generate_page_recursive( "content", "template.html", "public" )

main()
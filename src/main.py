from textnode import TextNode, TextType
from copy_static import *
from generate_page import *
import sys

def main():
    textNode = TextNode("some text", TextType.LINK, "https://www.mylink.org")
    #print( textNode )

    base_path = "/"

    if len(sys.argv) > 1:
        base_path = sys.argv[1]

    print( "args ", sys.argv )
    

    copy_static( "static", "docs" )
    #generate_page( "content/index.md", "template.html", "public/index.html" )
    #generate_page_recursive( "content", "template.html", "public" )

    #my_doc = "/https://github.com/ares-dev-temp/doc/"
    #base_path = "/https://github.com/" + base_path

    generate_page_recursive( "content", "template.html", "docs", base_path )

main()
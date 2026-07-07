from htmlnode import HTMLNode, LeafNode

def HTMLNode_tests():
    nodeA = HTMLNode( "<p>", "some text" )
    nodeB = HTMLNode( "<h>", "idont", [ nodeA ] )
    nodeC = HTMLNode( "<h1>", "lostsa text", [nodeA], {"A" : "C"} )

    print( "Printing Node A:" )
    print( nodeA.props_to_html() )
    print()
    print( "Printing Node B:" )
    print( nodeB.props_to_html() )
    print()
    print( "Printing Node C:" )
    print( nodeC.props_to_html() )


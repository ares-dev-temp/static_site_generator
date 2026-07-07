from enum import Enum
from htmlnode import *#LeafNode
import re

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code_text"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text : str, type : TextType, url=None):
        self.text = text
        self.text_type = type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )
        '''
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        
        return False
        '''
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        if text_node.url is None:
            raise ValueError("invalid URL")
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        if text_node.url is None:
            raise ValueError("invalid URL")
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"invalid text type: {text_node.text_type}")

'''
def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type == None:
        raise Exception
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text) 
    if text_node == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node == TextType.LINK:
        return LeafNode("a", text_node.text, {"href" : text_node.url} )
    if text_node == TextType.IMAGE:
        return LeafNode("img", "", {"src" : text_node.url, "alt" : text_node.text} )
'''


'''
def split_nodes_delimiter( old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type is TextType.TEXT:
            text = node.text
            nodes_text = text.split( delimiter )

            for i, new_text in enumerate(nodes_text):
                if i % 2 == 0:
                    new_nodes.append( TextNode( new_text, node.text_type ) )
                else:
                    new_nodes.append( TextNode( new_text, text_type ) )
        else:
            new_nodes.append( node )

    #if len(new_nodes) == len(old_nodes):
    if len(new_nodes) == len(old_nodes):
        raise Exception( "Error: invalid Markdown syntax" )

    return new_nodes
'''


'''
def extract_markdown_images(text):
    img_matches = re.findall( r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text )
    return img_matches

def extract_markdown_links(text):
    link_matches = re.findall( r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text )
    return link_matches
'''


'''
def split_nodes_image( old_nodes : list[TextNode] ) -> list[TextNode]:
    new_nodes = []

    for node in old_nodes:
        text = node.text
        nodes_text = extract_markdown_images( text )
        
        for pairs in nodes_text:
            image_alt, image_link = pairs
            sections = text.split(f"![{image_alt}]({image_link})", 1)
            
            #The text
            new_nodes.append( TextNode( sections[0], node.text_type ) )
            #The img
            new_nodes.append( TextNode( image_alt, TextType.IMAGE, image_link ) )

            text = sections[1] if len(sections) > 1 else ""

        #if theres leftover text append it
        if len(nodes_text) == 0:
            new_nodes.append( node )
        elif len(text) > 0:
            new_nodes.append( TextNode( text, node.text_type ) )

    return new_nodes

def split_nodes_link( old_nodes : list[TextNode] ) -> list[TextNode]:
    new_nodes = []

    print("")
    print("splitting links")

    for node in old_nodes:
        text = node.text
        nodes_text = extract_markdown_links( text )

        for pairs in nodes_text:
            link_alt, link_url = pairs
            sections = text.split(f"![{link_alt}]({link_url})", 1)
            
            #The text
            new_nodes.append( TextNode( sections[0], node.text_type ) )
            #The link
            new_nodes.append( TextNode( link_alt, TextType.LINK, link_url ) )

            text = sections[1] if len(sections) > 1 else ""

        #if theres leftover text append it
        if len(nodes_text) == 0:
            new_nodes.append( node )
        elif len(text) > 0:
            print( text )
            new_nodes.append( TextNode( text, node.text_type ) )

    return new_nodes
'''


'''
def text_to_textnodes(text):
    nodes = TextNode( text, TextType.TEXT )
    
    #splits code
    node_list = split_nodes_delimiter( [nodes], "`", TextType.CODE )
    
    #bold text
    node_list = split_nodes_delimiter( node_list, "**", TextType.BOLD )

    #italic text
    node_list = split_nodes_delimiter( node_list, "_", TextType.ITALIC )
    
    #image text
    node_list = split_nodes_image( node_list )

    #link text
    node_list = split_nodes_link( node_list )

    return node_list
'''


'''
def markdown_to_blocks( markdown ):
    block_text = markdown.split( "\n\n" )

    for i in reversed( range( len(block_text) ) ):
        block_text[i] = block_text[i].strip()

        if len( block_text[i] ) == 0:
            block_text.remove( block_text[i] )
        
    return block_text

def block_to_block_type(text):
    if re.match(r"^#+ ", text) is not None:
        return BlockType.HEADING
    elif re.search(r"^```\n.*```$", text) is not None:
        return BlockType.CODE
    elif re.search(r"^>.*", text) is not None:
        return BlockType.QUOTE
    elif re.match(r"^- ", text) is not None:
        return BlockType.UNORDERED_LIST
    elif re.match(r"^\d. ", text) is not None:
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
'''


'''
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks( markdown )

    for block in blocks:
        block_type = block_to_block_type( block )

        html_node = HTMLNode(block_type, block)

    print()

    return node
'''

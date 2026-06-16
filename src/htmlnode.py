class HTMLNode:
    def __init__(self, tag : str = None, value : str = None, children = None, props : dict = None ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        out = ""

        if self.props is not None:
            for key, value in self.props.items():
                out += f' {key}="{value}"'
        
        return out
    
    def __repr__(self):
        print( "tag:", self.tag )
        print( "value:", self.value )
        print( "children:", self.children )
        print( "props:", self.props )
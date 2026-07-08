from markdown_blocks import *
import os

def generate_page_recursive( dir_path_content, template_path, dest_dir_path, base_path ):
    if os.path.isfile(dir_path_content):
        generate_page(dir_path_content, template_path, dest_dir_path, base_path)
    else:
        if not( os.path.exists( dest_dir_path ) ):
            os.mkdir( dest_dir_path )
        
        paths = os.listdir( dir_path_content )

        for path in paths:
            path_dir = os.path.join(dir_path_content, path)
            new_dest_path = os.path.join(dest_dir_path, path)

            generate_page_recursive( path_dir, template_path, new_dest_path, base_path )

def generate_page( from_path, template_path, dest_path, base_path ):
    if dest_path.endswith(".md"):
        dest_path = dest_path.replace(".md", ".html")

    print( f"Generating page from {from_path} to {dest_path} using {template_path}" )

    markdown_file = open( from_path )
    markdown = markdown_file.read()
    markdown_file.close()

    html_file = open( template_path )
    html = html_file.read()
    html_file.close()

    raw_html_markdown = markdown_to_html_node( markdown ).to_html()

    title = extract_tiltle( markdown )

    #href="/"

    raw_html = html.replace( "{{ Title }}", title )
    raw_html = raw_html.replace( "{{ Content }}", raw_html_markdown )

    raw_html = raw_html.replace( 'href="/', f'href="{base_path}' )
    raw_html = raw_html.replace( 'src="/', f'src="{base_path}' )

    new_file = open( dest_path, "w" )
    new_file.write( raw_html )
    new_file.close()
    
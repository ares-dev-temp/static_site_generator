import os, shutil

#copy to public
def copy_static( source, destination ):
    print( f"current directory: '{destination}'" )

    if os.path.exists(destination):
        shutil.rmtree( destination )

    recursive_static_copy( source, destination )

def recursive_static_copy(source, destination):
    if not( os.path.exists( destination ) ):
        os.mkdir( destination )

    if os.path.isfile( source ):
        shutil.copy( source, destination )
        print( f"copied file: '{source}' to '{destination}'\n" )
    else:
        dirs = os.listdir( source )

        print( f"Directories: '{dirs}'\n" )

        for dir in dirs:
            new_static_path = os.path.join( source, dir )

            new_public_path = destination if os.path.isfile(new_static_path) else os.path.join( destination, dir )

            recursive_static_copy( new_static_path, new_public_path )


import os, os.path, hashlib, time
#==========================================================================
def createFileSignature (filename):
#==========================================================================
    """CreateFileHash (file): create a signature for the specified file
       Returns a tuple containing three values:
          (the pathname of the file, SHA1 hash)
    """

    f = None
    signature = None
    try:
        filesize  = os.path.getsize(filename)
        f = open(filename, "rb")  # open for reading in binary mode
        hash = hashlib.sha1()
        s = f.read(16384)
        while (s):
            hash.update(s)
            s = f.read(16384)

        hashValue = hash.hexdigest()   
        signature = (hashValue)     
    except IOError:
        signature = None
    except OSError:
        signature = None
    finally:
        if f: 
            f.close()
    return(signature)

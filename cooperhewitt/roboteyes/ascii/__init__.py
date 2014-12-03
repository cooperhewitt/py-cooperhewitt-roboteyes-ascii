import aalib
import Image
import urllib2
import logging

def draw(path, **kwargs):

    w = kwargs.get('width', 80)
    h = kwargs.get('height', 40)

    screen = aalib.AsciiScreen(width=w, height=h)

    fh = open(path, 'rb')

    im = Image.open(fh)
    im = im.convert('L')
    im = im.resize(screen.virtual_size)

    screen.put_image((0, 0), im)
    return screen.render()

if __name__ == '__main__':

    import sys
    import os.path

    path = sys.argv[1]

    if not os.path.exists(path):
        print "404"
        sys.exit(1)

    print draw(path)
    sys.exit(0)

import aalib

def dimensions(im, max_dim=300):

    w,h = im.size

    if w <= max_dim and h <= max_dim:
        return (w, h)

    if w > h:

        wpercent = (max_dim/float(w))

        w = max_dim
        h = int((float(h) * float(wpercent)))
        
    else:

        hpercent = (max_dim/float(h))

        h = max_dim
        w = int((float(w) * float(hpercent)))

    return (w, h)

def draw(im, **kwargs):

    m = kwargs.get('max', 80)
    w,h = dimensions(im, m)

    w = kwargs.get('width', w)
    h = kwargs.get('height', h)

    screen = aalib.AsciiScreen(width=w, height=h)

    im = im.convert('L')
    im = im.resize(screen.virtual_size)

    screen.put_image((0, 0), im)
    return screen.render()

if __name__ == '__main__':

    import sys
    import Image
    import urllib2
    from cStringIO import StringIO

    import optparse

    parser = optparse.OptionParser()
    parser.add_option('--url', dest='url', action='store_true', default=False, help='')
    parser.add_option('--max', dest='max', action='store', default=80, help='')

    (opts, args) = parser.parse_args()

    path = args[0]

    if opts.url:

        rsp = urllib2.urlopen(path)
        fh = StringIO(rsp.read())
        im = Image.open(fh)        

    else:
        im = Image.open(path)

    print draw(im, max=int(opts.max))
    sys.exit(0)

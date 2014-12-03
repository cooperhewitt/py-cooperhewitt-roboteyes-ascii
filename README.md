# py-cooperhewitt-roboteyes-ascii

## Usage

### Simple

	import sys
	import Image

	import cooperhewitt.roboteyes.ascii as ascii

	path = sys.argv[1]
	im = Image.open(path)

	print ascii.draw(im)

### Fancy

	import sys
	import Image
	import urllib2
	from cStringIO import StringIO
	import optparse

	import cooperhewitt.roboteyes.ascii as ascii

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

	print ascii.draw(im, max=int(opts.max))

## See also

* http://jwilk.net/software/python-aalib


import logging

l = logging.getLogger('ahoj')
l.propagate = False


print(l.handlers)
l.setLevel(logging.DEBUG)


sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
l.addHandler(sh)



fh = logging.FileHandler('/tmp/ahoj.log')
l.addHandler(fh)
fh.setLevel(logging.DEBUG)

l.debug('this is debug message')
l.info('this is info message')
l.warning('this is warning message')
l.error('this is error message')
l.critical('this is critical message')
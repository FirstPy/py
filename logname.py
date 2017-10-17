# -*- coding: utf-8 -*-
import logging
logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s %(filename)s %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='mh.log',
                    filemode='w')


logging.debug('debug message')
logging.info('info message')
logging.error('error message')

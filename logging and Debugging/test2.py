import logging as lg
lg.basicConfig(filename = "test2.log",level =lg.DEBUG, format = '%(levelname)s, %(asctime)s, %(name)s, %(message)s')
lg.info("info log included with timestamp.")
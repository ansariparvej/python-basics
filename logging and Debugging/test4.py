# loglevel priority: DEBUG(10)>INFO(20)>WARNING(30)>ERROR(40)>CRITICAL(50)

import logging as lg
lg.basicConfig(filename = "test4.log",level =lg.DEBUG, format = '%(levelname)s, %(asctime)s, %(name)s, %(message)s')

try:
    lg.info("Trying to read a file.")
    with open("pma.txt", 'r'):
        lg.info("Successfully has read the file.")
except Exception as e:
    lg.critical("could not read the file.")
    lg.error(e)
    lg.exception(e)

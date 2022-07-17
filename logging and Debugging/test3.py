# loglevel priority: DEBUG(10)>INFO(20)>WARNING(30)>ERROR(40)>CRITICAL(50)
import logging as lg
lg.basicConfig(filename = "test3.log",level =lg.ERROR, format = '%(levelname)s, %(asctime)s, %(name)s, %(message)s')
lg.info("info log included with timestamp.")

def divide(a,b):
    lg.info("The number entered by user is %s and %s", a,b)
    try:
        lg.info("we are into function.")
        div = a/b
        lg.info("division operation is completed.")
        lg.info("Result of code is %s",div)
        return div
    except Exception as e:
        lg.exception(e)
(divide(5,0))
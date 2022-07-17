# log level priority: DEBUG(10)>INFO(20)>WARNING(30)>ERROR(40)>CRITICAL(50)
import logging as lg

lg.basicConfig(filename="test1.log", level = lg.INFO)

lg.info("info log included.")
lg.warning("warning log included.")
lg.error("error log included.")

l = [1,2,3,4,5,6,7,8,9]

for i in l:
    if i ==2:
        lg.info(l)
        lg.warning("found your required number.")

#lg.shutdown()


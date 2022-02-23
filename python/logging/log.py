#!/usr/bin/env python3
#from asyncio.windows_events import NULL
import logging




if __name__ == "__main__":
    #Setup logging, to screen currently.
    log = logging.getLogger('FORE')
    log.setLevel(logging.DEBUG)

    consoleLogger = logging.StreamHandler()
    fileLogger = logging.FileHandler("test.log")

    formatter = logging.Formatter('%(asctime)s %(levelname)s - %(filename)s: %(message)s')
    consoleLogger.setFormatter(formatter)
    fileLogger.setFormatter(formatter)
    consoleLogger.setLevel(logging.CRITICAL)
    fileLogger.setLevel(logging.INFO)

    log.addHandler(consoleLogger)
    log.addHandler(fileLogger)
    
    log.info('this is atest')
    log.critical('UH OH!')

import logging
logging.basicConfig(filename='all_logs.log',format='%(asctime)s %(levelname)s %(message)s %(lineno)s',filemode='w')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)



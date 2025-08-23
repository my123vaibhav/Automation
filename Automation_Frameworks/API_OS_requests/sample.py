import logging
logging.basicConfig(filename='all_logs.log',format='%(asctime)s %(levelname)s %(message)s %(lineno)s',filemode='w')

logger=logging.getLogger()

logger.setLevel(logging.DEBUG)


logger.debug('this debug')
logger.info('this is info')
logger.warning('this is worning')
logger.error('this is error')
logger.critical('this is critical')
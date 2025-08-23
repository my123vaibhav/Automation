from Helper.requestshelper import RequestHelper
from config.constant import StatusCode
from Helper.logger import get_logs

log=get_logs(__name__)

class HRMHelperClass:
    def get_status_code(self,api,header):
        try:
            obj1=RequestHelper(api)
            log.info('object is created for request helper')
            actual_status_code=obj1.get_information(ex_status=True,header=header)
            log.info(f'actual status code is :{actual_status_code}')
            if actual_status_code == StatusCode.ok:
                log.debug(f'status is match')
                return True
            else:
                return False
        except Exception as e:
            log.error(f'expection as {e}')
            return False

    def get_response(self,api,header):
        '''
        this function is resp to take api and header as args
        :param api: api for the given tc
        :param header:
        :return: will return actual resp
        '''
        try:
            obj1=RequestHelper(api)
            actual_resp=obj1.get_information(ex_resp=True,header=header)
            log.info(f'response is :{actual_resp}')
            return actual_resp
        except Exception as e:
            return False

from Helper_sample import *
class comman_helper:
    def validate_api(self,resp,exstatus_code=200):
        if int(resp.status_code)!=exstatus_code:
            print('Failed')
            return False
        else:
            return True

    def validate_api_post(self,resp,exstatus_code=201):
        if int(resp.status_code)!=exstatus_code:
            print('Failed')
            return False
        else:
            return True

    def validate_api_delete(self,resp,exstatus_code=204):
        if int(resp.status_code)!=exstatus_code:
            print('Failed')
            return False
        else:
            return True


if __name__=='__main__':
    obj=comman_helper()

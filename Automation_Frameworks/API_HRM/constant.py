class Code:
    success=200
    create=201
    accept=202
    nocontent=204
    unth=401
    notfound=404

auth_api='https://the-internet.herokuapp.com/basic_auth'
delay_api='https://reqres.in/api/users?delay=3'
get_api_dict={
    'listuser':"/api/users?page=2",
    'single_user':"/api/users/2",
    "usernotfound":"/api/users/23"

}

post_api_dict={
'createuser':"/api/users",
    'register_success':'/api/register'

}

delete_api_dict={
'user_delete':"https://reqres.in/api/users/2"
}

put_api_dict={
'update_user':'/api/users/2'

}

patch_api_dict={
'update_user':"/api/users/2"

}
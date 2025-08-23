'''this module will take the API , Status code, Delay, auth, Timeout'''

class Constant_values:
    delay=3
    timeout=2
    user_id=2

class Status_code:
    success=200
    created=201   #Status_code.created
    accepted=202
    not_found=404

class DeleteAPI:
    delete_user=f"api/users/{Constant_values.user_id}"

collection_get_call={
    'list_users':f"api/users?page={Constant_values.user_id}",
    'single_user':"api/users/{}".format(Constant_values.user_id),
    'single_user_not_found':f"api/users/{Constant_values.user_id}"+'3',
    'list_resource':"api/unknown",
    'single_resource':f"api/unknown/{Constant_values.user_id}",
    'single_resource_not_found':"api/unknown/23",
    'delay_api':f"api/users?delay={Constant_values.delay}"
}

collection_post_call = {
    'create_user':"api/users",
    'register':"api/register",
    'login':"api/login",
}

collection_update_call={
    'update_users':f"api/users/{Constant_values.user_id}"
}


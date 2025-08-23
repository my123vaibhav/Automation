class StatusCode:
    ok=200
    created=201
    accepeted=202
    nocontent = 204
    badreq=400
    unauth=401
    notfound=404

#getcalls
page_2_api=f"https://reqres.in/api/users?page={{}}"
users_api=f"https://reqres.in/api/users/{{}}"
unknow_user="https://reqres.in/api/unknown"
single_user="https://reqres.in/api/unknown/{}"
delay_api="https://reqres.in/api/users?delay=3"
delay_negative="https://reqres.in/api/users?delay=abc"
unknow_user_abc="https://reqres.in/api/unknown/abc"

#postcalls
create_user_api="https://reqres.in/api/users"
register_api="https://reqres.in/api/register"
login_api="https://reqres.in/api/login"

#put
update_user="https://reqres.in/api/users/2"


#delete

delete_user="https://reqres.in/api/users/2"
delete_non_existing="https://reqres.in/api/users/99999"
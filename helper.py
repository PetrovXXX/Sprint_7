import data


def modify_create_courier_body(key,value):
    body = data.DataForCreatCourier.CREAT_COURIER_BODY.copy()
    body[key]=value
    return body
# -*- coding: utf-8 -*-
import  requests
people = {
    'mahao':{
        'phone':'123',
        'address':'tuniu'
    },
    'zyc':{
        'phone':'234',
        'address':'zijin'
    }
}
lables ={
    'phone':'phone number',
    'address':'home address'
}


name=raw_input('name is:')

key = 'phone'
if name in people:
    print  "%s's  %s is  %s."%(name,lables[key],people[name][key])
    print(people.get(key))
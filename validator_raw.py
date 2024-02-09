from cerberus import Validator

body = {
    "data":{
        "elemento2": 123,
        "elemento": "123"
    }
}

body_validator = Validator({
    "data": {
        "type": "dict",
        "schema": {
            "elemento1": {"type": "float", "required": True, "empty": False},
            "elemento2": {"type": "string", "required": True, "empty": True},
            "elemento3": {"type": "string", "required": False, "empty": False},       
        }
    }
})

response = body_validator.validate(body)

print(response) # True or False

if response is False:
    print(body_validator.errors)
else:
    print("body is valid")

print(body_validator.errors) # {} or {'data': {'elemento1': ['must be of float type']}}

import openaccess_cma.constants as c

def validate_arguments(values):

    if values.get('limit'):
        try:
            if int(values['limit']) <= 0:
            	raise ValueError("limit must be greater than or equal to zero")
        except ValueError:
            raise ValueError("limit must be able to be cast to an integer")

    if values.get('department'):
        if str(values['department']) not in c.VALID_DEPARTMENTS:
            raise ValueError(c.DEPARTMENT_ERROR_MESSAGE)

    if values.get('type'):
        if str(values['type']) not in c.VALID_TYPES:
            raise ValueError(c.TYPE_ERROR_MESSAGE)

    if values.get("created_before"):
        try:
            int(values["created_before"])
        except:
            raise ValueError("created_before must be able to be cast to an integer")

    if values.get("created_after"):
        try:
            int(values["created_after"])
        except:
            raise ValueError("created_after must be able to be cast to an integer")

    if values.get("created_after_age"):
        try:
            int(values["created_after_age"])
        except:
            raise ValueError("created_after_age must be able to be cast to an integer")

    if values.get("created_before_age"):
        try:
            int(values["created_before_age"])
        except:
            raise ValueError("created_before_age must be able to be cast to an integer")

    return None

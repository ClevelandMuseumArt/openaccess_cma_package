import openaccess_cma.constants as c

def validate_arguments(values):

    if values['limit'] is not None:
        try:
            if int(values['limit']) <= 0:
            	raise ValueError("Limit must be greater than or equal to zero")
        except ValueError:
            raise ValueError("Limit must be able to be cast to an integer")

    if values['cc0'] is not None:
        if str(values['cc0']) not in c.VALID_CC0_TYPES:
            raise ValueError(c.CC0_ERROR_MESSAGE)

    if values['department'] is not None:
        if str(values['department']) not in c.VALID_DEPARTMENTS:
            raise ValueError(c.DEPARTMENT_ERROR_MESSAGE)

    if values['type'] is not None:
        if str(type) not in c.VALID_TYPES:
            raise ValueError(c.TYPE_ERROR_MESSAGE)

    if values["created_before"] is not None:
        try:
            int(values["created_before"])
        except:
            raise ValueError("Created before must be able to be cast to an integer")

    if values["created_after"] is not None:
        try:
            int(values["created_after"])
        except:
            raise ValueError("Created after must be able to be cast to an integer")

    if values["created_after_age"] is not None:
        try:
            int(values["created_after_age"])
        except:
            raise ValueError("Created after age must be able to be cast to an integer")

    if values["created_before_age"] is not None:
        try:
            int(values["created_before"])
        except:
            raise ValueError("Created before age must be able to be cast to an integer")

    return None

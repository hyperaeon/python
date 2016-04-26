__author__ = 'hzliyong'


def temp_convet(var):
    try:
        return int(var)
    except (ValueError,var):
        print("The argument does not contain int value,",var)

temp_convet("sdf")
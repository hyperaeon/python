__author__ = 'hzliyong'


def faulty():
    raise Exception("Faulty wrong")


def ignore_exception():
    faulty()


def handle_exception():
    try:
        faulty()
    except:
        print("Exception handled")


# ignore_exception()

handle_exception()

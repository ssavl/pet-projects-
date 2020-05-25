import functools


def auto_try_except(retry_until_success=False):
    def wrap(func):
        @functools.wraps(func)
        def wrapped():
            if retry_until_success:
                succeded = False
                while not succeded:
                    try:
                        func()
                        succeded = True
                    except Exception:
                        print("Failed, not aborting")
            else:
                try:
                    func()
                except Exception:
                    print("Failed, not aborting")
        return wrapped
    return wrap



@auto_try_except(retry_until_success=False)
def failing_func():
    return 1 + '1'


failing_func()




"""Да, сейчас в письменной форме - надо написать декоратор, который принимает аргумент на количество 
попыток ретраев функции в случае какого-либо эксепшена. И ретраит ровно это количество раз, а на 
финальном выкидывает эксепшен, если таковой возникнет """


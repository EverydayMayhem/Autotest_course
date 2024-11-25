def global_function():
    """Нелокальные изменения
    :return: msg
    """
    msg = 1

    def local_function():
        nonlocal msg
        msg = 2

    local_function()


    return msg

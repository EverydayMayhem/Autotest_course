def test_file_path(file_path):
    """Путь до файла
    :param file_path: абсолютный путь до файла
    :return: название файла без расширения, названия диска и корневую папку
    """
    index = (file_path.split("\\"))[-1].rfind(".")
    file_name = (file_path.split("\\"))[-1][:index]
    disk_name = (file_path.split("\\"))[0].strip(":")
    root_folder = (file_path.split("\\"))[1]
    return file_name, disk_name, root_folder

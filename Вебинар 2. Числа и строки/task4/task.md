<html>
<head>
  <meta charset="utf-8" />
  <style>
   .colortext {
    color: orange;
   }
  </style>
 </head>
<h2>Задача 4</h2>
<p>Дан абсолютный путь до файла <code>file_path</code>.
  <br>Внутри функции <code><span class="colortext">test_file_path</span></code> напишите код, который:
<ul>
<li> в переменной <code>file_name</code> вычисляет название файла без расширения;</li>
<li> в переменной <code>disk_name</code> вычисляет название диска;</li>
<li> в переменной <code>root_folder</code> вычисляет корневую папку.</li>
</ul>

<p><b><i>Входные данные:</i></b>
  <ul>
  <li>строка <code>file_path</code> - абсолютный путь до файла
<br>Например, <code>file_path=r'C:\Python311\python.exe'</code>
</li>
</ul>
<p><b><i>Выходные данные:</i></b>
<ul>
  <li>
    <code>file_name</code> - название файла без расширения
<br>Например, <code>file_name='python'</code></li>
<li><p>
    <code>disk_name</code> - название диска
<br>Например, <code>disk_name='C'</code></li>
<li><p>
    <code>root_folder</code> - корневая папка
<br>Например, <code>root_folder='Python311'</code></li>
</ul>

<br>
<p><b>Подсказки:</b>
<div class="hint">
<div>Используйте метод <code>split</code>, чтобы разбить строку по разделителю.</div>
</div>
<div class="hint">
<div>Через обращение по индексу можно извлечь нужную часть пути.</div>
</div>

  <p><b>Материалы:</b>
  <a href="https://n.sbis.ru/shared/disk/6c01b0d9-b2fc-42e1-998a-eaf8a2b3a38f">Вебинар 2</a>
<br>
<br>
</html>
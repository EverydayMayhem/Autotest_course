<html>
<head>
  <meta charset="utf-8" />
  <style>
   .colortext {
    color: orange;
   }
  </style>
 </head>
<h2>Задача 2</h2>
<p>Дан файл <code>'test_file/task_2.txt'</code>. Можно считать, что это запись покупок в магазине, где указана только цена товара. 
<br>В каждой строке файла записана цена товара.
<br>Покупки, т.е. несколько подряд идущих цен, разделены пустой строкой.
<br>Нужно найти сумму трех самых дорогих покупок и записать результат в переменную <code>most_expensive_purchases</code>.
<br>
<br>
<p><b><i>Входные данные:</i></b>
  <ul>
  <li><code>'test_file/task_2.txt'</code> - путь до файла с записями покупок в магазине</li>
</ul>
<p><b><i>Выходные данные:</i></b>
<ul>
  <li>
    <code>most_expensive_purchases</code> - сумма трех самых дорогих покупок.
  </li>
</ul>
<br>
<p><b>Подсказки:</b>
<div class="hint">
<div>Считайте данные из файла с помощью метода <code>readlines</code>.</div>
</div>
<div class="hint">
<div>С помощью функции <code>sorted</code> отсортируйте список цен по возрастанию.</div>
</div>
<div class="hint">
<div>Функция <code>sum</code> поможет найти сумму требуемых элементов.</div>
</div>
<br>
  <p><b>Материалы:</b>
  <a href="https://n.sbis.ru/shared/disk/109a91f7-21f3-427b-851b-9e926ab1cb8a">Вебинар 9</a>
<br>
<br>
</html>
<html>
<head>
  <meta charset="utf-8" />
  <style>
   .colortext {
    color: orange;
   }
  </style>
 </head>
<h2>Задача 7</h2>
<p>Напишите функцию <code><span class="colortext">move_zeros</span></code>,
  который принимает список <code>lst</code> и перемещает все нули в конец, 
сохраняя порядок остальных элементов.
<br>
<br>
<p><b><i>Входные данные:</i></b>
  <ul>
  <li>список типа <code>list</code> из цифр типа <code>int</code></li>
<p>Например, <code>lst=[1, 0, 1, 2, 0, 1, 3]</code>
</ul>
<p><b><i>Выходные данные:</i></b>
<ul>
  <li>
    список типа <code>list</code>
  </li>
</ul>
<br>
<p><b>Пример:</b>
  <pre><code>move_zeros([1, 0, 1, 2, 0, 1, 3]) --> [1, 1, 2, 1, 3, 0, 0]</code></pre>
<br>
<br>
<p><b>Подсказки:</b>
<div class="hint">
<div>Подсчитайте количество нулей в списке с помощью метода <code>count</code>.</div>
</div>
<div class="hint">
<div>С помощью цикла <code>for</code> и метода <code>remove</code> удалите нули из исходного списка.</div>
</div>
<div class="hint">
<div>Полученный список расширьте с помощью метода <code>extend</code> 
на список из нулей длиной, равной количеству нулей в исходном списке.</div>
</div>

<br>
  <p><b>Материалы:</b>
  <a href="https://n.sbis.ru/shared/disk/0cb1a8f2-ef9f-4feb-a5e8-c3d3010b3252">Вебинар 4</a>
<br>
<br>
</html>
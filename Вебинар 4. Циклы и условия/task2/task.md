<html>
<head>
  <meta charset='utf-8' />
  <style>
   .colortext {
    color: orange;
   }
  </style>
 </head>
<h2>Задача 2</h2>
<p>Напишите функцию <code><span class='colortext'>flatten_and_sort</span></code>,
  которая принимает двумерный массив (список списков) чисел <code>array</code>
и возвращает 'плоский' список со всеми числами в порядке возрастания.
<br>
<br>
<p><b><i>Входные данные:</i></b>
  <ul>
  <li>список списков типа <code>list</code>, 
состоящих из чисел типа <code>int</code></li>
<p>Например, <code>array=[[3, 2, 1], [4, 6], [], [5]]</code>
</ul>
<p><b><i>Выходные данные:</i></b>
<ul>
  <li>
    список типа <code>list</code> из чисел типа <code>int</code>
  </li>
</ul>
<br>
<p><b>Пример:</b>
  <pre><code>flatten_and_sort([[3, 2, 1], [4, 6], [], [5]]) --> [1, 2, 3, 4, 5, 6]</code></pre>
<br>
<p><b>Подсказки:</b>
<div class="hint">
<div>Используйте метод <code>extend</code> для получения плоского списка.</div>
</div>
<div class="hint">
<div>Для сортировки воспользуйтесь методом <code>sort</code>.</div>
</div>

<br>
  <p><b>Материалы:</b>
  <a href='https://n.sbis.ru/shared/disk/0cb1a8f2-ef9f-4feb-a5e8-c3d3010b3252'>Вебинар 4</a>
<br>
<br>
</html>
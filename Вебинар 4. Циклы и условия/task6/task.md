<html>
<head>
  <meta charset="utf-8" />
  <style>
   .colortext {
    color: orange;
   }
  </style>
 </head>
<h2>Задача 6</h2>
<p>Напишите функцию <code><span class="colortext">create_phone_number</span></code>,
  которая принимает кортеж <code>num_tuple</code> из 10 цифр 
и возвращает строку из этих цифр в виде номера телефона.
<br>
<br>
<p><b><i>Входные данные:</i></b>
  <ul>
  <li>кортеж типа <code>tuple</code> из цифр типа <code>int</code></li>
<p>Например, <code>num_tuple=(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)</code>
</ul>
<p><b><i>Выходные данные:</i></b>
<ul>
  <li>
    строка типа <code>str</code>
  </li>
</ul>
<br>
<p><b>Пример:</b>
  <pre><code>create_phone_number((1, 2, 3, 4, 5, 6, 7, 8, 9, 0)) --> "(123) 456-7890"</code></pre>
<br>
<br>
<p><b>Подсказки:</b>
<div class="hint">
<div>С помощью генератора списков создайте список, элементами которого являются элементы исходного кортежа,
приведенные к строке.</div>
</div>
<div class="hint">
<div>С помощью метода <code>join</code> можно из списка сделать строку.</div>
</div>
<div class="hint">
<div>Воспользовавшись одним из способов форматирования строк, приведите полученную строку к требуемому виду.</div>
</div>

<br>
  <p><b>Материалы:</b>
  <a href="https://n.sbis.ru/shared/disk/0cb1a8f2-ef9f-4feb-a5e8-c3d3010b3252">Вебинар 4</a>
<br>
<br>
</html>
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
<p>Напишите функцию <code><span class="colortext">get_list_info</span></code>,
  которая принимает список <code>lst</code> из 7 чисел 
и возвращает кортеж <code>min_elem, max_elem, sum_list, average</code>:
<ul>
<li>минимальный элемент списка;</li>
<li>максимальный элемент списка;</li>
<li>сумму всех элементов;</li>
<li>среднее арифметическое с округлением до 2 знаков после запятой.</li>
</ul>
Необходимо сделать эту задачу <b>без использования циклов</b>.
<br>
<br>
<p><b><i>Входные данные:</i></b>
  <ul>
  <li>список типа <code>list</code> из чисел</li>
<p>Например, <code>lst=[1, 2, 3, 4, 5, 6, 7]</code>
</ul>
<p><b><i>Выходные данные:</i></b>
<ul>
  <li>
    кортеж типа <code>tuple</code> из четырех чисел:
<ul>
<li><code>min_elem</code> - минимальный элемент списка</li>
<li><code>max_elem</code> - максимальный элемент списка</li>
<li><code>sum_list</code> - сумма всех элементов</li>
<li><code>average</code> - среднее арифметическое с округлением до 2 знаков после запятой</li>

</ul>
  </li>
</ul>
<br>
<p><b>Пример:</b>
<pre>
  <code># 1 - минимальный элемент списка
# 7 - максимальный элемент списка
# 28 - сумма всех элементов
# 4.0 - среднее арифметическое
get_list_info([1, 2, 3, 4, 5, 6, 7]) --> (1, 7, 28, 4.0)</code>
</pre>
<br>
<p><b>Подсказки:</b>
<div class="hint">
<div>Воспользуйтесь функциями <code>min</code>, <code>max</code>, <code>sum</code>.</div>
</div>
<div class="hint">
<div>Примените формулу для нахождения среднего арифметического чисел 
и запишите её с помощью арифметических операций.</div>
</div>
<div class="hint">
<div>Используйте функцию <code>round</code> для округления.</div>
</div>
<br>
  <p><b>Материалы:</b>
  <a href="https://n.sbis.ru/shared/disk/e9550156-87e9-42b2-b51e-832dc262915e">Вебинар 3</a>
<br>
<br>
</html>
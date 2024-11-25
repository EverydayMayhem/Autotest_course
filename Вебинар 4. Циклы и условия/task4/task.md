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
<p>Напишите функцию <code><span class="colortext">multiplication_chain</span></code>,
  которая принимает положительное число <code>num</code> и возвращает количество раз, 
которое вы должны перемножить цифры числа <code>num</code> и полученных произведений,
пока не получите одну цифру.
<br>
<br>
<p><b><i>Входные данные:</i></b>
  <ul>
  <li>положительное число типа <code>int</code></li>
<p>Например, <code>num=39</code>
</ul>
<p><b><i>Выходные данные:</i></b>
<ul>
  <li>
    число типа <code>int</code>
  </li>
</ul>
<br>
<p><b>Пример:</b>
  <pre><code># num=39 --> 3*9 = 27, 2*7 = 14, 1*4 = 4, 4 - одна цифра, стоп. Итого 3 итерации, ответ - 3
multiplication_chain(39) --> 3</code></pre>
<pre><code># num=999 --> 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, 1*2 = 2, 2 - одна цифра, стоп. Итого 4 итерации, ответ - 4
multiplication_chain(999) --> 4</code></pre>
<pre><code># num=4 --> 4 - уже одна цифра, а значит мы проделали 0 итераций, ответ - 0
multiplication_chain(4) --> 0</code></pre>
<br>
<p><b>Подсказки:</b>
<div class="hint">
<div>Приведите число к строке, чтобы можно было работать с цифрами числа.</div>
</div>
<div class="hint">
<div>Заведите переменную-счетчик для хранения количества перемножений.</div>
</div>
<div class="hint">
<div>Используйте цикл <code>while</code> с проверкой условия количества цифр в числе.</div>
</div>
<div class="hint">
<div>Используйте цикл <code>for</code> и оператор <code>*=</code> для перемножения цифр числа.</div>
</div>
<br>
  <p><b>Материалы:</b>
  <a href="https://n.sbis.ru/shared/disk/0cb1a8f2-ef9f-4feb-a5e8-c3d3010b3252">Вебинар 4</a>
<br>
<br>
</html>
<html>
<head>
  <meta charset='utf-8' />
  <style>
   .colortext {
    color: orange;
   }
    .color_red {
     color: red;
   }
  </style>
 </head>
<h2>Задача 7</h2>
<p>Даны две строки из <b><u>неповторяющихся</u></b> символов <code>first_string</code> и <code>second_string</code>.
<br>Первая строка <code>first_string</code> длиной 3 символа. 
Вторая строка <code>second_string</code> точно содержит символы первой строки в любом порядке.
  <br>Внутри функции <code><span class='colortext'>minimum_length_slice</span></code> напишите код -
<u><b>без использования циклов и условий</b></u>, который находит срез минимальной длины во второй строке, 
содержащий все символы первой строки.

<p><b><i>Входные данные:</i></b>
  <ul>
  <li>строка <code>first_string</code> - строка длиной 3 символа
<br>Например, <code>first_string='wtf'</code>
</li>
<p>
<li>строка <code>second_string</code> - содержит символы первой строки в любом порядке
<br>Например, <code>second_string='brick quz jmpy veldt whangs fox</code>'
<br>Символы первой строки здесь - 'brick quz jmpy veld<span class='color_red'>t w</span>hangs <span class='color_red'>f</span>ox'
</li>
</ul>
<p><b><i>Выходные данные:</i></b>
<ul>
  <li>
     строка <code>min_slice</code> - срез минимальной длины во второй строке <code>second_string</code>, 
содержащий все символы первой строки <code>first_string</code>.
<br>Например, <code>min_slice='t whangs f'</code></li>
</ul>
<br>
<p><b>Подсказки:</b>
<div class="hint">
<div>Используйте метод <code>find</code> 
для нахождения символов первой строки во второй строке.</div>
</div>
<div class="hint">
<div>Найти срез минимальной длины помогут функции <code>min</code>
и <code>max</code>.</div>
</div>

<br>
  <p><b>Материалы:</b>
  <a href='https://n.sbis.ru/shared/disk/6c01b0d9-b2fc-42e1-998a-eaf8a2b3a38f'>Вебинар 2</a>
<br>
<br>
</html>
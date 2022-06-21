var res = await fetch('https://www.googleapis.com/books/v1/volumes?q=鬼滅');
var data = await res.json();

console.log(data); 

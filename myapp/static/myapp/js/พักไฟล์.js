// function hello() {
//     if (document.querySelector("#joinworld").innerHTML === '601 SQDN !!!!!!!')
//     { 
//         document.querySelector("#joinworld").innerHTML = 'สวัสดีครับ เว็บแอปสำหรับฝูง เพิ่งทำการจัดทำ มีอะไรแนะนำบอกได้ครับ ขอบคุณครับ'; 
//     }
//     else 
//     {
//         document.querySelector("#joinworld").innerHTML = '601 SQDN !!!!!!!';
//     }
// }

// //เมื่อเกิด event DOMcontentLoaded ก็คือเมื่อ เพจโหลดเสร็จ ให้รัน funtion hello เมื่อมีการคลิกที่ id ชื่อว่า hello_button
// document.addEventListener('DOMContentLoaded', function() {
// document.querySelector("#hello_button").onclick = hello;
// });

// <button class ="btn btn-secondary" id=hello_button>Hello</button>

// document.addEventListener('DOMContentLoaded', function() {
//     document.querySelector('form').onsubmit = function() {

//     // Send a GET request to the URL
    
//     // const url = ;

//     fetch('https://api.exchangeratesapi.io/latest?base=THB')
//     // Put response into json form
//     .then(response => response.json())
//     .then(data => {
//         // Get currency from user input and convert to upper case
//         const currency = document.querySelector('#currency').value.toUpperCase();

//         // Get rate from data
//         const rate = data.rates[currency];
//         const thai_convert = 1/rate
    
//         // Check if currency is valid:
//         if (rate !== undefined) {
//             // Display exchange on the screen
//             let date = new Date(data.date);
//             document.querySelector('#result1').innerHTML = `1 THB = ${rate.toFixed(8)} ${currency}.`;
//             document.querySelector('#result2').innerHTML = `1 ${currency} = ${thai_convert.toFixed(4)} Bath.`;
//             document.querySelector('#result3').innerHTML = `(update at ${date})`;
//             document.querySelector('#currency').value = '';
//         }
//         else {
//             // Display error on the screen
//             document.querySelector('#result').innerHTML = 'Invalid Currency.';
//         }
//     })
//     // Catch any errors and log them to the console
//     .catch(error => {
//         console.log('Error:', error);
//     });
//     // Prevent default submission
//     return false;
// }
// });
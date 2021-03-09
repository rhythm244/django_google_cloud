function hello() {
    if (document.querySelector("#joinworld").innerHTML === '601 SQDN !!!!!!!')
    { 
        document.querySelector("#joinworld").innerHTML = 'สวัสดีครับ เว็บแอปสำหรับฝูง เพิ่งทำการจัดทำ มีอะไรแนะนำบอกได้ครับ ขอบคุณครับ'; 
    }
    else 
    {
        document.querySelector("#joinworld").innerHTML = '601 SQDN !!!!!!!';
    }
}

//เมื่อเกิด event DOMcontentLoaded ก็คือเมื่อ เพจโหลดเสร็จ ให้รัน funtion hello เมื่อมีการคลิกที่ id ชื่อว่า hello_button
document.addEventListener('DOMContentLoaded', function() {
document.querySelector("#hello_button").onclick = hello;
});


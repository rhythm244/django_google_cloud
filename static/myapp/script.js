function hello() {
    document.querySelector('h1').innerHTML = 'Hello world';
}

document.addEventListener('DOMContentLoaded', function() {
document.querySelector("button").onclick = hello;
});
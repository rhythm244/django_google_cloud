document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').onsubmit = function() {

    // Send a GET request to the URL
    fetch('https://api.exchangeratesapi.io/latest?base=THB')
    // Put response into json form
    .then(response => response.json())
    .then(data => {
        // Get currency from user input and convert to upper case
        const currency = document.querySelector('#currency').value.toUpperCase();

        // Get rate from data
        const rate = data.rates[currency];
        const thai_convert = 1/rate
    

        // Check if currency is valid:
        if (rate !== undefined) {
            // Display exchange on the screen
            let date = new Date(data.date);
            document.querySelector('#result1').innerHTML = `1 THB = ${rate.toFixed(8)} ${currency}.`;
            document.querySelector('#result2').innerHTML = `1 ${currency} = ${thai_convert.toFixed(4)} Bath.`;
            document.querySelector('#result3').innerHTML = `(update at ${date})`;
            document.querySelector('#currency').value = '';
        }
        else {
            // Display error on the screen
            document.querySelector('#result').innerHTML = 'Invalid Currency.';
        }
    })
    // Catch any errors and log them to the console
    .catch(error => {
        console.log('Error:', error);
    });
    // Prevent default submission
    return false;
}
});


// document.addEventListener('DOMContentLoaded', function() 
//         {
//             fetch('https://api.checkwx.com/metar/vtbd,vtbu,vtcc,vtpp,vtsb', 
//             {
//                 headers: {
//                     "X-API-Key": "29c7f5d572ed49019d1d5bddcf",
//                 },
                
//             })
//             .then(response => response.json())
//             .then(data => {
//                 console.log(data.data[0])
//                 for (x in data.data.reverse()) {
//                     document.querySelector("#metra").innerHTML += `${data.data[x]} <br>`;
//                   }
//             })
            
//             return false;
//         })

// document.addEventListener('DOMContentLoaded', function() 
//         {
//             fetch('https://api.checkwx.com/taf/vtbd,vtbu,vtcc,vtpp,vtsb', 
//             {
//                 headers: {
//                     "X-API-Key": "29c7f5d572ed49019d1d5bddcf",
//                 },
                
//             })
//             .then(response => response.json())
//             .then(data => {
//                 console.log(data.data[0])
//                 for (x in data.data.reverse()) {
//                     document.querySelector("#taf").innerHTML += `${data.data[x]} <br>`;
//                   }
//             })
                
//         })


// document.addEventListener('DOMContentLoaded', function() {
//     document.querySelector('#taf_submit').onsubmit = function() {
    
//     var airport = document.querySelector('#taf').value;
//     // Send a GET request to the URL
//     fetch(`https://api.checkwx.com/taf/${airport}`, 
//             {
//                 headers: {
//                     "X-API-Key": "29c7f5d572ed49019d1d5bddcf",
//                 },
                
//             })
//     .then(response => response.json())
//     .then(data => {
//         console.log(data)
//         for (x in data.data.reverse()) {
//             console.log(`Thsi is airport user choose : ${airport}`)
//             let clean_data = data.data[x]
//             let patt = /BECMG|TEMPO/g;
//             let res = patt.test(clean_data);
//             var result = clean_data.match(patt);

//             if (result != null)
//             {
//                 let cleant = clean_data.split(/BECMG|TEMPO/g).filter(Boolean).join(`<br> ${result[x]}`);
//                 console.log(res)
//                 console.log(`This is word match RE ${result}`)
//                 console.log(`It is : ${cleant}`)
//                 document.querySelector("#taf_display").innerHTML += `${cleant}`;
//             }
//             else 
//             {
//                 document.querySelector("#taf_display").innerHTML += `<br> ${clean_data} `;       
//             }
//         }
//     })
//     // Catch any errors and log them to the console
//     .catch(error => {
//         console.log('Error:', error);
//     });

//     document.querySelector('#metra_display').innerHTML = 'test2'

//     return false;
// }
// });

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#taf_submit').onsubmit = function() {
    
    var airport = document.querySelector('#taf').value;
    var airport_ary = airport.split(",");
    // Send a GET request to the URL
    fetch(`https://api.checkwx.com/taf/${airport}`,
            {
                headers: {
                    "X-API-Key": "29c7f5d572ed49019d1d5bddcf",
                },
                
            })
    .then(response => response.json())
    .then(data => {
        for (let x in data.data)
        {
            document.querySelector("#taf_display").innerHTML += `${data.data[x]} <br>`;
        }
    })
    // Catch any errors and log them to the console
    .catch(error => {
        console.log('Error:', error);
    });

    fetch(`https://api.checkwx.com/metar/${airport}`,
            {
                headers: {
                    "X-API-Key": "29c7f5d572ed49019d1d5bddcf",
                },
                
            })
    .then(response => response.json())
    .then(data => {
        //ถ้าจะเพิ่มฟังก์ชั่นในอนาคต ก็เอาข้อมูลใส่ตัวแปล แล้วค่อยไปแสดงผลนอกฟังก์ชั่นทีหลังละกัน
        for (let x in data.data)
        {
            document.querySelector("#metar_display").innerHTML += `${data.data[x]} <br>`;
        }
    })
    // Catch any errors and log them to the console
    .catch(error => {
        console.log('Error:', error);
    });

    return false;
}
});


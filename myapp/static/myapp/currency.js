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


document.addEventListener('DOMContentLoaded', function() 
        {
            fetch('https://api.checkwx.com/metar/vtbd,vtbu,vtcc,vtpp,vtsb', 
            {
                headers: {
                    "X-API-Key": "29c7f5d572ed49019d1d5bddcf",
                },
                
            })
            .then(response => response.json())
            .then(data => {
                console.log(data.data[0])
                for (x in data.data.reverse()) {
                    document.querySelector("#metra").innerHTML += `${data.data[x]} <br>`;
                  }
            })
                
        })

document.addEventListener('DOMContentLoaded', function() 
        {
            fetch('https://api.checkwx.com/taf/vtbd,vtbu,vtcc,vtpp,vtsb', 
            {
                headers: {
                    "X-API-Key": "29c7f5d572ed49019d1d5bddcf",
                },
                
            })
            .then(response => response.json())
            .then(data => {
                console.log(data.data[0])
                for (x in data.data.reverse()) {
                    document.querySelector("#taf").innerHTML += `${data.data[x]} <br>`;
                  }
            })
                
        })



        // then(data => data.forEach((element) => {console.log(element);}))
        //document.querySelector('#weather').innerHTML = `${test}`

        // function populate(thong_list){
        //     // for (k in thong_list) 
        //     // {
        //     //     console.log(k[data])
        //     //     // let li = document.createElement("li");
        //     //     // let node = document.createTextNode('data');
        //     //     // li.appendChild(node);
        //     //     // document.querySelector('#weather').appendChild(li);
        //     // }
        // }
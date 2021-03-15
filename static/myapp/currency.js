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

document.addEventListener('DOMContentLoaded', function() {
            fetch('https://api.checkwx.com/metar/vtbd', 
            {
                headers: {"X-API-Key": "29c7f5d572ed49019d1d5bddcf"}
            })
            .then(response => response.json())
            .then(data => {
                console.log(data)
            })
        })

        // then(data => data.forEach((element) => {console.log(element);}))
// document.addEventListener('DOMContentLoaded', function() {
        //     //defalut เป็น ยูโร
        //     fetch('https://api.exchangeratesapi.io/latest')
        //     .then(response => response.json())
        //     .then(data => {
        //         console.log(data)
        //         const rate_thai = data.rates.THB
        //         // const update = data.date
        //         let date = new Date(data.date);
        //         document.querySelector('#rate_EUR').innerHTML = `1 EUR = ${rate_thai.toFixed(3)} Bath (update at ${date})`
        //     })
        // })

        // document.addEventListener('DOMContentLoaded', function() {
        //     fetch('https://api.exchangeratesapi.io/latest?base=USD')
        //     .then(response => response.json())
        //     .then(data => {
        //         const rate_thai = data.rates.THB
        //         // const update = data.date
        //         let date = new Date(data.date);
        //         document.querySelector('#rate_USD').innerHTML = `1 USD = ${rate_thai.toFixed(3)} Bath (update at ${date})`
        //     })
        // })
        //-----------------------------------------------------------------------------------------------------------------------------
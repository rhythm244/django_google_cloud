document.addEventListener('DOMContentLoaded', function() {
    
    fetch(`/weather_key`,)
        .then(response => response.json())
        .then(data => {
            onRefrech(data.weather_key)
        })
        // Catch any errors and log them to the console
        .catch(error => {
            console.error('Error:', error);
        });
    
    function onRefrech(WEATHER_KEY){
            document.querySelector('#taf_submit').onsubmit = function() {
            
            const airport = document.querySelector('#taf').value;
            const taf_display = document.querySelector("#taf_display")
            taf_display.innerHTML = '';

            loading(taf_display);

            let re = /[^A-Za-z]/g; //split ด้วยทุกตัวที่ไม่ใช้ตัวอักษรภาษาอังกฤษ
            let airport_re = re[Symbol.split](airport);
            
            var url = `https://api.checkwx.com/taf/${airport_re}`
            fetch(url,
            {
                headers: {
                    "X-API-Key": WEATHER_KEY,
                }
            })
            .then(response => response.json())
            .then(data => {
                listOfTaf(data.data);
            })
            // Catch any errors and log them to the console
            .catch(error => {
                console.error('Error:', error);
            });

            return false;
        }
    }
});


//รับค่า data.data เข้ามาในฟังก์ชั่น listOfTaf
function listOfTaf(taf)
    {
        let re = /[^A-Za-z0-9/]/g;
        let result = []; //เก็บค่าที่ได้จากการ split
        let format = []; //เก็บค่าที่ได้จากเปลี่ยน result ที่มี change indicator โดยการเพิ่ม <br> เข้าไป
        let taf_format = []; //ทำให้คำมารวมกัน เพราะตอนแรก split ไว้
        let change_indicator = ['BECMG', 'TEMPO', 'PROB', 'FM']; //ประกาศไว้ตรงนี้ จะได้ไม่รกตรง if และใน if ใช้ includes ถ้ามีคำเหล่านี้ให้เป็น true

        let main = document.createElement('div');
        
        taf_display.innerHTML = '' //ทำให้ loading หายไป

        taf_display.appendChild(main);
        let taf_ul = document.createElement('ul')
        taf_ul.className = 'list-group';
        main.appendChild(taf_ul);
        
        //iterate all airport user input
        for (let i = 0; i < taf.length; i++) {
            result[i] = re[Symbol.split](taf[i]);
            
            //ถ้าไม่เอาตัวแปรใหม่มาเก็บ ค่าที่ได้มันจะเป็นค่าเดิม
            format[i] = result[i].map((item) => {
                if (change_indicator.includes(item)) {
                    item = "<br>" + item;
                    return item;
                }
                else {
                    return item;
                }
            })

            let taf_li = document.createElement('li'); 
            taf_li.className = 'list-group-item';
            taf_format[i] = format[i].join(" ");
            taf_li.innerHTML += taf_format[i];
            taf_ul.appendChild(taf_li);
        }
    }

    document.addEventListener('DOMContentLoaded', function() {

        fetch(`/weather_key`,)
        .then(response => response.json())
        .then(data => {
            onRefrechMetar(data.weather_key)
        })
        // Catch any errors and log them to the console
        .catch(error => {
            console.error('Error:', error);
        });

        function onRefrechMetar(WEATHER_KEY){
                document.querySelector('#metar_submit').onsubmit = function() {
                
                const airport = document.querySelector('#metar').value;
                const metar_display = document.querySelector("#metar_display")
                metar_display.innerHTML = '';
                loading(metar_display);

                let re = /[^A-Za-z0-9/]/g; //split ด้วยทุกตัวที่ไม่ใช้ตัวอักษรภาษาอังกฤษ
                let airport_re = re[Symbol.split](airport);

                var url_metar = `https://api.checkwx.com/metar/${airport_re}`
                
                const option = {
                    headers: {
                        "X-API-Key": WEATHER_KEY,
                    }
                }

                fetch(url_metar, option)
                .then(response => response.json())
                .then(data => {
                    metar_display.innerHTML = listOfMetar(data.data);
                })
                // Catch any errors and log them to the console
                .catch(error => {
                    console.error('Error:', error);
                });
            
                return false;
            }
        }
    });

function listOfMetar(metar)
    {
        const patt = /(BECMG|TEMPO)/g;

        let metar_airport = metar.map(metar => `<li> ${metar.split(patt).join(`<br/>`)}</li>`).join('\n');
        // let metar_clean = metar_airport.map(metar_airport => metar_airport.split(patt).join(""));
        // console.log(metar_clean)
        return `<ul>${metar_airport}</ul>`;
    }

function loading(div_display) {
    var div_load = document.createElement('div');
    const div_strong = document.createElement('strong');
    div_strong.innerHTML = "Loading...";
    const div_spin = document.createElement('div');

    div_display.appendChild(div_load);
    div_load.appendChild(div_strong);
    div_load.appendChild(div_spin);

    div_load.className = 'd-flex align-items-center';
    div_spin.className = 'spinner-border ml-auto text-info';
    div_spin.setAttribute("role", "status");
    div_spin.setAttribute("aria-hidden", "true");
}

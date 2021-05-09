window.onpopstate = function (e) {
    console.log(e.state);
    if (e.state === null) {
        lesson_view.innerHTML = '';
        load.style.display = 'block'
        load.className = 'loader'
        //เพื่อเป็นการเชคว่าอยู่ในช่วง delopment หรือ production
        if (window.location.hostname == "127.0.0.1"){
            window.location.href = 'http://127.0.0.1:8000/lessonlearn' 
        }
        else if (window.location.hostname == 'my-django-gae-304810.et.r.appspot.com'){
            window.location.href = 'https://my-django-gae-304810.et.r.appspot.com/lessonlearn'
        }
    }
    else if (e.state.title == "generate_lesson") {
        generate_lesson(e.state.airport_id)
    }
}

const load = document.querySelector('#load')

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('#dropdown-airport').forEach(button => {
        button.onclick = function() {
            const airport = this.dataset.airport;

            history.pushState({
                airport_id : airport,
                title : "generate_lesson",
            }, "",);
            generate_lesson(airport)
        };
    });
});

//fet url only airport query by id
function generate_lesson(airport)
{
    // history.pushState({ airport : airport} , "", `lessonlearn`);
    const lesson_view = document.querySelector('#lesson_view')
    lesson_view.innerHTML = '';

    const url = `/lessonlearn_filter/${airport}`;
    const att = {
        method: 'POST',
        headers:{
            'X-CSRFToken': getCookie('csrftoken'),
        },
    }

    fetch(url, att)
    .then((response) => response.json())
    .then((data) => {  
        show_data(data, airport)
    })
    .catch((error) => console.error(error));
}

function show_data(data, airport)
{
    data = JSON.parse(data);
    // console.log(data);
    
    //add table head => fill in function
    const { main, table } = th_row();
    
    lesson_view.appendChild(main);
    main.appendChild(table);
 
    data.forEach((item)=> {

        var row = document.createElement('tr');
        for (var key in item['fields']) {
            var cell = document.createElement('td');
            cell.setAttribute('style', 'line-height: auto');
            cell.setAttribute('style', 'width:150px');
            
            //check if item == date_fly and format date
            if ( key == 'date_fly') {
                const date_format = format_date(item['fields'][key])  

                //insert date_format to cellText
                var cellText = document.createTextNode(date_format);
            } else {
                var cellText = document.createTextNode(`${item['fields'][key]}`);
            }
            
            cell.appendChild(cellText);
            row.appendChild(cell);
        }
        var cell = document.createElement('td');
        var btn_detail = document.createElement('button')

        btn_detail.addEventListener('click', () => {

            build_lesson_one(item.pk);
            // history.replaceState({
            //     airport_id : airport,
            //     title : "generate_lesson",
            // }, "",);

            history.pushState({
                airport_id : airport,
                title : "generate_lesson",
            }, "",);

            function build_lesson_one(pk) {
                const lesson_view = document.querySelector('#lesson_view')
                lesson_view.innerHTML = '';

                const url_one = `/lessonlearn_filter_one/${pk}`;
                fetch(url_one, {
                    method: 'GET',
                    headers: {
                        'X-CSRFToken': getCookie('csrftoken'),
                    },
                })
                .then((response) => response.json())
                .then((data) => {
                    gen_card(data) 
                })
                .catch((error) => console.error(error));
            }  
        });

        cell.appendChild(btn_detail);
        row.appendChild(cell);
        btn_detail.innerHTML = "รายละเอียด"; 
        btn_detail.className = 'btn btn-info';   

        table.appendChild(row);
    });
    
    lesson_view.appendChild(main);
    main.appendChild(table);
    

    function th_row() {
        const main = document.createElement('div');
        const table = document.createElement('table');
        table.className = 'table-bordered table-striped';
        const row_th = document.createElement('tr');

        var th = document.createElement('th');
        cell_date = document.createTextNode('วัน เดือน ปี');
        th.appendChild(cell_date);

        var th_title = document.createElement('th');
        cell_title = document.createTextNode('ชื่อเรื่อง');
        th_title.appendChild(cell_title);

        var th_name = document.createElement('th');
        cell_name = document.createTextNode('ชื่อผู้เขียน');
        th_name.appendChild(cell_name);

        var th_airport = document.createElement('th');
        cell_airport = document.createTextNode('สนามบิน');
        th_airport.appendChild(cell_airport);

        var th_detail = document.createElement('th');
        cell_detail = document.createTextNode('รายละเอียด');
        th_detail.appendChild(cell_detail);


        row_th.appendChild(th);
        row_th.appendChild(th_title);
        row_th.appendChild(th_name);
        row_th.appendChild(th_airport);
        row_th.appendChild(th_detail);
        row_th.className = 'table-primary';
        table.appendChild(row_th);
        return { main, table };
    }
    function gen_card(data){
        // console.log(JSON.parse(data));
        data = JSON.parse(data)
    
        const card_container = document.createElement('div');
        card_container.className = 'card text-dark bg-light mb-3" style="max-width: 55rem'
    
        const card_header = document.createElement('div');
        card_header.className = 'card-header';
        const date_format = format_date(data[0]['fields'].date_fly)
        card_header.innerHTML = `วันที่บิน : ${date_format}`;
    
        const card_body = document.createElement('div');
        card_body.className = 'card-body';
    
        const card_title1 = document.createElement('h5');
        card_title1.className = 'card-title';
        card_title1.innerHTML = `ชื่อเรื่อง : ${data[0]['fields'].title}`
        
        const card_title2 = document.createElement('h5');
        card_title2.className = 'card-title';
        card_title2.innerHTML = `สนามบิน : ${data[0]['fields'].airport}`
    
        const card_text = document.createElement('p');
        card_text.className = 'card-text';
        card_text.innerHTML = `${data[0]['fields'].lesson}`

        lesson_view.appendChild(card_container);
        card_container.appendChild(card_header)
        card_header.appendChild(card_body)
        card_body.appendChild(card_title1)
        card_body.appendChild(card_title2)
        card_body.appendChild(card_text)
        
    }
}

//--------------ฟังก์ชั่นที่เอา csrf token มา---------------------------
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }
  //--------------จบ getCookie---------------------------


const format_date = (date) => {
    const monthNames = ["January", "February", "March", "April", "May", "June",
                        "July", "August", "September", "October", "November", "December"];

    //format date format using quite manual
    const dateObj = new Date(date)
    const month = monthNames[dateObj.getMonth()];
    const day = String(dateObj.getDate()).padStart(2, '0');
    const year = dateObj.getFullYear();
    const output = day  + ' ' + month  + ' ' + year; 

    return output;
}
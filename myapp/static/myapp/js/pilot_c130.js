window.onpopstate = function (e) {
    console.log(e.state);
    if (e.state === null){
        load_pilot130(0)
    }
    else if(e.state.title == "load_pilot") {
        load_pilot130(e.state.range)
    }
    else if(e.state.title == "show_data") {
        show_data(e.state.data)
    }
}

document.addEventListener('DOMContentLoaded', function() {  
    document.querySelectorAll('#btn-filter').forEach(button => {
        button.onclick = function() {
            const range = parseInt(this.dataset.pilot);

            history.pushState({
                range : range,
                title : "load_pilot",
            }, "",`/pilot_c130`);

            load_pilot130(range)
        };
    });
    
});

function load_pilot130(range)
{
    const csrftoken = getCookie('csrftoken');
    pilot130_view.innerHTML = "";
    load.style.display = 'block'
    load.className = 'loader'

    const url = `/pilot_c130/${range}`;
    fetch(url, {
      method: "POST",
      headers: {"X-CSRFToken": csrftoken,},
      body: JSON.stringify(),
    })
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
        return response.status(500).json({ message: "Response is not OK." });
      })
      .then((data) => {
        load.style.display = "none";
        if (data) {
          show_data(data);
        }
        return pilot130_view.innerHTML = "No data for you looking for.";;
      })
      .catch((error) => console.error(error));
}

function show_data(data)
{
    //จะทำอย่างไรกับ initial ต้องเขียน flow chart เพิ่ม ****
    data = JSON.parse(data);
    const image_url = `https://storage.googleapis.com/media-bucket-thong-django-2/`;
    
    //create Row
    data.forEach((item) => {
        valid_data()
        
        const { btn_detail, box_image, img, name, afaps, lucky_number, telephone, main, ul } = element(); 
        
        if ( `${item['fields'].picture}` === 'null') {
            img.src = "";
            describe()
        }
        else {
            img.src = `${image_url}${item['fields'].picture}`; 
            box_image.className = 'image'
            box_image.appendChild(img)
            describe()
        }
        
        btn_detail.addEventListener('click', () => {
            load.style.display = 'block'
            load.className = 'loader'
            build_person_one(item.pk);

            history.pushState({
                data : data,
                title : "show_data",
            }, "",`/pilot_c130`);

            function build_person_one(employee_id) {
                pilot130_view.innerHTML = "";

                const url_one = `/person/${employee_id}`;
                fetch(url_one, {
                    //จริงๆต้องเป็น GET เพราะไม่ได้ส่งข้อมูลอะไรเข้าไป แค่รับมาอย่างเดียว
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': getCookie('csrftoken'),
                    },
                })
                .then((response) => response.json())
                .then((data) => {
                    gen_person_one(data)
                    
                    function gen_person_one(data) {
                        data = JSON.parse(data)

                        const name = document.createElement("li");
                        // เพิ่งเอา Test เข้าไปใน element li ได้
                        name.innerHTML = "test"

                        let btn_detail_one = document.createElement('button')
                        btn_detail_one.innerHTML = "Edit"; 
                        btn_detail_one.className = 'btn btn-info'; 
                        
                        btn_detail_one.addEventListener('click', () => {
                            history.pushState({
                                data : data,
                                title : "gen_person_one",
                            }, "",`/pilot_c130`);
                            window.location.href = `/person/${data[0].pk}`;
                        })

                        pilot130_view.appendChild(main);
                        ul.append(name, btn_detail_one)
                        btn_detail.style.display = 'none'
                        load.style.display = 'none'
                    }
                })
                .catch((error) => console.error(error));
            }  
        });

        function describe() {
            name.innerHTML = `<strong> ยศ ชื่อ - สกุล : </strong> ${item['fields'].rank} ${item['fields'].first_name_thai} ${item['fields'].last_name_thai}`;
            afaps.innerHTML = `<strong> ต.ท. </strong> ${item['fields'].afaps}`;
            lucky_number.innerHTML = `Lucky ${item['fields'].lucky_number}`;
            telephone.innerHTML = `<strong> เบอร์ : </strong> ${item['fields'].telephone}`;

            pilot130_view.appendChild(main);
            main.appendChild(box_image);
            main.appendChild(ul);
            ul.append(name, afaps, lucky_number, telephone, btn_detail);
            load.style.display = 'none'
        }
        function valid_data() {
            //รุ่นเตรียม ถ้าเป็น 0 คือไม่รู้ว่ารุ่นอะไรให้แสดงผลเป็น -
            if ( item['fields'].afaps == 0) {
                item['fields'].afaps = '-';
            }
            if ( item['fields'].telephone == null) {
                item['fields'].telephone = '-';
            }
        }
    })
    
}

function element() {
    const main = document.createElement("div");
    main.className = 'pilotc130_box';
    const ul = document.createElement("ul");

    const name = document.createElement("li");
    const afaps = document.createElement("li");
    const lucky_number = document.createElement("li");
    const telephone = document.createElement("li");

    const box_image = document.createElement('div')
    const img = document.createElement('img');

    const btn_detail = document.createElement('button');
    btn_detail.className = 'btn btn-info';
    btn_detail.innerHTML = "รายละเอียด";
    return { btn_detail, img, name, afaps, lucky_number, telephone, main, ul, box_image };
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


document.addEventListener('DOMContentLoaded', function() {

    history.pushState({data: "test"}, "", '/pilot_c130')

    // Use buttons to toggle between views
    const edit_view = document.querySelector('#edit-view')
    const edit_btn = document.querySelector('#edit-info-person')

    edit_view.style.display = 'none';
    edit_btn.addEventListener('click', show_edit_info_person)

    
})

function show_edit_info_person()
{
    const edit_view = document.querySelector('#edit-view')
    const edit_btn = document.querySelector('#edit-info-person')

    if ( edit_btn.innerHTML == 'Hide Edit')
    {
        edit_btn.innerHTML = 'Edit information'
        edit_view.style.display = 'none';
    }
    else //edit_btn == 'Edit information'
    {
        edit_btn.innerHTML = 'Hide Edit'
        edit_view.style.display = 'contents';
    }
}
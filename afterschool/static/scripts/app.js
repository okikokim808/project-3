console.log('ready fready')
$('.signin_form').on('submit', function(e){

    e.preventDefault()
    //console.log('anything')
    var name = $(this).children('.name').val()
    var csrf = $(this).children().eq(0).val()
    
    console.log(y)
    console.log(csrf)
    console.log(name)
    saveURL = 'student_signin/'
    $.ajax({
        url: saveURL,
        method: 'POST',
        data:{
            name: name,
            csrf: csrf,
        },
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", csrf);
        },
        dataType: 'json',
        success:function(json){
            console.log(json)
        },
        error:function(error){
            console.log(error)
        }
    })
})
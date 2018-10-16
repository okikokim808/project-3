$('#signin_form').on('submit','input', function(e){
    e.preventDefault();
    var idxClicked = $(this).index('input');
    saveURL = 'save_restaurant'
    $.ajax({
        url: saveURL,
        method: 'POST',
        data:{
            'array':track_array[idxClicked],
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
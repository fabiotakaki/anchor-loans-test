// create elements input text
$('#go').click(function (argument) {
  var qtd = $('#quantity').val();
  if(qtd < 0 || qtd > 100) {
    alert('Please enter a number between 0 and 100.')
  }else{
    $('#form').html('');
    for(var i=0; i<qtd; i++){
      $('<input/>').attr({ type: 'text', id: 'creditcard'+i, name: 'creditcard'+i, placeholder: 'Enter your credit card number', class: 'form-control form-creditcard'}).appendTo('#form');
    }
  }
});

// keyup input text to validate a credit card
$('#form').on('keyup', 'input', function() {
  var x = $(this);
  $.post( "/validate", { creditcard: $(this).val() }, function( data ) {
    if(data.valid){
      x.css('border-bottom', '1px solid green');
    }else{
      x.css('border-bottom', '1px solid red');
    }
  });
});

// form file submit
$("form#uploadForm").submit(function(){

    var formData = new FormData($(this)[0]);

    $.ajax({
        url: '/validate_file',
        type: 'POST',
        data: formData,
        async: true,
        success: function (data) {
          $('.result-file').html('');
          if(data.error){
            $('.result-file').append('<p class="invalid">'+data.error+'</p>');
            return;
          }
          for(var i=0; i<data.length; i++){
            if(data[i].valid){
              $('.result-file').append('<p class="valid">'+data[i].creditcard+': Valid </p>');
            }else{
              $('.result-file').append('<p class="invalid">'+data[i].creditcard+': Invalid </p>');
            }
          }
        },
        cache: false,
        contentType: false,
        processData: false
    });

    return false;
});
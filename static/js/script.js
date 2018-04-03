$(document).ready(function(){
    $('.form-add-product').on('submit', function(e){
        e.stopPropagation();
        e.preventDefault();

        var parent =  $(this).parent().parent();
        var element = $('img', $(parent));
        var oldOffset = element.offset();
        var img = element.clone().appendTo('body');
        var newOffset = $('#aliments').offset();
        var width = $(img).css('width');
        var height = $(img).css('height');

         $.ajax({
            type:'POST',
            url: $(this).attr('href'),
            data:{},
            success: function(response) {
                $(img).css({
                    'position': 'absolute',
                    'left': oldOffset.left,
                    'top': oldOffset.top,
                    'width': width,
                    'height': height,
                    'zIndex': 1000
                });

                $(img).animate({
                    'top': newOffset.top,
                    'left': newOffset.left,
                'width': 0,
                    'height': 0,
                }, 'slow', function() {
                    $(img).remove();
                });
            }
        });


    });

    // When the user scrolls down 20px from the top of the document, show the button
    window.onscroll = function() {scrollFunction()};

    function scrollFunction() {
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
            document.getElementById("btn-top").style.display = "block";
        } else {
            document.getElementById("btn-top").style.display = "none";
        }
    }

    // When the user clicks on the button, scroll to the top of the document
    $('#btn-top').on('click',function() {
        document.body.scrollTop = 0; // For Safari
        document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
    });

});
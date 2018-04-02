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

});
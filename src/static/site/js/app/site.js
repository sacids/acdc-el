$(document).ready(function(){


    $(".section_item").click(function(){

        var lesson_id   = $(this).attr('wrp_id');
        var section_id  = $(this).attr('id');

        $('.section_item_clr .fa').removeClass('fa-angle-up');
        $('.section_item_clr .fa').addClass('fa-angle-down');
        if($('#'+lesson_id).is(":visible")){
            $('#'+lesson_id).slideUp();
        }else{
            $('#'+lesson_id).slideDown();
            $('#'+section_id+' .section_item_clr .fa').addClass('fa-angle-up')
            $('#'+section_id+' .section_item_clr .fa').removeClass('fa-angle-down');
        }
        
        

    });

    $(".lesson_item").click(function(){
        var video_src   = $(this).attr('lesson_src');
        $("#lesson_content_vid source").attr('src', video_src);
        $("#lesson_content_vid").load();
    });

    $(".section_item, .lesson_item").click(function(){

        var topPos     = $("#scrollable").scrollTop();
        var divPos     = $(this).offset().top - 125;
        $("#scrollable").animate({ scrollTop: divPos+topPos });

        $(".section_item, .lesson_item").removeClass('active_item');
        $(this).addClass('active_item');
    });

  });
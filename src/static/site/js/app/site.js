$(document).ready(function(){


    $(".section_item").click(function(){

        var lesson_id   = $(this).attr('wrp_id');
        $('.lesson_wrp').hide();
        $('#'+lesson_id).slideDown();

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
$ = django.jQuery


 $(document).ready(function() {
	   
	   $("#id_submit_rt").ajaxSend(function(e,xhr,settings){
		   

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = $.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
	var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
	       });	   
		   $("#id_submit_rt").click(function(){
			   left = document.getElementById("id_left")
			       rt = document.getElementById("id_reltype")
			       right = document.getElementById("id_right")
			       absolute_url = document.getElementById("id_back_url")
			       url = "/objects/dynamicRelation/save/"+ left.value + "/" +rt.value+"/"+right.value+"/"
			       // alert(url);
			       $.get(url,function(data){		     
			       	      window.location.replace(absolute_url.value);
			       	   });

		       });      
	   
 });



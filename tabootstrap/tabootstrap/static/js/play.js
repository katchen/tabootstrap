var return_dict = {}
var counter;

$(document).ready(function(){
	var counter = 60;
	function seconds_to_time(sec)
    {
        var minutes = (Math.floor(sec / 60)).toString();
        var seconds = (sec % 60).toString();

        if(seconds.length == 1)
        {
            seconds = "0" + seconds;
        }

        return minutes + ":" + seconds;
    }

    function getContent(startup,banned)
    {

        document.getElementById('startup').innerHTML = startup;
        //var banned = Array(1,2,3);
        var wordlist = "";
        for(i=0;i<banned.length;i++)
        {
          var element = "<li>";
          element += banned[i];
          element += "</li>";
          wordlist+=element;
        }
        document.getElementById('banned').innerHTML = wordlist;
        $('#banned').listview('refresh');
    } 

    function tick () {
		if (counter>0)
		{
			counter-=1;
    		setTimeout ('tick()', 1000);
			$('#counter').html(counter);
		}
		else
		{
			counter = 60
			$('#counter').html("done");
			
		}
    	// if (document.getElementById('counter').data > 0) {
    	// 	document.getElementById('counter').data = document.getElementById ('counter').firstChild.data - 1;
    	// 	setTimeout ('tick()', 1000);
    	// } else {
    	// 	document.getElementById('counter').data = 'done';
    	// }
    }

//    if (document.getElementById('counter')) = function () {
//      console.log("HII");
//      document.getElementById('counter').data = 60;
//    	tick();
//    }

        var prev_words = [];
        $("#getNewSet").click(function(){
            getNewSet();
        })

        function getNewSet(){
            prev_words_string = String(prev_words)
            var data = {};
            data['prev_words'] = prev_words_string;
            $.ajax({
                       type: "GET",
                       url: "./",
                       data: data,
                       success: function(data){
                           data_dict = eval("("+data+")")
                           used_all = data_dict['used_all']
                           new_word = data_dict['taboo_word']
                           new_banned_words = data_dict['banned_words']
                           if (used_all) {
                               prev_words.length = 0
                           }
                           prev_words.push(new_word)
                           setDict(new_word,new_banned_words);

                           // START DOING STUFF WITH DATA HERE
                           // new_word is a string of the new taboo word
                           // new_banned_word is an array of strings, which are the words not allowed to be used


                       }
                   })
        }

        function setDict(new_word,new_banned_words) {
            return_dict['taboo_word'] = new_word;
            return_dict['new_banned_words'] = new_banned_words;
            alert(return_dict['taboo_word'])
        }

        function startCounter(seconds) {
            counter = seconds;
            $("#counter").html(counter)
            var interval = setInterval(function(){counter -= 1;
                $("#counter").html(counter);if (counter == 0) {
                    clearInterval(interval);
                    $("#counter").html("Done")
                }},1000);

        }

        function tick() {

            counter -= 1;
            $("#counter").html(counter)
            if (counter == 0) {
                clearInterval(interval)
            }
        }

        $("#count").click( function() {
            startCounter(3);
        })

    $("#timing").click(function(){
        startCounter(60);


    })
})

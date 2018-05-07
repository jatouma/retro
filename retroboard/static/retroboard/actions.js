document.addEventListener('DOMContentLoaded', () => {
    var buttons = document.querySelectorAll('.complete-btn');
    for(i = 0; i < buttons.length; i++){
        buttons[i].addEventListener('click', function() {
            // Initialize new request
            const request = new XMLHttpRequest();
            request.open('POST', '/complete');

            var csrftoken = Cookies.get('csrftoken');
            request.setRequestHeader("X-CSRFToken", csrftoken);

            // Callback function for when request completes
            request.onload = () => {

                // Extract JSON data from request
                const data = JSON.parse(request.responseText);
                
                if (data.success) {
                    var contents = document.querySelector('#li'+this.id);
                    var item = contents.firstChild.textContent;
                    var li = document.createElement("li");
                    li.appendChild(document.createTextNode(item));
                    li.setAttribute("class", "list-group-item bg-success");
                    document.querySelector("#complete-list").appendChild(li);
                    document.querySelector("#incomplete-list").removeChild(contents);
                }

                //TODO: Error handling
            }
            // Add data to send with request
            const data = new FormData();
            data.append('id', this.id);

            // Send request
            request.send(data);
        });
    }
});

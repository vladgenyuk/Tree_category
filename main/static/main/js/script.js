        let counter = 0;
        my_list = document.getElementById('level2');

        function changeCat(cat){
            my_list.innerHTML = "";
            let note;
            let msg;
            {% for i in cats %}
                {% if i.level == 3 %}
                    note = document.createElement('li');
                    msg = document.createTextNode(cat);
                    note.appendChild(msg);
                    my_list.appendChild(note);
                {% endif %}
            {% endfor %}
        }

        function showCats(title){
            let note = document.createElement('li');
            let msg = document.createTextNode(title);
            note.appendChild(msg);
            my_list.appendChild(note);
        }

        function add(){

        }
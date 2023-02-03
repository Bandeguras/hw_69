    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function onButtonClickClose() {
        let div2 = document.getElementById('note');
        let child = div2.children[0];
        div2.removeChild(child);
    }

    async function buttonClick(event) {
            let target = event.target;
            let url =  target.dataset['indexLink'];
            let a = document.getElementById('first').value;
            let b = document.getElementById('second').value;

            let response = await fetch(url,{
                    method: 'POST',
                    headers: {"X-CSRFToken": getCookie('csrftoken'),
                             "content-type": "application/json"},
                    body:JSON.stringify({a, b}),
            });

            if(response.ok) {
                let index_text = await response.json();
                let div = document.createElement('div')
                div.className='alert';
                div.innerHTML= `<p>Answer is : ${index_text['answer']}</p><button class='button'  onclick='onButtonClickClose()'><i class='bi bi-x-circle'></i></button>`;
                let div2 = document.getElementById('note')
                div2.appendChild(div)
                setTimeout(onButtonClickClose,5000)
            }
            else {

            }
    }

    async function onLoad(){
        const button = document.querySelectorAll(`[id="click_me"]`);
        if(button){
        for(let i of button){
            i.onclick = buttonClick;
        }
        }
    }

    window.addEventListener('load', onLoad)
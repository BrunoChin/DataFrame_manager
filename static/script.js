window.onload = function() {
    const check_null = document.getElementById("checkNull")
    const response_area = document.getElementById("response_area")

    const btn_describe = document.getElementById("btn_describe")

    check_null.onsubmit = function(event) {
        event.preventDefault();
        fetch("/checknull", {
            method: "GET"
        })
        .then(response => {
            return response.blob()
        })
        .then(() => {
            fetch("/get_responce", {
                method: "GET"
            })
            .then(response => {
                return response.text();
            })
            .then(html => {
                response_area.innerHTML = html
            })
        })
    }

    btn_describe.onclick = function(event) {
        event.preventDefault()
        fetch("/describe", {
            method: "GET"
        })
        .then(response => {
            return response.text()
        })
        .then(html => {
            console.log(html)
            response_area.innerHTML = html
        })
    }
}
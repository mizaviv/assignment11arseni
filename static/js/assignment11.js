function fetchUserFE() {
   var user_id = document.getElementsByName('user_id')[0].value;
    fetch(`https://reqres.in/api/users/${user_id}`).then(
        response => response.json()
    ).then((response_obj) => {
        Object.keys(response_obj.data).forEach(key => {
          el = document.getElementsByName(key)[0];
          if (el) {
            if (key == 'avatar') {
              el.setAttribute("src", response_obj.data[key]);
            } else {
                el.value = response_obj.data[key];
            }
          }
        });
        var el = document.getElementById("fe_form");
        if (el) {
          el.setAttribute("style", "display:visible;");
        }
    }
    ).catch(
        error => console.log(error)
    )
}
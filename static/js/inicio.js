$("#boton-usuarios").on("click", getUsers);
 
function getUsers() {
  $.ajax({
    url: "https://randomuser.me/api/?results=5&inc=name,dob,location,picture",
 
    success: function (respuesta) {
    console.log(respuesta.results);
 
      var listaUsuarios = $("#lista-usuarios");
      $("#lista-usuarios").empty();
      $.each(respuesta.results, function (index, elemento) {
        listaUsuarios.append(
        "<div>" +
            "<p>" +
            elemento.name.first +
            "</p>" +
            "<p>" +
            elemento.dob.age +
            "</p>" +
            "<p>" +
            elemento.location.country +
            "</p>" +
            "<img src='" +
            elemento.picture.large +
            "'/>" +
            "<p>"+
            "<br>"+
        "</div>"
        );
      });
    },
    error: function () {
      console.log("No se ha podido obtener la información");
    },
    // para limpiar el contedor antes de desplegar
    
    
  });
}


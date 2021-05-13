$(document).ready(function() {
    $("#contact-form").validate({
      rules: {
        nombre : {
          required: true,
          minlength: 5
        },
        apellido : {
            required: true,
            minlength: 5
          },
        email: {
          required: true,
          email: true
        },
        pais : {
            required: true,
          },
        sexo: {
            required: true,
        },
        categoria: {
            required: true,
        },
        cmbEdades:{
            required: true,
            number: true,
        },
        subjet: {
            required: true,
            minlength: 3
        },
        message: {
            required: true,
            minlength: 3
        }
      },
      messages : {
        nombre: {
          minlength: "El nombre debe tener al menos 3 caracteres"
        },
        apellido: {
            minlength: "El apellido debe tener al menos 3 caracteres"
          },
        email: {
            email: "Debe tener sintaxis de email"
        },
        email: {
            email: "Debe ingresar su pais"
        },
        sexo: {
          required: "Por favor seleciona su sexo",
 
        },
        categoria: {
            required: "Seleccione al menos una categoria",
        },
        cmbMedioss:{
            required: "Debe seleccionar el medio por el cual nos encontró",
            number: true,
        },
        subjet: {
            required: "Ingrese titulo mensaje",
            minlength: "Largo min 3 caracteres"
        },
        message: {
            required: "Ingrese texto del mensaje",
            minlength: "Largo min 3 caracteres"
        }
      
      }
      

      
    });
     
  });
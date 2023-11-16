function updateHiddenFields(form) {
    // Obtener la fila correspondiente al formulario
    var row = form.parentNode.parentNode;

    // Actualizar los campos ocultos con los valores editados
    form.querySelector('input[name="name"]').value = row.cells[0].innerText;
    form.querySelector('input[name="surname"]').value = row.cells[1].innerText;
    form.querySelector('input[name="age"]').value = row.cells[2].innerText;
    form.querySelector('input[name="course"]').value = row.cells[3].innerText;
}

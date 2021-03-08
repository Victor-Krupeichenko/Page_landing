// ответ на комментарий
function addMessages(name, id) {
    document.getElementById("messages-parent").value = id;
    document.getElementById("form-messages").innerText = `${name}, `
}
//
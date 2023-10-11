const addNoteBtn = document.getElementById("add-note")
const noteDialog = document.getElementById("note-dialog")
const formCancel = document.getElementById("form-cancel")

addNoteBtn.addEventListener("click", () => noteDialog.showModal())

formCancel.addEventListener("click", () => noteDialog.close())

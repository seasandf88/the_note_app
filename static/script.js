// Getting the dialog elements from the DOM
const addNoteBtn = document.getElementById("add-note")
const noteDialog = document.getElementById("note-dialog")
const formCancel = document.getElementById("form-cancel")

// Open the Dialog using a built-in method showModal()
addNoteBtn.addEventListener("click", () => noteDialog.showModal())

// Close the Dialog using a built-in method close()
formCancel.addEventListener("click", () => noteDialog.close())

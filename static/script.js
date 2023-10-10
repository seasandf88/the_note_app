const addNoteBtn = document.getElementById("add-note")
const noteDialog = document.getElementById("note-dialog")

function openDialog() {
  noteDialog.showModal()
}

addNoteBtn.addEventListener("click", openDialog)

async function fetchNotes() {
  const respone = await fetch("http://127.0.0.1:5000/users")
}

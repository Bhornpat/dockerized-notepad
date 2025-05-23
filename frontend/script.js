const API_BASE = "http://localhost:8000";  // Adjust if needed
const noteForm = document.getElementById("noteForm");
const noteInput = document.getElementById("noteInput");
const notesList = document.getElementById("notesList");

function loadNotes() {
  fetch(`${API_BASE}/notes`)
    .then(res => res.json())
    .then(data => {
      notesList.innerHTML = '';
      data.forEach(note => {
        const li = document.createElement("li");
        li.textContent = note.text;
        const delBtn = document.createElement("button");
        delBtn.textContent = " 🗑️";
        delBtn.onclick = () => deleteNote(note.id);
        li.appendChild(delBtn);
        notesList.appendChild(li);
      });
    });
}

function deleteNote(id) {
  fetch(`${API_BASE}/notes/${id}`, { method: "DELETE" })
    .then(() => loadNotes());
}

noteForm.addEventListener("submit", e => {
  e.preventDefault();
  const text = noteInput.value;
  fetch(`${API_BASE}/notes`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text })
  }).then(() => {
    noteInput.value = "";
    loadNotes();
  });
});

loadNotes();

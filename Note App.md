# Note App

## Requirements:

1. Ask the user for a first name
2. Display a **"Welcome username"** message
3. Save the name to the local storage.
4. Redirect to the homepage.
5. Home page features:
   - Add a note.
   - View all notes.
   - Search.
6. The notes should be saved inside a file.
7. Built on **Flask**.
8. Commit to Git **regularly**.

## Extra details:

- The notes are cards.
- You can filter through the notes.
- You can add new note.
- The cards has random colors.
- The card has timestamp.
- You can delete the cards individually.
- You can assign custom color for the note.

## Logic:

#### First Step:

```python
if local storage empty:
  show form to enter name
else:
  redirect to homepage
```

#### Second Step:

```python
if there is a note file with the user name:
  1. retrieve notes from file
  2. put the notes inside an array
  3. display them on homepage
else:
  create a new file with the user name
```

#### Add Note:

```python
1. show the add note form
2. submit the form with "post" method to homepage and write to file
```

#### Search:

```python
1. submit the search form to the results page
2. use find() to search existing note for the search parameter
3. display the results on screen
```

#### Delete Note:

```python
1. get the not index from element
2. delete the note from the notes array[index]
3. rerender the notes from the updated array
```

#### Log Out:

```python
allow the user to log out by clearing the local storage but not the notes file
```

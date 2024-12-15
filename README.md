# Student Management System

## Description
The **Student Management System** is a GUI-based application built using Python's `tkinter` and `customtkinter` libraries. It provides a simple interface to manage student records stored in a MongoDB database. Users can perform CRUD (Create, Read, Update, Delete) operations on student data, such as adding new records, editing existing ones, and deleting entries. The application also features a sortable table to view student details.

## Features
- **Add Students**: Easily add student details (name and age) to the MongoDB database.
- **Edit Students**: Modify existing student records directly from the GUI.
- **Delete Students**: Remove unwanted student records.
- **Sortable Table**: View all student records in a table with sortable columns.
- **Dark Mode UI**: The application uses `customtkinter` to provide a modern and visually appealing dark mode theme.

## Technologies Used
- **Python**: Core programming language.
- **tkinter**: For the GUI interface.
- **customtkinter**: For enhanced GUI styling and dark mode.
- **MongoDB**: For database storage and management.
- **pymongo**: Python library to interact with MongoDB.

## Usage
1. **Add Student**:
   - Navigate to the **Add** tab.
   - Enter the student's name and age.
   - Click the **Add Student** button to save the record.

2. **Edit Student**:
   - Select a student from the table.
   - Navigate to the **Edit** tab.
   - Modify the details and click **Save Changes**.

3. **Delete Student**:
   - Select a student from the table.
   - Navigate to the **Delete** tab.
   - Click **Delete Selected Student**.

4. **View Students**:
   - All student records are displayed in the table on the left.
   - Use the column headers to sort by Name or Age.


## Acknowledgments
- The project leverages `customtkinter` for a modern GUI experience.
- MongoDB for efficient NoSQL database management.


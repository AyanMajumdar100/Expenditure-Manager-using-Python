# Expenditure Manager 🧾

## Overview

Expenditure Manager is a Python-based desktop application designed to help users track their daily expenses. The application provides a simple and intuitive interface for adding, viewing, and deleting expenditures. It also automatically calculates and displays the total expenditure. This tool is perfect for personal budgeting and expense management.

## Tech Stack

- **Language**: Python
- **GUI Framework**: Tkinter
- **Data Handling**: Python Lists
- **Deployment**: Standalone Desktop Application

## Project Structure

The project is organized into a single Python file that contains the following components:

### Components

- **Main Window**: The primary interface where users interact with the app.
- **Input Fields**: Fields for entering expenditure descriptions and amounts.
- **Buttons**:
  - **Add Expenditure**: Adds a new expenditure to the list.
  - **Delete Selected**: Removes the selected expenditure from the list.
- **Listbox**: Displays all added expenditures.
- **Total Label**: Shows the total amount of all expenditures.

### Methods

- **add_expenditure()**: Adds a new expenditure to the list and updates the total.
- **delete_expenditure()**: Deletes the selected expenditure from the list and updates the total.
- **update_expenditure_listbox()**: Refreshes the listbox to display all expenditures.
- **update_total_expenditure()**: Calculates and displays the total of all expenditures.

## Running the Project

To run the Expenditure Manager on your local machine:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/AyanMajumdar100/Expenditure-Manager-using-Python.git
    cd ExpenditureManager
    ```

2. **Run the Python script:**
    ```bash
    python main.py
    ```

## Features

### User Features

- **Add Expenditure**: Users can enter a description and amount to add a new expenditure.
- **View Expenditures**: The listbox displays all added expenditures with their respective amounts.
- **Delete Expenditure**: Users can select and delete any expenditure from the list.
- **Automatic Total Calculation**: The total expenditure is automatically updated and displayed as items are added or removed.

## Environment Variables

This project doesn't require environment variables as it runs directly on the desktop using Python.

## Future Enhancements

- **Persistent Data Storage**: Save and load expenditures from a file to maintain data across sessions.
- **Advanced Reporting**: Generate reports and charts for better expense analysis.
- **Categorization**: Allow users to categorize expenditures for more detailed tracking.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

---

Feel free to reach out if you have any questions or need further assistance with the project. Happy budgeting with Expenditure Manager!

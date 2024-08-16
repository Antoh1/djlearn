
---

# Task Manager

A simple task management application built with Django. This application allows users to create, update, delete, and view tasks, helping individuals or teams stay organized and track their progress.

## Features

- **User Authentication**: Register, log in, and manage user accounts.
- **Task Management**: Create, edit, and delete tasks.
- **Task Status**: Mark tasks as complete or incomplete.
- **Due Dates**: Set and view due dates for tasks.
- **Task Prioritization**: Assign priorities to tasks for better organization.
- **Search and Filter**: Easily search and filter tasks by status, priority, or due date.

## Technologies Used

- **Django**: Web framework used for building the application.
- **SQLite**: Default database used for local development. Can be swapped with other databases like PostgreSQL or MySQL.
- **Bootstrap**: CSS framework used for styling the frontend (optional, adjust according to your setup).

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/Antoh1/djlearn.git
   cd djlearn
   ```

2. **Create a virtual environment**

   ```
   virtualenv venv
   ```

3. **Activate the virtual environment**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages**

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply database migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (admin user)**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**

   ```bash
   python manage.py runserver
   ```

8. **Open your browser** and navigate to `http://127.0.0.1:8000/` to see the application in action.

## Usage

- **Homepage**: View a list of tasks.
- **Task Creation**: Add new tasks by filling out the form on the "Create Task" page.
- **Task Management**: Edit or delete tasks by navigating to the task detail page.
- **Task Filtering**: Use the search bar and filters to find specific tasks.

## Running Tests

To run the test suite, use:

```bash
python manage.py test
```

## Deployment

For deployment, you can use platforms like Heroku, AWS, or any other cloud service. Make sure to:

- Set up environment variables for sensitive data (like `SECRET_KEY`).
- Configure the database settings according to the production environment.
- Collect static files with:

  ```bash
  python manage.py collectstatic
  ```

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions, feel free to contact [antotiro@gmail.com](mailto:antotiro@gmail.com).

---

Feel free to adjust the sections according to your project's specifics and personal preferences!
# Django To-Do List Application

A feature-rich task management application built with Django that allows users to create, read, update, and delete tasks.

## Features

- Create new tasks with title, description, and due date
- View list of all tasks
- View detailed information for each task
- Update existing tasks
- Delete tasks
- Mark tasks as complete/incomplete
- Modern and responsive UI design

## Technologies Used

- Python 3.x
- Django
- SQLite3
- HTML5
- CSS3

## Setup and Installation

1. Clone the repository
```bash
git clone https://github.com/PrajwalMalokar/crud_project.git
cd crud_project
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install required packages
```bash
pip install django
```

4. Apply migrations
```bash
python manage.py migrate
```

5. Run the development server
```bash
python manage.py runserver
```

6. Open your browser and navigate to `http://127.0.0.1:8000`

## Project Structure

```
crud_project/
├── crud_project/          # Project configuration directory
│   ├── settings.py        # Project settings
│   ├── urls.py           # Project URL configuration
│   └── wsgi.py           # WSGI configuration
├── to_do_app/            # Main application directory
│   ├── models.py         # Data models
│   ├── views.py          # View functions
│   ├── urls.py           # URL patterns
│   ├── static/           # Static files (CSS, JS)
│   └── templates/        # HTML templates
├── manage.py             # Django management script
└── README.md            # Project documentation
```

## Usage

1. **Creating a Task**
   - Click on "Create New Task"
   - Fill in the task details
   - Click "Save"

2. **Viewing Tasks**
   - All tasks are displayed on the home page
   - Click on a task title to view details

3. **Updating a Task**
   - Click on the task to view details
   - Click "Edit"
   - Modify the task details
   - Click "Save"

4. **Deleting a Task**
   - Click on the task to view details
   - Click "Delete"
   - Confirm deletion

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Prajwal Mohan Malokar
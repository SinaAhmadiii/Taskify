# Taskify

Taskify is a web application built with Django that allows users to manage and organize their tasks effectively. It provides a user-friendly interface for creating, updating, and tracking tasks, ensuring that nothing falls through the cracks.

## Features

- **Task Creation**: Easily create new tasks by providing a title, description, due date, and priority level.
- **Task Management**: View, update, and delete tasks from the intuitive user interface.
- **Task Filtering**: Filter tasks based on their priority or due date, helping you focus on what's most important.
- **Task Sorting**: Sort tasks by title, due date, or priority to streamline your workflow.
- **Task Completion**: Mark tasks as complete when you finish them, keeping your task list up to date.
- **User Authentication**: Secure user registration and login system to protect your tasks and ensure privacy.
- **User Profiles**: Personalize your profile by adding a profile picture and customizing your preferences.
- **Responsive Design**: Enjoy a seamless experience across devices, whether it's a desktop, tablet, or mobile.

## Installation

1. Clone the repository:

```shell
git clone https://github.com/SinaAhmadiii/Taskify.git
```

2. Change to the project's directory:

```shell
cd Taskify
```

3. Create a virtual environment:

```shell
python -m venv venv
```

4. Activate the virtual environment:

On macOS and Linux:

```shell
source venv/bin/activate
```

On Windows:

```shell
venv\Scripts\activate
```

5. Install the project dependencies:

```shell
pip install -r requirements.txt
```

6. Run database migrations:

```shell
python manage.py migrate
```

7. Start the development server:

```shell
python manage.py runserver
```

8. Open your web browser and visit `http://localhost:8000` to access Taskify.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please submit an issue or a pull request. Make sure to follow the project's code of conduct.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- Taskify uses the Django framework, which provides a solid foundation for building web applications.
- We would like to express our gratitude to the open-source community for their valuable contributions.

## Contact

If you have any questions or feedback, feel free to reach out to us at sinaahmadi615@gmail.com.

Happy task management with Taskify!
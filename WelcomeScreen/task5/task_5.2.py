print("=== Команды задачи 5.2 ===")

commands = [
    'python -m pip install "packaging==24.0"',
    'python -m pip install "packaging==21.0"',
    'python -c "import packaging; print(packaging.__version__)"',

    'py -m venv project_a/.venv',
    'py -m venv project_b/.venv',

    'project_a/.venv/Scripts/python -m pip install "packaging==21.0"',
    'project_b/.venv/Scripts/python -m pip install "packaging==24.0"',

    (
        'project_a/.venv/Scripts/python '
        '-c "import packaging; print(\'A:\', packaging.__version__)"'
    ),

    (
        'project_b/.venv/Scripts/python '
        '-c "import packaging; print(\'B:\', packaging.__version__)"'
    ),
]

for command in commands:
    print(">", command)
print("=== Команды задачи 6.1 ===")

commands = [
    "winget install astral-sh.uv",
    "uv --version",
    "uv venv .venv",
    "uv venv --python 3.12 .venv312",
    "uv pip install requests --python .venv",
    "uv pip list --python .venv",
    "uv pip freeze --python .venv",
    "uv python list",
    "uv python install 3.13",
]

for command in commands:
    print(">", command)

print(
    "\nДополнительное задание: "
    "сравнить установку 50 пакетов "
    "через pip и uv."
)

print(
    "> python -m pip install "
    "-r requirements-50.txt"
)

print(
    "> uv pip install "
    "-r requirements-50.txt --python .venv"
)
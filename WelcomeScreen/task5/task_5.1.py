import site
import sys

print("Исполняемый файл:", sys.executable)
print("Префикс:", sys.prefix)
print("Базовый префикс:", sys.base_prefix)

print(
    "В виртуальном окружении?",
    sys.prefix != sys.base_prefix
)

print(
    "site-packages:",
    site.getsitepackages()
)

print("\n=== Команды PowerShell ===")

commands = [
    "py -m venv .venv",
    ".venv\\Scripts\\Activate.ps1",
    "where.exe python",
    "python -V",
    "pip list",
    "pip install six",
    "pip list",
    "deactivate",
    "where.exe python",
]

for command in commands:
    print(">", command)
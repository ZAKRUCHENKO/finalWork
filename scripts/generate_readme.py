import tomllib  # Встроен в Python 3.11+. Для более старых версий: pip install tomli
import subprocess
from pathlib import Path
from jinja2 import Template


def get_project_metadata():
    """Читает метаданные из pyproject.toml"""
    with open('pyproject.toml', 'rb') as f:
        data = tomllib.load(f)
    return data['project']


def get_installed_version(package_name):
    """Получает установленную версию пакета (например, selenium)"""
    try:
        result = subprocess.run(
            ['pip', 'show', package_name],
            capture_output=True, text=True, check=True
        )
        for line in result.stdout.split('\n'):
            if line.startswith('Version:'):
                return line.split()[1]
        return 'N/A'
    except subprocess.CalledProcessError:
        return 'Not installed'


def get_project_structure(startpath='.'):
    """Генерирует текстовое дерево структуры проекта (опционально)"""
    ignore_dirs = {'.git', '__pycache__', 'venv', '.pytest_cache'}
    lines = []
    for path in sorted(Path(startpath).rglob('*')):
        if any(part in ignore_dirs for part in path.parts):
            continue
        depth = len(path.relative_to(startpath).parts)
        indent = '    ' * depth
        lines.append(f"{indent}{path.name}")
    return '\n'.join(lines)


def main():
    # Читаем данные
    metadata = get_project_metadata()

    # Подготавливаем контекст для шаблона
    context = {
        'project_name': metadata['name'],
        'description': metadata['description'],
        'python_version': metadata['requires-python'].lstrip('>='),
        'license': metadata.get('license', {}).get('text', 'N/A'),
        'author_name': metadata['authors'][0]['name'],
        'author_email': metadata['authors'][0]['email'],
        'github_username': 'your-github-username',  # Захардкодьте или вынесите в config
        'browser_name': 'Chrome',  # Или другой браузер по умолчанию
        'selenium_version': get_installed_version('selenium'),
        'dependencies': metadata['dependencies'],
        'project_structure': get_project_structure()
    }

    # Читаем и рендерим шаблон
    template_path = Path('scripts/readme_template.md')
    template_content = template_path.read_text(encoding='utf-8')
    template = Template(template_content)
    rendered_readme = template.render(context)

    # Записываем результат
    output_path = Path('README.md')
    output_path.write_text(rendered_readme, encoding='utf-8')
    print(f"✅ README.md успешно сгенерирован!")


if __name__ == '__main__':
    main()
import re

# Укажите пути к вашим HTML и CSS файлам
html_file = "index.html"
css_file = "css/style.css"

# Считываем содержимое HTML
with open(html_file, "r", encoding="utf-8") as file:
    html_content = file.read()

# Ищем все классы в HTML
classes = re.findall(r'class="(.*?)"', html_content)
unique_classes = set(".".join(class_name.split()) for class_name in classes)

# Генерируем CSS
with open(css_file, "a", encoding="utf-8") as file:
    for class_name in unique_classes:
        if class_name.strip():
            file.write(f"{class_name} {{\n\n}}\n\n")

print("CSS-классы успешно добавлены в файл.")

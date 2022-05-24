# Анализ статей из интернета на соответствие тематике по коэффиценту Жаккарда и метрике Косинуса

### [GoogleDoc с результатами и объяснением](https://docs.google.com/document/d/1acXeYt0b2bmOz8c03dVzOKWsd2qcA-_5MPrzIWTT5g4/edit?usp=sharing)
## Первоначальный запуск
```
pip install requirements.txt
python main.py
```
## Структура проекта
- **main.py** - основной скрипт;
- Скрипт берет ключевые слова для четырех тематик *(новости, спорт, шоппинг, наука)* из папки **keywords**;
- **website_text.txt** и **website_text_alt.txt** - анализируемые статьи.

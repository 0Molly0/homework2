from pywebio.input import input as pw_input
from pywebio.output import put_success, put_markdown, popup

favorite_dish = pw_input('Введіть свою улюблену страву ').lower()
put_success(favorite_dish)

result = f'О, я теж люблю {favorite_dish} \U00002605'
put_markdown(result)
popup(result)

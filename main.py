import sys
import argparse
from queries.my_select import (
    select_1, select_2, select_3, select_4, select_5,
    select_6, select_7, select_8, select_9, select_10
)
from cli.cli_app import main as cli_main

def test_queries():
    print("1. Топ-5 студентів за середнім балом:")
    print(select_1())
    
    print("\n2. Студент із найвищим середнім балом з предмета (id=49):")
    print(select_2(49))
    
    print("\n3. Середній бал у групах з предмета (id=49):")
    print(select_3(49))
    
    print("\n4. Середній бал на потоці:")
    print(select_4())
    
    print("\n5. Курси, які читає викладач (id=1):")
    print(select_5(1))
    
    print("\n6. Студенти в групі (id=19):")
    print(select_6(19))
    
    print("\n7. Оцінки студентів у групі (id=19) з предмета (id=49):")
    print(select_7(19, 49))
    
    print("\n8. Середній бал, який ставить викладач (id=1):")
    print(select_8(1))
    
    print("\n9. Курси, які відвідує студент (id=295):")
    print(select_9(295))
    
    print("\n10. Курси, які студенту (id=295) читає викладач (id=1):")
    print(select_10(295, 1))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cli_main()  # Якщо передані аргументи, виконуємо CLI
    else:
        test_queries()  # Інакше запускаємо SQL-запити

import requests
import matplotlib.pyplot as plt
try:
    response = requests.get("https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/opendata.stat")
    response.raise_for_status() 
    fail = response.text
    month = []
    cnt = []
    k = 0
    a = [x for x in fail.split("\n") if x != ""]
    for i in a:
        s = [u for u in i.split(",") if u != ""]
        if len(s) >= 4:
            if (s[0] == 'Средняя пенсия' and s[1] == 'Забайкальский край' and (s[2].split('-'))[0] == '2018'):
                cnt.append(float(s[3]))
                k += 1
                month.append((s[2].split('-'))[1])
    if k > 0:
        print(f"Средняя пенсия в Забайкальском крае за 2018 год: {sum(cnt)/k} рублей")
    else:
        print("Нет данных за 2018 год по Забайкальскому краю")
    plt.plot(month, cnt)
    plt.title('Динамика средней пенсии в Забайкальском крае за 2018 год')
    plt.xlabel('Месяц')
    plt.ylabel('Средняя пенсия (руб)')
    plt.show()
except Exception as e:
    print(f"Ошибка: {e}")
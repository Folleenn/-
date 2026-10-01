import sched
import time


s = sched.scheduler(
    time.time,
    time.sleep
)

start = time.time()


def say(text):
    elapsed = time.time() - start

    print(
        f"[{time.strftime('%H:%M:%S')}] "
        f"{text} | +{elapsed:.1f} c"
    )


s.enter(
    0.5,
    1,
    say,
    ("Прошло 0.5 секунды",)
)

s.enter(
    1,
    1,
    say,
    ("Прошла 1 секунда",)
)

s.enter(
    2,
    0,
    say,
    ("Прошло 2 секунды (приоритет 0)",)
)

s.enter(
    2,
    1,
    say,
    ("Прошло 2 секунды (приоритет 1)",)
)

s.enterabs(
    start + 3,
    1,
    say,
    ("Абсолютное время t0+3 c",)
)


print("Старт. Отсчёт времени от t0 = 0")

print(
    "Очередь до run():",
    len(s.queue),
    "задач"
)

s.run()

print(
    "Готово. Пустая очередь?",
    s.empty()
)
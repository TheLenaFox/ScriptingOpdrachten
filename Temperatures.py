import random
import time

def get_temperature():
    return round(15 + 10 * random.randint(0,5), 2)

def collect_data(duration, interval):
    temperatures = []
    end_time = time.time() + duration
    while time.time() < end_time:
        temperature = get_temperature()
        print(f"Temperatuur gemeten: {temperature}°C")
        temperatures.append(temperature)
        time.sleep(interval)
    return temperatures

def avarage_temperature(temperatures):
    return round(sum(temperatures) / len(temperatures), 2)
def max_temperature(temperatures):
    return max(temperatures)
def min_temperature(temperatures):
    return min(temperatures)

def main():
    duration = 10
    interval = 1
    temperatures = collect_data(duration, interval)
    print(f"Gemiddelde temperatuur: {avarage_temperature(temperatures)}°C")
    print(f"Hoogste temperatuur: {max_temperature(temperatures)}°C")
    print(f"Laagste temperatuur: {min_temperature(temperatures)}°C")

if __name__ == "__main__":
    main()
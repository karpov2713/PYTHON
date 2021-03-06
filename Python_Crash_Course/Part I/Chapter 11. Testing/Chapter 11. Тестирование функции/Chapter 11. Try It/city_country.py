from city_function import get_city_country_names

print("Enter 'q' at any time to quit.")
while True:
    city = input("\nPlease give me a City name: ")
    if city == 'q':
        break
    country = input("Please give me a Country name: ")
    if country == 'q':
        break

    full_city_country_name = get_city_country_names(city, country)
    print(f"\tNeatly formatted name: {full_city_country_name}")


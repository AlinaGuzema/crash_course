cities = {
    'Tokyo': {
        'country': 'Japan',
        'population': 'approximately 14 million',
        'fact': 'Tokyo is the most populous metropolitan area in the world.'
    },
    'New York': {
        'country': 'USA',
        'population': 'approximately 8.4 million',
        'fact': 'New York City is known as the "Big Apple".'
    },
    'London': {
        'country': 'United Kingdom',
        'population': 'approximately 8.9 million',
        'fact': 'London has been a major settlement for two millennia.'
    }
}
for city, info in cities.items():
    print(f"{city}:")
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact']}")
    print()
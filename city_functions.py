# city_functions.py

def city_country(city, country, population=None, language=None):
    """Return a string in the form:
    - 'City, Country'
    - 'City, Country - population xxx'
    - 'City, Country - population xxx, Language'
    depending on which arguments are provided.
    """
    if population and language:
        return f"{city}, {country} - population {population}, {language}"
    elif population:
        return f"{city}, {country} - population {population}"
    else:
        return f"{city}, {country}"


# Call the function at least three times
print(city_country("New York", "United States"))                     # City, Country
print(city_country("Paris", "France", 2148000))                      # City, Country, Population
print(city_country("Tokyo", "Japan", 13960000, "Japanese"))          # City, Country, Population, Language


dial_codes = [
    (880, "Bangladesh"),
    (55, "Brazil"),
    (86, "China"),
    (91, "India"),
    (62, "Indonesia"),
    (81, "Japan"),
    (234, "Nigeria"),
    (92, "Pakistan"),
    (8, "United States"),
    (1, "United States"),
]
print(dial_codes)
country_dial = {country: code for code, country in dial_codes}
print(country_dial)
upper_country = {
    code: country.upper() for country, code in sorted(country_dial.items()) if code < 70
}
print(upper_country)

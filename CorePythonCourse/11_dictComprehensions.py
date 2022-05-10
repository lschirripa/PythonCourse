from pprint import pprint as pp

country_to_capital = {  'United Kingdom' : 'London',
                        'Brasil' : 'Brasilia',
                        'Morocco' : 'Rabat',
                        'Sweden' : 'Stockholm',
                        'Argentina' : 'Buenos Aires',
                    }

capital_to_country = { capital: country for country, capital in country_to_capital.items() }

pp(capital_to_country)
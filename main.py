from pyscript import display


restaurant_name = 'Frankies' # String
owner_name= "Ed Firmalo" # String
year_established= '2012' # Integer
business_hours1= '10' # Integer
business_hours2= '2' # Integer


display (f'{restaurant_name}', target='div1')

display(f'By: {owner_name}', target='div1')
display(f'Since: {year_established}', target='div1')
display(f'{business_hours1}AM- {business_hours2}AM', target='div2')
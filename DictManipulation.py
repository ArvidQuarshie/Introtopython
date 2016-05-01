#mapping of state to the abbreviation
states={
    'Oregon':'OR',
    'Florida':'FL',
    'Calofornia':'CA',
    'NewYork':'NY',
    'Michigan':'MI'
    }
#create a basic set of states  and some cities
cities={
    'CA':'San Francisco',
    'MI':'Detroit',
    'FL':'Jacksonville'
    }
#add some more cities
cities['NY']='NewYork'
cities['OR']='Porteland'

# print out some states using the cities dict
print '_' * 10
print "michigan's abbreviation is:",states['Michigan']
print "florida's abbreviation is:",states['Florida']


#print every state abbreviation
print '_' * 10
for state,abbrev in states.items():
        print "%s is abbreviated %s" %(abbrev,cities)
#now do both at the same time
print '_' * 10
for state,abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" %(states,abbrev,cities[abbrev])

print '_' * 10
#safely get abbreviation of a state that might not be there
state=states.get("Texas")

if not state:
     print "Sorry no texas"

#get a city with a default value
city=cities.get('Tx','Sorry does not exist')
print "The city for the state 'TX' is: %s" % city

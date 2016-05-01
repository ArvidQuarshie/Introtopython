import hashmap

#create a mapping of state to abbreviation
states=hashmap.new()
hashmap.set(states,'Oregon','OR')
hashmap.set(states,'Florida','FL')
hashmap.set(states,'California','CA')
hashmap.set(states,'NewYork','Ny')
hashmap.set(states,'Michigan','MI')

#create a basic set of states and some cities
cities=hashmap.new()
hashmap.set(cities,'CA', 'San Francisco')
hashmap.set(cities,'Mi', 'Detroit')
hashmap.set(cities,'FL', 'Jacksonville')

#add some more cities
hashmap.set(cities,'NY','NewYork')
hashmap.set(cities,'OR','Portland')

#print out some cities
print'_' * 10
print "NY State has %s" %hashmap.get(cities,'Ny')
print "OR State has %s" %hashmap.get(cities,'OR')

#print some states
print '_' * 10
print "Michigan's abbreviation is:%s" %hashmap.get(states,'Michigan')
print "Florida's abbreviation is:%s" %hashmap.get(states,'Florida')


#do it by using the state then cities dict
print '_' * 10
print "Michigan has %s" %hashmap.get(cities,hashmap.get(states,'Michigan'))
print "Florida has %s" %hashmap.get(cities,hashmap.get(states,'Florida'))

#print every state abbreviation
prin t'_' * 10
hashmap.list(cities)

print '_' * 10
state=hashmap.get(states,'Texas')
if not state:
    print"sorry no texas"

#default values using || = with the nil result
#can you do this on one line?

city=hashmap.get(cities,'Tx','Does Not Exist')
print "The city for the state 'Tx' is: %s" %city




































































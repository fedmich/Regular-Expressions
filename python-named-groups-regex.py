import re

#Unit testing
phrases = []
phrases.append( "between Nov 13 and December 15th" )	#Your example
phrases.append( "between Nov 2 and December 21st" )
phrases.append( "between Nov 6 and December 22nd" )
phrases.append( "between Noov13 and Decc1" )		#WRONG
phrases.append( "between Nov 6 and May 3rd" )
phrases.append( "between Nov 13 and December 1" )


#RegEx pattern
#English dates only
#Handles, 3 letter months
#Handles, Full lengthmonths
#Handles 1st, 2nd, 3rd, 4th, extra 2 letters after number

months = 'Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec'
months2 = 'January|February|March|April|June|July|August|September|October|November|December'
months = '(%s|%s) \d{1,2}' % (months , months2)

pattern = r"between (?P<date1>%s.*?)(th|rd|st|nd)? and (?P<date2>%s.*?)(th|rd|st|nd)?" % (months, months)

print ( '----' )
print ( 'PATTERN:' )
print ( pattern )
print ( '----' )
print ( '' )

pattern_obj = re.compile(pattern)

for phrase in phrases:	
	res = pattern_obj.search(phrase)
	if res:
		print 'Sample Text : ' + phrase + "\t"
		print ( res.group('date1') + ' , ' + res.group('date2') )
	else:
		print phrase + "\t" + 'no match'
	print ( '-' )
	print ( '' )

days = ['mon','tue','wed','thu','fri','sat','sun']
print("Days list:",days,id(days))

workdays = days.copy()
print("Workdays list:",workdays,id(workdays))

del workdays[-2:]
print("Workdays list:",workdays,id(workdays))
print("Days list:",days,id(days))




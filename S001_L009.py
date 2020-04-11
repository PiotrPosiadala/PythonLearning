projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for n, (project, date, leader) in enumerate(zip(projects, dates, leaders)):
    print("{}. The leader of {} started {} is {}".format(n+1,project, date, leader))


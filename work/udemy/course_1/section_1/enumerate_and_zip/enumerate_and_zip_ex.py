projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

for project, leader in zip(projects, leaders):
    print(project, leader)


dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for i, (project, leader, date) in enumerate(zip(projects, leaders, dates)):
    print(i, project, leader, date)
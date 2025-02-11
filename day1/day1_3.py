

artists = ['BTS', 'NJZ', '핑클', 'SES', 'HOT', '블랙핑크']
groups = artists #주소만 복사
print(artists, groups)
artists[2] = '세븐틴'
print(artists, groups)

# groups는 artists의 주소를 같이쓰고있기때문에 artists의 2번째 값이 바뀌면 groups도 같이 바뀐다.
import re


def solution(files):
    data = dict()
    for i, f in enumerate(files):
        g = re.search('([^0-9]+)(\d{1,5})', f)
        data[(g.group(1).upper(), int(g.group(2).lstrip('0')) if g.group(2).lstrip('0') else 0, i)] = f
    answer = list(sorted(data.keys(), key=lambda x: (x[0], x[1], x[2])))
    return [data[i] for i in answer]


# file = ['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG']
file = ['F-5 Freedom Fighter', 'B-50 Superfortress', 'A-10 Thunderbolt II', 'F-14 Tomcat']
print(solution(file))
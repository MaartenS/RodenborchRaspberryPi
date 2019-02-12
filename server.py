from bottle import route, run, template

cnt = 0

@route('/count')
def counter():
    global cnt
    cnt += 1
    return template('<h1>Geklikt {{counter}}</h1>', counter=cnt)

@route('/')
def index():
    global cnt
    return template('<h1>Geklikt {{counter}}</h1>', counter=cnt)


run(host='0.0.0.0', port=8080)
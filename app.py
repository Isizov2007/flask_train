from flask import Flask, url_for, request

app = Flask(__name__)


@app.route("/")
def mission_name():
    return "Миссия Колонизация Марса"


@app.route("/index")
def mission_motto():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def promotion():
    return """
    <strong>Человечество вырастает из детства.</strong><br>
    <strong>Человечеству мала одна планета.</strong><br>
    <strong>Мы сделаем обитаемыми безжизненные пока планеты.</strong><br>
    <strong>И начнем с Марса!</strong><br>
    <strong>Присоединяйся!</strong>
    """


@app.route("/image_mars")
def image_mars():
    return f"""
    <title>Привет, Марс!</title>
    <h2>Жди нас, Марс!</h2>
    <img src="{url_for('static', filename='mars_image.png')}" 
           alt="здесь должна была быть картинка, но не нашлась"
           width="300">
    <p>Вот она какая, красная планета.</p>
    """


@app.route("/promotion_image")
def promotion_image():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for(
        'static', filename='css/style.css')}" />
                        <title>Колонизация</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars_image.png')
    }" alt="здесь должна была быть картинка марса"
    width="300">
                        <div class="alert alert-dark" role="alert">
                         Человечество вырастает из детства.
                        </div>
                        <div class="alert alert-success" role="alert">
                         Человечеству мала одна планета.
                        </div>
                        <div class="alert alert-dark" role="alert">
                         Мы сделаем обитаемыми безжизненные пока планеты.
                        </div>
                        <div class="alert alert-warning" role="alert">
                         И начнем с Марса!
                        </div>
                        <div class="alert alert-danger" role="alert">
                         Присоединяйся!
                        </div>
                      </body>
                    </html>"""


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h3>на участие в миссии</h3>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <label for="classSelect"></label>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас оброзавание?</label>
                                        <select class="form-control" id="education" name="education">
                                          <option>нет оброзавания</option>
                                          <option>начальное</option>
                                          <option>среднее</option>
                                          <option>высшее</option>
                                          <option>профисиональное</option>
                                        </select>
                                     </div>
                                    <label for="classSelect"></label>
                                    <label for="classSelect">Какие у вас есть профессии?</label>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules1" name="in_is">
                                        <label class="form-check-label" for="acceptRules1">инженер-исследователь</label>
                                     </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules2" name="pil">
                                        <label class="form-check-label" for="acceptRules2">пилот</label>
                                     </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules3" name="sto">
                                        <label class="form-check-label" for="acceptRules3">строитель</label>
                                     </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules4" name="exb">
                                        <label class="form-check-label" for="acceptRules4">экзобиолог</label>
                                     </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules5" name="in_tr">
                                        <label class="form-check-label" for="acceptRules5">инженер по терраформированию</label>
                                     </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules6" name="vr">
                                        <label class="form-check-label" for="acceptRules6">врач</label>
                                     </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules7" name="klim">
                                        <label class="form-check-label" for="acceptRules7">климатолог</label>
                                     </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules8" name="prog">
                                        <label class="form-check-label" for="acceptRules8">программист</label>
                                     </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules9" name="prf_rad_arm">
                                        <label class="form-check-label" for="acceptRules9">специалист по радиационной защите</label>
                                     </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules10" name="astrg">
                                        <label class="form-check-label" for="acceptRules10">астрогеолог</label>
                                     </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules11" name="shtur">
                                        <label class="form-check-label" for="acceptRules11">штурман</label>
                                    </div>
                                    <label for="classSelect"></label>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="answer" rows="3" name="answer"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы ли остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        return "Форма отправлена"



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
from flask import Flask, url_for

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)


# Если что, то все будет в архиве

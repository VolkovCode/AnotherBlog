<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Главная страница</title>
</head>

<body>
    {% for post in posts %}
    <p>
        {{ post.text }}
    </p>
</body>
{% endfor %}
</body>

</html>
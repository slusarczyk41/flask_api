# Quickstart

## Prerequisites:
- docker-compose: https://docs.docker.com/compose/install/
- redis: https://redis.io/topics/quickstart
- python packages: pip install -r content_api/requirements.txt

## Testing
Ensure that redis server is up, cd to content_api and run python tests.py

## Run service
Ensure that docker daemon is up and run docker-compose up while being in project root directory

## Endpoints
- /add_task/<type>/<url> - add tasks of a given type (text/images) to scrap given url
- /check_status/<id> - checks job status of given id
- /get_page/<url> - send back zip with all resources found about url



## Komentarz
Ze wszystkich użytych tutaj technologii kiedyś korzystałem, było to jednak albo dosyć dawno temu
albo w niewielkim stopniu, dlatego połączenie dockera, flaska oraz scrapowania stron internetowych
okazało się być zadaniem przy którym musiałem się nieco wysilić ale nie sprawiło mi to większych
trudności.

W pewnym momencie miałem problem z drobną rzeczą która przestała działać po wrzuceniu do obrazu
dockera. Siedziałem nad tym dość długo, jako że nie miałem obok siebie zespołu i kogoś kogo mógłbym
spytać o radę - w tym przypadku inna osoba od razu by zobaczyła gdzie leży błąd i zaoszczędziłbym
dwie godziny przeszukiwania internetu co jest nie tak.

Domyślam się też, że można by dopisać jeszcze kilka testów, niestety do tej pory miałem z
tym niewielkie doświadczenie i przez to ta część zadania może się wydawać niekompletna. Gdybym był
zatrudniony w firmie robiąc to zadanie, poprosiłbym bardziej doświadczoną osobę o pokazanie podobnego projektu z którego
testów mógłbym się wzorować, lub w przypadku gdyby takiego nie było to o listę przypadków które
powinienem przetestować, i następnie sam zabrałbym się do pracy aby jednocześnie skorzystać z wiedzy takiej osoby, ale nie zabierać jej zbyt wiele czasu.

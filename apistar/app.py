from apistar import Include, Route
from apistar.frameworks.wsgi import WSGIApp as App
from apistar.handlers import docs_urls, static_urls

from resources.schema import StringRequest

def random_string(request: StringRequest):

	from apistar.exceptions import BadRequest
	import string
	import random

	print(request)

	choices = ""

	if request["alpha"]:
		choices = choices + string.ascii_letters
	if request["digit"]:
		choices = choices + string.digits
	if request["punctuation"]:
		choices = choices + string.punctuation

	if len(choices) == 0:
		raise BadRequest(detail="Impossible options.")
		

	for ex in request["exclude"]:
		if ex in choices:
			choices = choices.replace(ex, "")

	result = ""

	result = result.join(random.SystemRandom().choice(choices) for _ in range(request["length"]))

	if request["upper"]:
		result = result.upper()
	if request["lower"]:
		result = result.lower()

	return(result)

routes = [
    Route('/', 'POST', random_string),
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]

app = App(routes=routes)


if __name__ == '__main__':
    app.main()

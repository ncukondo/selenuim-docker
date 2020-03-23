FIG = docker-compose
SERVICE = app

build:
	@$(FIG) build
run:
	@$(FIG) run selenium python test.py
shell:
	@$(FIG) run selenium /bin/ash
clean:
	@docker image prune
	@docker volume prune

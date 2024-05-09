

up:
	@docker-compose up --detach --wait

up-debug:
	@docker-compose up

down:
	@docker-compose down

logs:
	@docker-compose logs --tail=0 --follow

migrate:
	@docker-compose exec django  python manage.py migrate

migrations:
	@docker-compose exec django  python manage.py makemigrations

bash:
	@docker-compose exec django bash

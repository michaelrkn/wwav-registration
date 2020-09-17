makemigrations core



Dont forget to change admin password

add zips
create superuser

core migrations init.py

To do blue green deployment
Clone env, go to rds go to default vpc security group 
add inbound postgres rule with value of the new env security group (found in configuration>instance>edit)
Swap env cname 
Go to rds, remove old inbound rule
Go to EB, Terminate old env



If deploying from scratch, you might need to add commands for `manage.py addZips` and `manage.py createsu` in db-migrate.config
```
  04_migrate:
    command: "source /var/app/venv/staging-LQM1lest/bin/activate && python manage.py createsu"
    leader_only: true
  05_migrate:
    command: "source /var/app/venv/staging-LQM1lest/bin/activate && python manage.py addZips"
    leader_only: true
```
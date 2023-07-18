from django.core.management import call_command

def create_database():
    call_command("")

def update_database():
    call_command("migrate")
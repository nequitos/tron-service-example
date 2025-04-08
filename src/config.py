
from environs import Env


env = Env()
env.read_env()

POSTGRES_USER = env.str("POSTGRES_USER")
POSTGRES_PASSWORD = env.str("POSTGRES_PASSWORD")
POSTGRES_HOST = env.str("POSTGRES_HOST")
POSTGRES_PORT = env.int("POSTGRES_PORT")
POSTGRES_DATABASE = env.str("POSTGRES_DATABASE")

HOST = env.str("HOST")
PORT = env.int("PORT")

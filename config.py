from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "8806700"))
API_HASH = getenv("API_HASH", "e3be731079b3d459bac857e7eec3ee87")
BOT_TOKEN = getenv("BOT_TOKEN","5109963129:AAEh1nsreej43O1jyr57ZBP13aKaf3z_7A0")
BOT_NAME = getenv("BOT_NAME","ðââððÍŦAĖķTĖķAĖķKĖķððâðĶââĢðĐððŠâĢâðŧâðĶðððâðĪâŋâŊââââðĐððŠððââðŋððžððððââð âãðŪðģãâĪðĪðĐ")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
SESSION_NAME = getenv("SESSION_NAME", "BQB28R0FEXW5q6MHD9oJlNGs_bpIRSYzNLmJOj-FMzFzyCs6mbPiUlJKP0mKXz7ym5Jn5Jru5dDptFfi8sYwSOGzo_JHgZkTosdzlMzquEQqIPuX4I07U5I6Kq9KjsbbrjN8EJNpFbQ7KO3KbAf5BEOi8CE1zcEWcIOQjOHoqEuaCt3XkOAAkgJoCDgVuNQz4thLyK0bzXM1EwNmjsasubdgMViQA2KmDjpT9q65IegBMQZGOEERQI8EXT3C7fZY7X4U3h0ROc_o3pPPcwv1i48d4-rFrKm6jcr0PFECSjgkJZjjAcaUUVzaivoiBWQIKUcG4WShu8ABi-FdcEtkl2xkfXKMAQA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5080000553").split()))

import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    for player in data:
        Player.objects.create(nickname=player)
        


if __name__ == "__main__":
    main()

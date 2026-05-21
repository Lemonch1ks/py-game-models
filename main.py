import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    for player in data:
        Player.objects.create(
            nickname=player,
            email=player["email"],
            bio=player["bio"],
            race=Race.objects.create(
                name=player["race"]["name"],
                description=player["race"]["description"]
            ),
            guild=Guild.objects.create(
                name=player["guild"]["name"],
                description=player["guild"]["description"]
            ),

        )




if __name__ == "__main__":
    main()

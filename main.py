import init_django_orm  # noqa: F401
import json

from db.models import Guild, Player, Race, Skill


def _get_or_create_race_with_skills(player_data: dict) -> Race:
    race_data = player_data["race"]
    race, _ = Race.objects.get_or_create(
        name=race_data["name"],
        defaults={"description": race_data["description"]},
    )

    for skill_data in race_data["skills"]:
        Skill.objects.get_or_create(
            name=skill_data["name"],
            defaults={"bonus": skill_data["bonus"], "race": race},
        )

    return race


def _get_or_create_guild(player_data: dict) -> Guild | None:
    guild_data = player_data["guild"]
    if guild_data is None:
        return None

    guild, _ = Guild.objects.get_or_create(
        name=guild_data["name"],
        defaults={"description": guild_data["description"]},
    )
    return guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        players_data = json.load(file)

    # `players_data` has the following shape:
    # {
    #   "nickname": {
    #       "email": str,
    #       "bio": str,
    #       "race": {...},
    #       "guild": {...} | null,
    #   },
    # }
    # Therefore we iterate by `.items()` to get both nickname and payload.
    for nickname, player_data in players_data.items():
        race = _get_or_create_race_with_skills(player_data)
        guild = _get_or_create_guild(player_data)

        Player.objects.create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()

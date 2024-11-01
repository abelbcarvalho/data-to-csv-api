json_success: list[dict[str, any]] = [
    dict(
        name="paula",
        age=23,
        gender="female",
        occupation="scientist"
    ),
    dict(
        name="maria",
        age=25,
        gender="female",
        occupation="developer"
    ),
    dict(
        name="joseph",
        age=20,
        gender="male",
        occupation="lawyer"
    )
]


json_fail_one: list[dict[str, any]] = [
    *json_success,
    dict(
        name="julia",
        age=25,
        gender="female",
        college="harvard"
    )
]


json_fail_two: list[dict[str, any]] = [
    dict(
        name="hadassa",
        age=23,
        gender="female",
        college="stanford"
    ),
    *json_success,
]


csv_success: str = (
    'name,age,gender,occupation\n'
    'paula,23,female,scientist\n'
    'maria,25,female,developer\n'
    'joseph,20,male,lawyer\n'
)
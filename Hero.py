class SuperHero():
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def __str__(self):
        return f'{self.name} {self.nickname} {self.superpower} {self.health_points} {self.catchphrase}'

    def __len__(self):
        return f'{self.catchphrase}'
def hero_name(name):
    print(f'Hero name is {name} ')


hero_name('Peter Parker')


def hero_points(health_points):
    health = health_points * 2
    print(f'Hero health = {health}')


hero_points(50)

hero = SuperHero('Peter Parker', 'Spider-Man', 'Strong', 100,'With great power comes great responsibility')
print(f' Hero nickname is {hero.nickname}.'
      f' \n He is very {hero.superpower}. '
      f'\n And his health-point is = {hero.health_points}')
print(f' His cathphrase len is = {len(hero.catchphrase)}')
print(f'')
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

hero = SuperHero('Peter Parker', 'Spider-Man', 'Strong', 100,
                 'With great power comes great responsibility')
print(f' Hero nickname is {hero.nickname}.'
      f' \n He is very {hero.superpower}. '
      f'\n And his health-point is = {hero.health_points}')
print(f' His cathphrase len is = {len(hero.catchphrase)}')


class HeroOne(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def hero_points(self):
      health = self.health_points ** 2
      print(f'Hero health = {health}')
      self.fly = True

    def true_phrase(self):
       print(f' fly in the True_phrase ')
aquaman = HeroOne('Artur,', 'Aquaman,', 'breathe underwater,', 50, 'You have to do what you feel is right, even if it hurts you.', 'n')
print(aquaman.fly)
aquaman.true_phrase
hero_points(aquaman.health_points)

class HeroTwo(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly
    def hero_points(self):
      health = self.health_points ** 2
      print(f'Hero health = {health}')
      self.fly = True

    def true_phrase(self):
        print(f' fly in the True_phrase ')

tor = HeroTwo(f'Thor', f'Thor','lightning control', 50,\
               'Feel free to choose expressions. Loki is wrong, but he is still an Asgardian and also my brother', 5)
print(tor)
tor.true_phrase
hero_points(tor.health_points)
class Villain(HeroTwo):
    people = 'monster'
    def gen_x(self):
        pass
    def crit(self):
        self.damage **= 2
        return self.damage

print(HeroTwo.damage)
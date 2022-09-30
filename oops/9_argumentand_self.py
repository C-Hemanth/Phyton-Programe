class students:
    branch = 'c.s.e'

    # we can add argumnts when we are defining with self
    def greet(self, sign, fav):
        print(f"{self.name}\n{sign}\n{fav}")


hemanth = students()
hemanth.name = 'j'
hemanth.greet('h', 'k')
# hemanth.greet()

from random import randint


class TerrainRace:
    def __init__(self, terrain, debug=False):
        self.terrain = terrain
        self._pos = 0
        self.debug = debug

    def _move(self):
        move_length, move_strength = self._random_move_parameters()
        if self.debug:
            self._show_position(move_length, move_strength)
        while (self._pos < len(self.terrain)
               and move_length
               and move_strength >= self.terrain[self._pos]):
            move_length -= 1
            self._pos += 1

    def _random_move_parameters(self):
        return randint(1, 6), randint(1, 6)

    def _show_position(self, d1, d2):
        for i, t in enumerate(self.terrain):
            if self._pos == i:
                print('*', end='')
            else:
                print(' ', end='')
            print(t, end='')
        print(f'   {d1} {d2}')

    def number_of_moves(self):
        self._pos = 0
        counter = 0
        while self._pos < len(self.terrain):
            counter += 1
            self._move()
        return counter

    def ave_number_of_moves(tries=10000):
        total = 0
        for _ in range(tries):
            total += self.number_of_moves()
        return total/tries

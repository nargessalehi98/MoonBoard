import random


class Map:
    def __init__(self):
        self.letters = 'ABCDEFGHIJK'
        self.map = {'1A': 3.4, '1B': 4.4, '1C': 8.1, '1D': 5.0, '1E': 7.8, '1F': 4.1, '1G': 6.9, '1H': 6.3, '1I': 6.6,
                    '1J': 6.6, '1K': 2.5,
                    '2A': 5.6, '2B': 3.8, '2C': 9.4, '2D': 2.8, '2E': 7.8, '2F': 3.8, '2G': 7.2, '2H': 5.3, '2I': 5.9,
                    '2J': 3.1, '2K': 5.6,
                    '3A': 4.1, '3B': 3.8, '3C': 9.4, '3D': 7.5, '3E': 3.1, '3F': 8.1, '3G': 6.9, '3H': 7.2, '3I': 6.6,
                    '3J': 6.6, '3K': 7.8,
                    '4A': 2.2, '4B': 4.4, '4C': 3.4, '4D': 2.5, '4E': 5.0, '4F': 5.6, '4G': 4.4, '4H': 5.0, '4I': 6.3,
                    '4J': 4.4, '4K': 5.6,
                    '5A': 0.6, '5B': 8.1, '5C': 9.4, '5D': 3.8, '5E': 7.5, '5F': 3.1, '5G': 7.2, '5H': 2.5, '5I': 6.9,
                    '5J': 8.1, '5K': 4.4,
                    '6A': 2.5, '6B': 7.5, '6C': 6.6, '6D': 6.6, '6E': 5.0, '6F': 5.0, '6G': 4.1, '6H': 8.1, '6I': 6.3,
                    '6J': 6.9, '6K': 6.9,
                    '7A': 7.2, '7B': 6.9, '7C': 5.0, '7D': 7.5, '7E': 6.3, '7F': 4.7, '7G': 1.9, '7H': 6.9, '7I': 1.3,
                    '7J': 6.3, '7K': 7.5,
                    '8A': 4.1, '8B': 4.4, '8C': 9.4, '8D': 7.2, '8E': 4.4, '8F': 2.5, '8G': 4.1, '8H': 5.0, '8I': 1.3,
                    '8J': 6.9, '8K': 8.1,
                    '9A': 8.1, '9B': 5.9, '9C': 6.9, '9D': 2.8, '9E': 6.9, '9F': 5.0, '9G': 7.5, '9H': 6.3, '9I': 6.9,
                    '9J': 2.5, '9K': 6.3,
                    '10A': 5.9, '10B': 6.3, '10C': 3.4, '10D': 1.9, '10E': 8.8, '10F': 7.2, '10G': 3.8, '10H': 3.1,
                    '10I': 6.3, '10J': 8.8, '10K': 5.6,
                    '11A': 3.1, '11B': 9.4, '11C': 6.6, '11D': 6.6, '11E': 4.4, '11F': 8.8, '11G': 3.1, '11H': 5.6,
                    '11I': 6.9, '11J': 1.9, '11K': 4.4,
                    '12A': 5.3, '12B': 5.9, '12C': 6.6, '12D': 5.9, '12E': 6.6, '12F': 3.4, '12G': 6.6, '12H': 8.4,
                    '12I': 6.3, '12J': 7.5, '12K': 8.8,
                    '13A': 8.1, '13B': 3.4, '13C': 3.8, '13D': 7.8, '13E': 1.3, '13F': 5.6, '13G': 2.5, '13H': 7.8,
                    '13I': 4.4, '13J': 4.1, '13K': 2.2,
                    '14A': 2.8, '14B': 9.1, '14C': 2.2, '14D': 9.4, '14E': 4.4, '14F': 7.2, '14G': 5.6, '14H': 5.9,
                    '14I': 6.9, '14J': 8.8, '14K': 7.5,
                    '15A': 7.2, '15B': 6.6, '15C': 8.8, '15D': 4.1, '15E': 7.8, '15F': 7.5, '15G': 7.8, '15H': 6.9,
                    '15I': 9.4, '15J': 7.2, '15K': 1.3,
                    '16A': 3.4, '16B': 10.0, '16C': 0.3, '16D': 6.6, '16E': 4.7, '16F': 8.8, '16G': 6.3, '16H': 7.5,
                    '16I': 5.3, '16J': 1.3, '16K': 7.5,
                    '17A': 7.8, '17B': 9.4, '17C': 8.1, '17D': 5.3, '17E': 8.1, '17F': 5.0, '17G': 4.7, '17H': 6.3,
                    '17I': 10.0, '17J': 9.4, '17K': 4.7,
                    '18A': 2.5, '18B': 0.6, '18C': 7.2, '18D': 4.4, '18E': 4.7, '18F': 3.8, '18G': 8.1, '18H': 1.9,
                    '18I': 7.2, '18J': 19, '18K': 7.5
                    }

    def get_score(self, hold):
        return self.map[hold]

    def set_start(self, size):
        start = []
        for i in range(0, size):
            num = random.randint(1, 6)
            letter = random.choice(self.letters)
            start.append(f'{num}{letter}')
        return start

    def set_top(self):
        top = []
        letter = random.choice(self.letters)
        top.append(f'18{letter}')
        return top

    def alphabet_to_number(self, hold) -> (int):
        if hold.endswith('A'):
            return 0
        if hold.endswith('B'):
            return 1
        if hold.endswith('C'):
            return 2
        if hold.endswith('D'):
            return 3
        if hold.endswith('E'):
            return 4
        if hold.endswith('F'):
            return 5
        if hold.endswith('G'):
            return 6
        if hold.endswith('H'):
            return 7
        if hold.endswith('I'):
            return 8
        if hold.endswith('J'):
            return 9
        if hold.endswith('K'):
            return 10

    def get_row_of_hold(self, hold):
        if len(hold) == 3:
            return int(hold[0] + hold[1])
        if len(hold) == 2:
            return int(hold[0])

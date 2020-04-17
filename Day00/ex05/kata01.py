def kata():
    languages = {
    'Python': 'Guido van Rossum', 
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }

    for x, y in languages.items():
        print(f"{x} is created by {y}")


if __name__ == '__main__':
    kata()
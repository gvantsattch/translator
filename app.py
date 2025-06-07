class TranslatorLogic:
    def __init__(self):
        self.words = {
            "ინგლისური": {
                "სიყვარული": "love",
                "დედა": "mother",
                "მამა": "father",
                "თვე": "moon",
                "გული": "heart",
                "წიგნი": "book",
                "კომპიუტერი": "computer",
                "ფანჯარა": "window",
                "სახლი": "house",
                "მანქანა": "car",
                "მეგობარი": "friend",
                "ცხვარი": "sheep",
                "თევზი": "fish",
                "ხე": "tree",
                "წყალი": "water",
                "სიხარული": "joy",
                "წვიმა": "rain",
                "თოვლი": "snow",
                "სითხე": "liquid",
                "ხილი": "fruit",
                "ტვინი": "brain",
                "თვალი": "eye",
                "სუნთქვა": "breath",
                "ხელები": "hands",
                "ფეხები": "legs",
            },
            "ფრანგული": {
                "სიყვარული": "amour",
                "დედა": "mère",
                "მამა": "père",
                "თვე": "lune",
                "პური": "pain",
                "წიგნი": "livre",
                "სახლი": "maison",
                "მანქანა": "voiture",
                "მეგობარი": "ami",
                "ცხვარი": "mouton",
                "თევზი": "poisson",
                "ხე": "arbre",
                "სიხარული": "joie",
                "სევდა": "tristesse",
                "წვიმა": "pluie",
                "თოვლი": "neige",
                "სითხე": "liquide",
                "ხილი": "fruit",
                "ტვინი": "cerveau",
                "სუნთქვა": "souffle",
                "ხელები": "mains",
                "ფეხები": "jambes",
            }
        }

    def translate(self, word, language):
        return self.words.get(language, {}).get(word.lower(), "თარგმანი ვერ მოიძებნა")






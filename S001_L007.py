def GenerateColours(colours, n):
    new_colours = colours.copy()
    new_colours = new_colours[:n]
    return new_colours

colours = ["red", "orange", "green", "violet", "blue", "yellow"]

for i in range(len(colours)+1):
    print(GenerateColours(colours,i))

print("-"*30)

text = "Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli. " 
print(text[text.index('(')+1:text.index(')')])
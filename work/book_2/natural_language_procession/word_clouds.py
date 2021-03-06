import matplotlib.pyplot as plt

#utworzenie chmury wyrazowej polega na ułożeniu słów w dostępnej przestrzeni w interesujący sposób

#słowo, liczba użyć w ofercie pracy, liczba użyć w życiorysach zawodowych
data = [("big data", 100, 15), ("Hadoop", 95, 25), ("Python", 75, 50),
        ("R", 50, 40), ("machine learning", 80, 20), ("statistics", 20, 60),
        ("data science", 60, 70), ("analytics", 90, 3),
        ("team player", 85, 85), ("dynamic", 2, 90), ("synergies", 70, 0),
        ("actionable insights", 40, 30), ("think out of the box", 45, 10),
        ("self-starter", 30, 50), ("customer focus", 65, 15),
        ("thought leadership", 35, 35)]


def text_size(total):
        return 8 + total / 200 * 20


for word, job_popularity, resume_popularity in data:
        plt.text(job_popularity, resume_popularity, word,
                 ha='center', va='center',
                 size=text_size(job_popularity + resume_popularity))
plt.xlabel("Popularnosc w ofertach pracy")
plt.ylabel("Popularnosc w CV")
plt.axis([0, 100, 0, 100])
plt.xticks([])
plt.yticks([])
plt.show()
import os
from collections import Counter
import thugRating


def analyze(lyrics):
	lyrics = lyrics.replace("'", "")
	lyrics = lyrics.replace(",", "")
	lyrics = lyrics.replace("?", "")
	lyrics = lyrics.replace("!", "")
	lyrics = lyrics.replace(".", "")
	lyrics = lyrics.replace("\"", "")
	lyrics = lyrics.replace("\r", "")

	all_lines = []
	all_words = []

	vLines = lyrics.split("\n")

	for line in vLines:
		all_lines.append(line)

	if all_lines[-1][0:10] == "read more:":
		all_lines[-4:] = []

	if "chorus" in all_lines[-1]:
			all_lines.pop(-1)

	for l in all_lines:
		if l[0:7] == "[chorus" or l[0:5] == "[hook":
			chorusIndex = all_lines.index(l)
			i = chorusIndex
			endIndex = 0
			while i < len(all_lines):
				if all_lines[i + 1] == "":
					endIndex = i
					break
				i += 1
			all_lines[(chorusIndex - 1):(endIndex+2)] = []
		
	for l in all_lines:

		if "[" in l:
			all_lines.pop(all_lines.index(l))


	for l in all_lines:
		wordsInLine = l.split(" ")
		for w in wordsInLine:
			all_words.append(w)

	for l in all_lines:
		if l == "":
			all_lines.pop(all_lines.index(l))

	

	ind = 0

	while ind < len(all_words):
		if "(" in all_words[ind] or ")" in all_words[ind]:
			all_words.pop(ind)
		ind += 1

	unique_words = set(all_words)

	uniqueWordsCount = len(unique_words)
	percentageUnique = (float(uniqueWordsCount) / len(all_words)) * 100

	last_words = []

	for l in all_lines:
		line_words = l.split(" ")
		last_words.append(line_words[-1])

	repeated_rhymes = last_word_repeat(last_words)

	eligibleW = []
	for w in all_words:
		if w not in commonWords:
			eligibleW.append(w)



	words_to_count = (word for word in eligibleW)
	c = Counter(words_to_count)
	most_common_3 = c.most_common(5)
	return {
		'total_words' : len(all_words),
		"unique_words" : uniqueWordsCount,
		"percentage" : percentageUnique,
		"repeated_rhymes" : repeated_rhymes,
		"bad_words" : countbadwords(all_words),
		"most_common" : most_common_3,
		"thug_rating" : thugRating.thug_rating(eligibleW),
		"avg_syllables" : thugRating.avg_syllables(eligibleW)
	}
# bad words

def last_word_repeat(words):
	repeats = 0

	if len(words) < 2:
		return repeats

	i = 1
	while i < len(words):
		if words[i-1] == words[i]:
			repeats += 1
		i += 1

	return repeats

def countbadwords(lyric):
    j = 0
    for i in lyric:
        if badword(i):
            j +=1
    
    return j

curses = ['bastard', 'asshole', 'tit', 'nigga', 'nigger', 'fuck', 'cunt', 'shit', 'damn', 'bitch', 'dick', 'piss', 'pussy', 'fag', 'cock', 'slut']

def badword(word):
        if word == 'ass':
            return True
        for i in curses:
            if i in word:
                return True
        return False


# common words

commonWords = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me', 'when', 'make', 'can', 'like', 'time', 'no', 'just', 'him', 'know', 'take', 'people', 'into', 'year', 'your', 'good', 'some', 'could', 'them', 'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its', 'over', 'think', 'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work', 'first', 'well', 'way', 'even', 'new', 'want', 'because', 'any', 'these', 'give', 'day', 'most', 'us', 'um', 'i', 'im', 'ive', 'is', 'uh', '']


# analyze("logic_metropolis")
# analyze("eminem_therealslimshady")
# analyze("eminem_loseyourself")
# analyze("lildicky_professionalrapper")
# analyze("lildicky_lemmefreak")
# analyze("kanyewest_stronger")
# analyze("nwa_straightouttacompton")
# analyze("rickross_bmf")
# analyze("e40_choices")
# analyze("asap_1train")
# analyze("eminem_rapgod")
# analyze("eminem_lovegame")
# analyze("lilwayne_fireman")
# analyze("kendricklamar_kingkunta")
# analyze("rickross_astonmartinmusic")
# analyze("lilwayne_watchmyshoes")
# analyze("drake_9amindallas")
# analyze("drake_0to100thecatchup")
# analyze("drake_10bands")
# analyze("nickiminaj_anaconda")
# analyze("getoboys_damnitfeelsgoodtobeagangsta")




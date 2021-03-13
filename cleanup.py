from bs4 import BeautifulSoup

def cu1():
	final = []

	with open("messages.html", "r") as f:
		lines = f.read().split("<br>\n")
	c = 0
	for line in lines:
		c +=1 
		print(c)
		try:
			nameHTML = line.split("] ")[1].split(">: ")[0] + ">"
			timeStamp = line.split(" ")[0]
			message = line.split(">: ")[-1]


			soup = BeautifulSoup(nameHTML, features="lxml")
			name = soup.get_text()

			if len(name) == 0 or name == "":
				name = nameHTML.split(' title="')[1].split('"')[0]
			

			final.append(timeStamp + " - " + name + ": " + message)

		except:
			print("error")
			final.append("[PARSING ERROR] parsing_error: error")

	with open("formatted.txt", "w") as f:
		f.write("\n".join(final))
	# [2021-03-12T23:44:36.302Z] <i class="rf_i rf_god"></i><img class="rf_img" src="//cdn.raidforums.com/i/RF_ZI5U.gif" title="pacino"/>: the only based countries are lithuania, poland, latvia, slovakia, literally every other country in that area, east germany<br>


# def cu3():
# 	final = []
# 	with open("formatted.txt", "r") as f:
# 		text = f.read().split("\n")

# 	for x in text:
# 		final.append(
# 			" ".join(x.split(" ")[:3]) + ": " + " ".join(x.split(" ")[3:])
# 			)

# 	with open("formatted.txt", "w") as f:
# 		f.write("\n".join(final))


cu1()
# cu3()

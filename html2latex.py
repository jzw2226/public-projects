#request html string as user input
string = input("Please enter a HTML string: ")

#replace HTML characters wtih LaTeX counterparts
new_string = string.replace("&ldquo;", "``")
new_string = new_string.replace("&rdquo;", '"')
new_string = new_string.replace("&apos;", "'")
new_string = new_string.replace("&amp;", "&")
new_string = new_string.replace("&lt;", "<")
new_string = new_string.replace("&gt;", ">")
new_string = new_string.replace("{", "\{")
new_string = new_string.replace("}", "\}")
new_string = new_string.replace("%", "\%")

#print results
print(new_string)
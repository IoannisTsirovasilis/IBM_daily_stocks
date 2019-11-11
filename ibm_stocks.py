

with open("files/IBM.csv", "r") as f:
    content = f.readlines()

new_content = []
with open("files/results.csv", "w") as f:
    print("writing lines...")
    new_content = [c.replace("\n", "") + "," + str(100 * (float(c.split(",")[1]) - float(c.split(",")[4])) /
                   float(c.split(",")[1])) + "\n" for c in content if c != content[0]]
    f.write("Date,Open,High,Low,Close,Adj Close,Volume,Daily Stock\n")
    f.writelines(new_content)


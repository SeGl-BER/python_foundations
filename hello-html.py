#name = input ("What's your name?  ")
#print("Hello,", name)

html = """<!DOCTYPE html>
<html>
<meta charset="utf-8">
<head>
<title>Hello human</title>
<style>
  body {
    color: orange;
    style: bold;
  }
  form {
    color: blue;
    size: 12 px;
  }
</style>
</head>
<body>
<h1>Hello</h1>
  <form>
  <label for="name"> Full Name </label>
  <input type="text" name ="name" required placeholder="Enter your name">
  <br>
  <input type="submit">
  </form>
</body>
</html>


"""

f = open("index.html", "w")
f.write(html)
f.close()
## Answer Sheet: Lab09

**Question 1:** What is the purpose of the `@app.route('/health')` decorator in the code?

**Answer:** The purpose is to check whether the server is working well(keep running), which refers as 'Health' or not.(A branch of the route)




----------------
**Question 2:** In Jinja2, what is the difference between `{{ my_variable }}` and `{% for item in my_list %}`?

**Answer:**{% ... %} for Statements， {{ ... }} for Expressions to print to the template output(Variable names)




----------------
**Question 3:** In `app.py`, why is it important to use `(?, ?)` and pass the variables as a tuple in the `conn.execute()` command instead of using f-strings to put the variables directly into the SQL string? What is this technique called?

**Answer:** Because f-string may easily lead to error or be attacked by others. f-string directly put the value into SQL string, thus sometime recognize it as a SQL command. And this method is called Parameterized Queries and only treated it as data.




----------------
**Question 4:** What is the purpose of `event.preventDefault()` in the JavaScript code? What would happen if you removed that line?

**Answer:** it stops the default action for a certain action, for the lab, it prevent reload the page annd leave the text in the colunm if the error occurs.




----------------
**Question 5:** In the `Dockerfile`, why is the `CMD` `["flask", "run", "--host=0.0.0.0"]` necessary? Why wouldn't the default `flask run` (which uses host 127.0.0.1) work?

**Answer:** If Flask listens only to 127.0.0.1, it is only accessible by myself. connect to 0.0.0.0 makes other can also join it.



----------------
**Question 6:** In the `docker-compose.yml` setup, Nginx is configured to `proxy_pass http://flask-app:5000`. How does the Nginx container know the IP address of the `flask-app` container?

**Answer:** Because docker Compose automatically creates a shared network and provides built-in DNS 
resolution.




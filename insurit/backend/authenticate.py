# backend
def login(cursor, username: str, password: str, login_level: int) -> int:
	SQL = "SELECT AUTH(%s, %s, %s);"
	params = (username, password, login_level)
	cursor.execute(SQL, params)
	response = cursor.fetchone()
	cursor.close()
	return response[0]


# backend
def login(cursor, username: str, password: str, login_level: int) -> int:
	SQL = "SELECT AUTH(%s, %s, %s);"
	params = (username, password, login_level)
	cursor.execute(SQL, params)
	response = cursor.fetchone()
	cursor.close()
	return response[0]


def id_from_username(conn, access, uid):
	SQL = "SELECT ID FROM INSURIT.SECRETS WHERE USERNAME = %s AND LVL = %s"
	cursor = conn.cursor()
	cursor.execute(SQL, (uid, str(access)))
	response = cursor.fetchone()
	cursor.close()
	return response[0]
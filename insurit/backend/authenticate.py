# backend
def login(cursor, username: str, password: str, login_level: int) -> int:
	"""
	Authenticate user login
	:param cursor: Database connection strings cursor instance
	:param username: Username as entered by user
	:param password: Password as entered by user
	:param login_level: The login level. This is identified by frontend parser
	:return: Bool: 0 for failure and 1 for success
	"""
	SQL = "SELECT AUTH(%s, %s, %s);"
	params = (username, password, login_level)
	cursor.execute(SQL, params)
	response = cursor.fetchone()
	cursor.close()
	return response[0]


def id_from_username(conn, access, uid):
	"""
	Fetch User ID from their username
	:param conn: Connection string
	:param access: Access level
	:param uid: Username of user
	:return:
	"""
	SQL = "SELECT ID FROM INSURIT.SECRETS WHERE USERNAME = %s AND LVL = %s"
	cursor = conn.cursor()
	cursor.execute(SQL, (uid, str(access)))
	response = cursor.fetchone()
	cursor.close()
	return response[0]
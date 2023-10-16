if __name__ == "__main__":
	try:
		__import__("new_enc").login()
	except Exception as e:
		exit(str(e))

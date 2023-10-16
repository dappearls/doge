if __name__ == "__main__":
	try:
		__import__("doge_enc").login()
	except Exception as e:
		exit(str(e))

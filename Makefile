format_notebooks:
	poetry run nbqa isort notebooks/*
	poetry run nbqa black notebooks/*
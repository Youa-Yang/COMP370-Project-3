# COMP 370 Group Project 3

## How to use

1. Install Python 3 and pip (https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
2. Inside the project folder, create a virtual environment by running
   - Unix/macOS: `python3 -m venv env`
   - Windows: `py -m venv env`
3. Active the virtual environment
   - Unix/macOS: `source env/bin/activate`
   - Windows: `.\env\Scripts\activate`
4. Install PyGithub: `pip install PyGithub`
5. Create the file `config.py`. In it, add the line
   ```python
   access_token = "YOUR ACCESS TOKEN"
   ```
   - Generate a GitHub access token and replace the `YOUR ACCESS TOKEN` part above with it
   - https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#creating-a-token
6. Run `python3 <file.py>`

# Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one?
'''
1) Create the First Virtual Environment
-> python3 -m venv env1
-> source env1/bin/activate

2) Install Some Packages in env1
-> pip install requests flask

3) Export the Installed Packages
-> pip freeze > requirements.txt

4) Create the Second Virtual Environment
-> deactivate  # if env1 is still active
-> python3 -m venv env2
-> source env2/bin/activate

5) Install the Same Packages in env2
-> pip install -r requirements.txt

'''
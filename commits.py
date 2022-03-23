import config

from github import Github
import csv

g = Github(login_or_token=config.access_token, per_page=100)

with open('commits.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "URL",])
    for commit in g.get_repo("ninja-build/ninja").get_commits():
        writer.writerow([commit.commit.committer.date, commit.commit.tree.url])

import config

from github import Github
import csv
from os import environ

g = Github(login_or_token=environ.get("ACCESS_TOKEN", config.access_token), per_page=100)


def getCodeSize(sha):
    size = 0
    tree = g.get_repo(
        "ninja-build/ninja").get_git_tree(sha).tree
    for element in tree:
        if (element.type == "blob"):
            size += element.size
        else:
            size += getCodeSize(element.sha)
    return size


total_commits = g.get_repo("ninja-build/ninja").get_commits().totalCount
current_commits = sum(1 for row in open('code_sizes.csv'))

with open('code_sizes.csv', 'a+', newline='') as file:
    writer = csv.writer(file)
    progress = 0
    for commit in g.get_repo("ninja-build/ninja").get_commits()[current_commits:current_commits+100]:
        progress += 1
        print(str(progress), "/ 100", [commit.commit.committer.date, commit.commit.tree.sha, getCodeSize(commit.commit.tree.sha)])
        writer.writerow(
            [commit.commit.committer.date, commit.commit.tree.sha, getCodeSize(commit.commit.tree.sha)])

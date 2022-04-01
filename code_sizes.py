import config

from github import Github
import csv

g = Github(login_or_token=config.access_token, per_page=100)


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

with open('code_sizes.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["Sha", "Code Size"])
    progress = 0
    for commit in g.get_repo("ninja-build/ninja").get_commits():
        progress += 1
        print(str(progress), "/", str(total_commits), " ",
              [commit.commit.sha, getCodeSize(commit.commit.sha)])
        writer.writerow([commit.commit.sha, getCodeSize(commit.commit.sha)])

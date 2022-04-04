import config

from github import Github
import csv

g = Github(login_or_token=config.access_token, per_page=100)

with open('issues.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["#", "Title", "URL", "State", "Labels", "# of Labels",
                    "Assignees", "# of Assignees", "# of Comments", "Closed at", "Created at", "Locked"])
    for issue in g.get_repo("ninja-build/ninja").get_issues(state="all"):
        if (issue.pull_request == None):
            writer.writerow([issue.number, issue.title, issue.html_url, issue.state, issue.labels, len(issue.labels),
                            issue.assignees, len(issue.assignees), issue.comments, issue.closed_at, issue.created_at, issue.locked])

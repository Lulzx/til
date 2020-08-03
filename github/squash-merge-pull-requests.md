
## What is a squash merge?

Squash merging is a merge option that allows you to condense the Git history of topic branches when you complete a pull request. Instead of each commit on the topic branch
being added to the history of the default branch, a squash merge takes all the file changes and adds them to a single new commit on the default branch. 

![Squash Merging in pull requests in Azure Repos](https://docs.microsoft.com/en-us/azure/devops/repos/git/media/squash_merge.png)

A simple way to think about this is that squash merge gives you just the file changes, and a regular merge gives you the file changes and the commit history. 


## How is a squash merge helpful?

Squash merging keeps your default branch histories clean and easy to follow without demanding any workflow changes on your team. Contributors to the topic branch work how they want in 
the topic branch, and the default branches keep a linear history through the use of squash merges. The commit history of a `master` branch updated with squash merges will have one commit 
for each merged branch. You can step through this history commit by commit to find out exactly when work was done.

## Considerations when squash merging

Squash merging condenses the history of changes in your default branch, so it is important to work with your team to decide when you should squash merge and when you want to 
keep the full commit history of a topic branch. When squash merging, it's a good practice to delete the source branch. This prevents confusion as the topic branch itself does not have a commit merging it into the default branch.

### References

- [Microsoft Azure DevOps Docs](https://docs.microsoft.com/en-us/azure/devops/repos/git/merging-with-squash?view=azure-devops#what-is-a-squash-merge)

# Git

A meta account of the workings of Git.
Documentation: https://www.git-scm.com/docs/

## Commits
- Use **Atomic commits**: When possible, each commit should encompass a single feature, change, or fix.
- **Tense:** Use present-tense imperative style. Example: *Make x do y*, rather than *Makes/Made x do y*.

## Git Ignore
The .gitignore file can be used to specify files that should not be tracked by Git. Templates for .gitignore files can be found online.

- .DS_Store will ignore files named .DS_Store.
- folderName/ will ignore an entire directory.
- *.png will ignore all png files.

## Branching
Branches can be used to work on the same project in parallel. Each branch can be seen as a timeline of the project.

- The master/main branch is the initial branch.
- **HEAD:** A pointer that refers to the current location that is being checked out. HEAD -> main means that we are looking at the main branch.
- **git branch:** gives a list of the current branches of the repository.
- **git branch \<branch-name\>:** Creates a new branch with the given name.
- **git switch:** Used to switch to a different branch. Replaces *git checkout* for that purpose.
- **git switch -c \<branch-name\>:** To create a new branch and switch to it
- **git branch -d \<branch-name\>:** Deletes a branch. HEAD cannot point to the branch that you are deleting.
- **git branch -m \<new-name\>:** Changes the branch name. HEAD should point to the branch that you are renaming.

## Merging
The act of combining branches. Often, one merges correctly implemented features into the main branch. Merging always happens to the current HEAD branch.

- git merge \<branch-name\>: merges the current branch to the specified branch.
- **Fast-forward merge:** A merge where one branch simply catches up with additional commits from another branch.
- Combining branches with different changes is doing using a new commit for the merge.
- **Merge conflicts:** Occur when there are conflicting changes between the two branches.
- You can solve merge conflicts by inspecting and altering the code where the conflicts occur.

## Other commands
- **log:** Show all previous commits.
- **add:** Add a file to be committed.
- **commit:** Commit the added files.
- **commit -a:** Automatically add all files, then commit.
- **commit --amend:** Used to change the last commit.

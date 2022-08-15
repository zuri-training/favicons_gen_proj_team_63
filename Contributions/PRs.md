# Making PRs

Making PRs are supposed to be easy, nevertheless

## How to begin

As you all know we are having two main branches in total: `dev` and `main`, where `dev` is where you clone and make PRs against, and `main` is the production branch which is continually deployed to the live url. 
We may subsequenly have other branches we'll work with in situations where task comes in workflow mode

- Firstly before you start any task, from your terminal you do the following
  - `git fetch upstream dev` 
  - `git pull upstream dev`
- In case you have made changes[commits included]
  - `git rebase` _[this will update your working branch with the current upstream]_
- Complete your task with appropriate commit messages as indicated in the _Commits_ sub-section above.
- Push and make a PR against the `dev` branch. The title of your PR should be in the format: ` | Title_of_issue_resolved |` ensure it is short and concise.
- When PR is merged, delete that branch if it is not either `main` or `dev`
- For each task, ensure to pull from the `dev` branch first._[regardless of the current branch your're in]_
- Don't forget to add the tag to your PR for instance `[UI]` or `[API]` or `[Bug]`... to your title.

**Note:** You are responsible for keeping your branches up to date with the master branch. I won't solve merge conflicts for you. Ensure zero conflicts.

# Commits

You'll want to chill a bit and do a bit of understanding guidelines on how you'll make commit messages. I've found commit messages to be very helpful as regards large projects or projects with more than one contributor just like what we have.

### Why this?

- Firstly this is to have some sort of consistent commit message to ensure ease of flow across repositories and projects. Also, it helps in your personal project, you having a standard to follow.
- Secondly it helps us[the team] to know where to find certian changes and how to generally control the if it stays or not.

### How to begin

The point of the commit message has to do with a prefix. Commit messages should be in the format:
`[Commit type]: [Commit Message]`

**Where:**

- **Commit type:** refers to one of a predefined subset of what a commit could mean. The subsets are:
  - **Feature:** Involves adding a new feature to the product or an implementation of a specified feature.
  - **Chore:** For changes that do not add new functionality but simply denotes a task performed. Does not have to do with bug fixes. Changes includes: initializing a new project, addition of files, partial changes that do not cause bugs, updates, etc.
  - **Bug:** For changes fixing a bug, typo or anything that leads to correctness of the system being worked on
  - **Buggy:** Should be avoided as much as possible but could be needed. It is used when changes have been partially implemented and execution of the current state of the project would lead to evil bugs and sinister errors. An example refers to unclosed tags and a hurried commit since you might not get access to your PC for a while.
   Projects with this commit type as the latest one should perhaps not be pulled or cloned except such implementation is to be continued by you.
- **Commit Message:** refers to a message describing the changes made. 
  - It is important that each commit should only reflect one feature or implementation change. 
  - **NB** You should not cram two functionalities into one commit except they depend closely on one another. For example, implmentation of auth and adding views for a user profile are closely related but do not inter-depend on one another and should be separated into different commits. 
  - This is just to ensure a dev could work with states that are narrowed down to specific implementations and features.

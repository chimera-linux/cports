# Git basics with cports

There is a chance you are unfamiliar with how Git works and it's giving you
some trouble. This is not a replacement for a proper Git guide per se but
aims to provide some tips for basic foolproof usage.

In general, do not use GitHub's UI for anything but creating a pull request.
Everything else should be done on your computer using local Git tools.

## Cloning cports

After you have forked the repository on GitHub, you will need to clone your
personal fork to have a local copy. To be able to push changes into it, you
will need to use the SSH URL (which means you need your public SSH key set up
on GitHub).

Typically this will involve the following:

```
$ git clone git@github.com:yourusername/cports.git
```

Git has a concept of "remotes". A remote is basically a pair of URLs (one
for fetching, one for pushing) that represents the repository on a remote
server. After you have cloned the repository, the URL you have cloned it
with is the `origin` remote for both pulling and pushing.

It is okay to use the non-SSH URL for pulling, and sometimes might be good,
e.g. to avoid having to type in your SSH key passphrase every time you pull.
You can alter that like this:

```
$ git remote set-url origin https://github.com/yourusername/cports.git
$ git remote set-url --push origin git@github.com:yourusername/cports.git
```

The `set-url` command will alter both URLs, so you need to manually reset
just the push URL afterwards.

In any case, you will also want a remote for Chimera's `cports` repository,
which you will use to sync changes back into your fork. As you most likely
do not have push access there anyway, let's use the HTTPS URL:

```
$ git remote add upstream https://github.com/chimera-linux/cports.git
```

Configure your email and name for the repository as well:

```
$ git config user.email "me@email.provider"
$ git config user.name "Firstname Lastname"
```

It is acceptable to use an anonymous handle instead of a full name for
the latter. By passing `--global`, you can set these for all repositories
anywhere.

Now you should be ready.

## Commits and branching

You can just do whatever you like in your clone now. However, if you wish
to submit it as a pull request, there are some rules to follow.

Git uses "commits" to store changes. A commit is pretty much a difference
in repository contents over some previous commit, with some additional metadata
such as the commit message and author name and email, identified by a specific
hash. A Git history is a chain of commits, all the way to the first one.

Git also supports branches. A branch represents a particular history. The
`master` branch is the primary one in `cports`. You can have custom branches
which diverge from the `master` branch in their own ways.

Git histories are immutable, so changing it results in a new history starting
at the point of change. The old history can still be identified by a commit
hash. In the altered history, every commit from the point of the alteration
will have a new hash, as it links to an altered commit and therefore is a
new commit.

In order to be able to send your changes as a pull request, you will need
a branch for that pull request, and the difference over `master` is what the
pull request will contain.

### Using checkout and switch

To create a new branch in the current tree and switch to it, you can use
either the older `checkout` command or the newer (and as of version 2.44,
experimental) `switch` command. These two are equivalent:

```
$ git checkout -b my-custom-branch-name
$ git switch -c my-custom-branch-name
```

The `-b` and `-c` arguments respectively tell Git to create a new branch
if none yet exists; otherwise the command will only switch branches.

Use the `branch` command without arguments or with the `--list` argument to
list your local branches. It can also be used to create and delete branches.

### Using worktree

If you are managing multiple pull request branches, constantly having to
switch between them may be inconvenient. For this, Git has a concept of
worktrees. By default you have one worktree, which is the primary location
of your cloned repository.

You can create a worktree like so:

```
$ git worktree add additional_tree
```

This will create a directory `additional_tree` containing the `cports`
structure, but separately. You can create a worktree out of an unchecked
branch by passing that branch name afterthe directory name. By default,
if you do not pass anything, a new branch will be created, with the same
name as the directory. If you want this new branch name to be different,
you can pass `-b branch-name` separately.

The `git worktree list` command will display a list of your worktrees. The
`git worktree remove <path>` command will remove an existing worktree. You
can only have one worktree for any particular branch.

## Creating changes

With these things out of the way, you can make whatever changes you like in
the `cports` tree. You will then want to make them into commits, ensuring
that those commits follow Chimera's rules.

To create a commit, you will need to first tell Git which changes should be
included in the commit. The `git add` command is for that. You can run it like
so:

```
$ git add some/path/to/add
```

Sometimes, files may have to be removed instead. The `git rm` command is for
that. You run it equivalently:

```
$ git rm some/path/to/remove
```

See `git add --help` and `git rm --help` for various specifics. There is also
`git mv` to move files around.

Afterwards, you can create your commit. Type `git commit`. A text editor will
come up, where you need to specify your commit message. A commit message
consists of a first line, which is subject to Chimera's rules when it comes
to its formatting. The first line should be 50 characters or less, and should
be followed by an empty line. The other lines should be 72 characters or less,
and you should put a more detailed description of what your commit does there,
if necessary.

If you want to not create a new commit but rather change the previous commit,
you can use `git commit --amend`. This is important as your work on your
changes.

If you run `git commit` without having added or removed anything, it will
print the current state of the tree, including what files have been changed,
added or removed. This can be displayed at any time with `git status`.

## Synchronizing your changes

Once in a while you will want to make sync changes from the upstream repository
into your fork/branch. You should already have the `upstream` remote added,
which makes this easier.

First, fetch the changes from the `upstream` remote:

```
$ git fetch upstream
```

Now, while in the branch you are synchronizing, use the `rebase` command:

```
$ git rebase upstream/master
```

The `rebase` command is very useful not only for this; it basically takes
a given Git object (a branch, commit, or anything else) and re-rolls the
changes of the current branch on top of it. Therefore, if your branch was
previously based on an old version of `upstream/master`, it will take the
current version and re-apply your commits on it. You can likewise use this
to rebase on local branches or other remote branches of your fork; for local
branches you will reference them simply by name, for your fork's remote
branches, this will typically be `origin/branchname` (as your fork's remote
is called `origin`).

It is possible the rebasing will create some file conflicts. If that happens,
you will get an error and your current Git state will allow for editing of the
commit that failed to apply. Locate the files that are conflicting, alter them
to what they should be, then do the following:

```
$ git add conflicting/file
$ git commit
$ git rebase --continue
```

Repeat as many times as it takes until your history is clean. If things get
too messed up to continue, you can run `git rebase --abort` to reset to the
pre-rebase state.

## Interactive rebase

The `rebase` command has a special version called "interactive rebase".
This is mainly useful for reordering, squashing, rewording commits and
so on. This mode is enabled with the `-i` argument.

Let's say you want to take the last 20 commits for interactive rebase.
Run the following:

```
$ git rebase -i HEAD~20
```

A text editor will open. You will see the list of your 20 commits in there,
in the form like:

```
pick <some commit hash> <some commit message>
pick <another commit hash> <another commit message>
...
```

The idea is to edit this in a way you like. You can for example reorder
the lines to reorder the commits. If you wish to edit the commit message
of the commit, change `pick` to `reword`. If you wish to perform changes
in the tree at the point of a specific commit, change it to `edit`. If
you want to squash two or more commits together, set the commit you want
to squash to `squash` and it will merge with the one above.

After you save and quit the text editor, the rebase will occur. If you
have any `edit` commits, Git will stop there, with the edited commit as
the current tip, and you can do changes there (including creating new
commits and amending that commit) and run `git rebase --continue` once
done.

If errors occur at any point, resolve conflicts like when syncing, or
abort the rebase.

## Pushing changes

If you want to push the changes to the remote, use the `push` command:

```
$ git push origin my-branch
```

If no PR exists yet, the output of that command will include a link to
create a pull request.

If you have rebased and therefore the history has been altered, you might
have to force the push. By default, Git does not allow altering history,
and this is what `--force` is for:

```
$ git push --force origin my-branch
```

Every time you push to your branch, the pull request associated with it
(if any) will update.

## Other tips and what not to do

If you are not experienced with Git, you should pretend the `merge` command
does not exist. Chimera keeps a flat history, so all the workflows use
rebasing instead. Some other projects use merge workflows instead, where
the current branch's history itself is branching; whenever you `merge` another
branch into a branch, it will create a special merge commit, representing
the sum of the commits that were merged. Chimera does not do this because
it makes the history more confusing.

This is also why GitHub's web tools should not be used. For example, the
PR sync button will create merge commits.

If you wish to drop top N commits from the current branch, the easiest way
is to run `git reset --hard HEAD~N`. If you wish to reset the current branch
to a specific commit or another object (e.g. another branch), you can also
use it, e.g. `git reset --hard another-branch`.

Use `git log` to inspect the current history. The `git log --graph` command
will also show how the history branches. In Chimera's case, it will be pretty
much flat all the time.

Use `git grep` to quickly search within a repository. Use `git show` to view
the current commit's diff, and `git show some-object` to show the diff of
a commit, branch or soemthing else.

The `git stash` command can be used to stash away uncommitted changes so that
you can work with the tree and restore them later.

The `git diff` command can be used to diff arbitrary things. It's out of scope
of this little guide.

To quickly pull changes from the remote counterpart of your current branch
to the current branch, `git pull --rebase` works and is more or less equal
to `git fetch origin/curbranch; git rebase origin/curbranch`. It also has
a merging mode (potentially default depending on configuration), which you
should not use as it breaks flat history.

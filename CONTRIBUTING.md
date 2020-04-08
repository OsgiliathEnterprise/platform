# Contributing to Osgiliath Platform

Are you ready to contribute to Osgiliath Platform? We'd love to have you on board, and we will help you as much as we can. Here are the guidelines we'd like you to follow so that we can be of more help:

-   [Questions and help](#question)
-   [Issues and Bugs](#issue)
-   [Feature Requests](#feature)
-   [RFCs](#rfcs)
-   [Submission Guidelines](#submit)
-   [Generator development setup](#setup)
-   [Coding Rules](#rules)
-   [Git Commit Guidelines](#commit)

## <a name="question"></a> Questions and help

This is the Osgiliath platform bug tracker, and it is used for [Issues and Bugs](#issue) and for [Feature Requests](#feature). It is **not** a help desk or a support forum.

If you have a question on using Osgiliath platform, or if you need help with your Osgiliath platform project, please [read our help page](https://osgiliathenterprise.github.io/platform/reference/toc.html) and use the [Osgiliath Platform tag on StackOverflow](http://stackoverflow.com/tags/osgiliathplatform) or join our [Gitter.im chat room](https://gitter.im/OsgiliathEnterprise/platform).

## <a name="issue"></a> Issues and Bugs

If you find a bug in the source code or a mistake in the documentation, you can help us by [submitting a ticket](https://opensource.guide/how-to-contribute/#opening-an-issue) to our [GitHub issues](https://github.com/OsgiliathEnterprise/platform/issues). Even better, you can submit a Pull Request to our [Osgiliath Platform project](https://github.com/OsgiliathEnterprise/platform) or to our [Documentation project](https://github.com/OsgiliathEnterprise/platform/tree/master/src/site).

**Please see the Submission Guidelines below**.

## <a name="feature"></a> Feature Requests

You can request a new feature by submitting a ticket to our [GitHub issues](https://github.com/OsgiliathEnterprise/platform/issues). If you
would like to implement a new feature then consider what kind of change it is:

-   **Major Changes** that you wish to contribute to the project should be discussed first. Please open a ticket which clearly states that it is a feature request in the title and explain clearly what you want to achieve in the description, and the Osgiliath team will discuss with you what should be done in that ticket. You can then start working on a Pull Request. In order to communicate major changes proposals and receive reviews from the core team, you can also submit an RFC.
-   **Small Changes** can be proposed without any discussion. Open up a ticket which clearly states that it is a feature request in the title. Explain your change in the description, and you can propose a Pull Request straight away.

## <a name="rfcs"></a> RFCs

Sometimes, major feature requests are "complex" or "substantial". In this case, Github Issues might not be the best tool to to present them because we will need a lot of going back and forth to reach a consensus.

So we ask that these feature request be put through a formal design process and have their specifications described in an "RFC" (request for comments) that will be validated by the team through a Pull Request Review.

The RFC process is intended to provide a consistent and controlled path for major features and directions of the project.

To submit an RFC follow those steps:

1. Discuss the RFC proposal with the core team through Github issues or other channels
2. Create the initial Github issue for the Feature Request if it doesn't already exist
3. Use the Design proposal issue template
4. Fill in the RFC, make sure to complete every required section
5. Submit the RFC as a Pull Request with the summary of the proposal in the PR description
6. Build consensus and integrate feedback from the reviewers
7. The Pull Request is either accepted (merged), rejected (closed) or postponed (given an "on hold" status)

## <a name="submit"></a> Submission Guidelines

### [Submitting an Issue](https://opensource.guide/how-to-contribute/#opening-an-issue)

Before you submit your issue search the [archive](https://github.com/OsgiliathEnterprise/platform/issues/issues?utf8=%E2%9C%93&q=is%3Aissue), maybe your question was already answered.

If your issue appears to be a bug, and has not been reported, open a new issue.
Help us to maximize the effort we can spend fixing issues and adding new
features, by not reporting duplicate issues. Providing the following information will increase the
chances of your issue being dealt with quickly:

-   **Overview of the issue** - if an error is being thrown a stack trace helps
-   **Motivation for or Use Case** - explain why this is a bug for you
-   **Reproduce the error** - an unambiguous set of steps to reproduce the error. 
-   **Related issues** - has a similar issue been reported before?
-   **Suggest a Fix** - if you can't fix the bug yourself, perhaps you can point to what might be
    causing the problem (line of code or commit)
-   **Platform Version(s)** - is it a regression?

Click [here](issue-template) to open a bug issue with a pre-filled template. For feature requests and enquiries you can use [this template][feature-template].

Issues opened without any of these info will be **closed** without any explanation.

### [Submitting a Pull Request](https://opensource.guide/how-to-contribute/#opening-a-pull-request)

Before you submit your pull request consider the following guidelines:

-   Search [GitHub](https://github.com/OsgiliathEnterprise/platform/pulls?utf8=%E2%9C%93&q=is%3Apr) for an open or closed Pull Request
    that relates to your submission.
-   If you want to modify the Platform, read our [Contributor guide](https://osgiliathenterprise.github.io/platform/contributor/toc.html)
-   Make your changes in a new git branch

    ```shell
    git checkout -b my-fix-branch master
    ```

-   Create your patch, **including appropriate test cases**.
-   Follow our [Coding Rules](#rules).
-   Generate a new Platform, and ensure that all tests pass

    ```shell
    molecule test
    ```

-   Test that the new platform runs correctly:

    ```shell
    ansible-inventory ...
    ```

-   You can generate our Continuous Integration (with GitHub Actions and Azure Pipelines) by following [this](#local-build)

-   Commit your changes using a descriptive commit message that follows our
    [commit message conventions](#commit-message-format).

    ```shell
    git commit -a
    ```

    Note: the optional commit `-a` command line option will automatically "add" and "rm" edited files.

-   Push your branch to GitHub:

    ```shell
    git push origin my-fix-branch
    ```

-   In GitHub, send a pull request to `OsgiliathEnterprise/platform:master`.
-   If we suggest changes then

    -   Make the required updates.
    -   Re-run the tests on your sample generated platform to ensure tests are still passing.
    -   Rebase your branch and force push to your GitHub repository (this will update your Pull Request):

        ```shell
        git rebase master -i
        git push -f
        ```

That's it! Thank you for your contribution!

#### Resolving merge conflicts ("This branch has conflicts that must be resolved")

Sometimes your PR will have merge conflicts with the upstream repository's master branch. There are several ways to solve this but if not done correctly this can end up as a true nightmare. So here is one method that works quite well.

-   First, fetch the latest information from the master

    ```shell
    git fetch upstream
    ```

-   Rebase your branch against the upstream/master

    ```shell
    git rebase upstream/master
    ```

-   Git will stop rebasing at the first merge conflict and indicate which file is in conflict. Edit the file, resolve the conflict then

    ```shell
    git add <the file that was in conflict>
    git rebase --continue
    ```

-   The rebase will continue up to the next conflict. Repeat the previous step until all files are merged and the rebase ends successfully.
-   Re-run the Platform tests on your sample generated project to ensure tests are still passing.
-   Force push to your GitHub repository (this will update your Pull Request)

    ```shell
    git push -f
    ```

#### After your pull request is merged

After your pull request is merged, you can safely delete your branch and pull the changes
from the main (upstream) repository:

-   Delete the remote branch on GitHub either through the GitHub web UI or your local shell as follows:

    ```shell
    git push origin --delete my-fix-branch
    ```

-   Check out the master branch:

    ```shell
    git checkout master -f
    ```

-   Delete the local branch:

    ```shell
    git branch -D my-fix-branch
    ```

-   Update your master with the latest upstream version:

    ```shell
    git pull --ff upstream master
    ```

## <a name="setup"></a> Generator development setup

See the [contributor guide](https://osgiliathenterprise.github.io/platform/contributor/toc.html)

### Fork the platform project

Go to the [platform project](https://github.com/OsgiliathEnterprise/platform) and click on the "fork" button. You can then clone your own fork of the project, and start working on it.

[Please read the GitHub forking documentation for more information](https://help.github.com/articles/fork-a-repo)

### Configure and install package for your platform

In your cloned `platform` project, type `git submodule update` to download the linked repositories, and `./configure` to download and configure everything needed to execute everything.

For testing, you will want to bootstrap a VM or a docker container.

### Use a text editor

We do not recommend any IDE to develop on the Platform as Ansible and affiliates are simply yaml: up to you to choose vim! 

## Local Build

On the root of the ansible role you want to test, first execute `./configure` to bootstrap necessary modules, then `molecule create` to bootstrap your vm or container.
You can then either connect to the VM or container, either execute `molecule converge` to execute the role.
Finally, `molecule destroy` will teardown the vm.

## <a name="rules"></a> Coding Rules

To ensure consistency throughout the source code, keep these rules in mind as you are working:

-   All features or bug fixes **must be tested** by one or more tests.
-   All files must follow the ansible lint.
-   Ansible files **must follow** [Ansible Style Guide](https://docs.ansible.com/ansible/latest/index.html).

Please ensure to run `ansible-lint` and `molecule test` on the project root before submitting a pull request.

## <a name="commit"></a> Git Commit Guidelines

We have rules over how our git commit messages must be formatted. Please ensure to [squash](https://help.github.com/articles/about-git-rebase/#commands-available-while-rebasing) unnecessary commits so that your commit history is clean.

If the commit only involves documentation changes you can skip the continuous integration pipelines using `[ci skip]` or `[skip ci]` in your commit message header.

### <a name="commit-message-format"></a> Commit Message Format

Each commit message consists of a **header**, a **body** and a **footer**.

```
<header>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

Any line of the commit message cannot be longer 100 characters! This allows the message to be easier
to read on GitHub as well as in various git tools.

Ideally, commits are signed using your GPG key.

### Header

The Header contains a succinct description of the change:

-   use the imperative, present tense: "change" not "changed" nor "changes"
-   don't capitalize first letter
-   no dot (.) at the end

### Body

If your change is simple, the Body is optional.

Just as in the Header, use the imperative, present tense: "change" not "changed" nor "changes".
The Body should include the motivation for the change and contrast this with previous behavior.

### Footer

The footer is the place to reference GitHub issues that this commit **Closes**.

You **must** use the [GitHub keywords](https://help.github.com/articles/closing-issues-via-commit-messages) for
automatically closing the issues referenced in your commit.

### Example

For example, here is a good commit message:

```
upgrade to Ansible 10.0

upgrade the platform builds to use the new Ansible,
see https://github.com/ansible/ansible/blob/stable-2.9/changelogs/CHANGELOG-v2.9.rst

Fix #1234
```

### Regular Contributor Guidelines

These are some of the guidelines that we would like to emphasize if you are a regular contributor to the project
or joined the [Osgiliath team](https://github.com/orgs/OsgiliathEnterprise/teams/osgiliath-platform).

-  We recommend not committing directly to master, but always submit changes through PRs.
-  Before merging, try to get at least one review on the PR.
-  Add appropriate labels to issues and PRs that you create (if you have permission to do so).
-  Follow the project's [Code of Conduct](https://github.com/OsgiliathEnterprise/platform/blob/master/CODE_OF_CONDUCT.md)
and be polite and helpful to users when answering questions/bug reports and when reviewing PRs.
-  We work on our free time so we have no obligation nor commitment. Work/life balance is important, so don't 
feel tempted to put in all your free time fixing something.

[issue-template]: https://github.com/OsgiliathEnterprise/platform/issues/new?template=BUG_TEMPLATE.md
[feature-template]: https://github.com/OsgiliathEnterprise/platform/issues/new?template=ENHANCEMENT_REQUEST.md
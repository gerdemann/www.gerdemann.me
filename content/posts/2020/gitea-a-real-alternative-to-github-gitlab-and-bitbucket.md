---
title: Gitea - a real alternative to Github, Gitlab and BitBucket
date: '2020-01-25'
tags: ['git', 'gitea', 'github', 'code']
draft: false
summary: If you work with code, there is no way around version control. The current standard for version control is git, a distributed version control for files.
---

If you work with code, there is no way around version control. The current standard for version control is git, a distributed version control for files. If you only work with code alone, it is usually enough to use git locally. However, many people want to save their code to another location and move their code to Github. Even if you work with more than one on a code base, you need a central server that everyone can access and push the code to there.


## Self-hosted code management

Alternatives to the [Github](https://github.com) Cloud are for example [Gitlab](https://gitlab.com) or [BitBucket](https://bitbucket.org). But if you use the cloud there, you don't have any control over your data, so I'm a friend of a self-hosted git instance. Here there are several ways to host a git instance now. (I'm only going into variants with web interface here).

In my professional environment I often see that BitBucket from Atlassian is used. Although the software is good, it also has a few disadvantages. First of all, it is relatively expensive if you have more than 10 developers and secondly, we noticed that BitBucket sometimes does not display the code correctly in the interface. So it can happen that code is not displayed, but in reality it is existing. Furthermore it is a Java software that needs a lot of server resources.

Gitab is often referred as a free version. But even here it can quickly become expensive if you need more advanced features. Gitlab, like BitBucket, also needs a lot of resources and is also relatively sluggish in its web interface.

## Gitea – faster, resource saving and free

A real alternative to the previous ones is [Gitea](https://gitea.io/). It is enormously performant, needs few resources and all features are free. The user interface is very much oriented towards the github and therefore a switch is very easy. Navigating the interface is very performant, which is probably because the software is written in Go. Gitea is a very enhanced fork of [Gogs](https://gogs.io/).

In Gitea you can easily make pull requests and review the code, the global search and repository search work well, and the code highlighting and diff view look good.

Another advantage is the well documented API and the possibility to set up various webhooks. This makes integration into various CI/CD tools very easy.

If you are afraid that Gitea can't handle many and large git repositories, I think I can make you feel better. Even many large repositories are no problem. A proof is the [Codeberg](https://codeberg.org/), where almost 1,800 repositories are now hosted with relatively few server resources. If you are looking for a new code management software, give Gitea a chance!

Because hosting is relatively simple too! A docker image is also available.
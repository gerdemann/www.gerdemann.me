---
title: git rerere – Do not always resolve the same conflicts
date: '2019-01-23'
tags: ['git', 'code']
draft: false
summary: Recently I came across a very interesting post from Christophe Porteneuve on Medium, in which `git rerere` was introduced.
---

Recently I came across a very interesting post from [Christophe Porteneuve](https://twitter.com/porteneuve) on [Medium](https://medium.com/@porteneuve/fix-conflicts-only-once-with-git-rerere-7d116b2cec67), in which `git rerere` was introduced. The "rerere" stands for **Re**use **Re**corded **Re**solution and this means that the resolution of conflicts is recorded and can be used again if necessary.

For me an so far unknown, but very helpful git command. I hope it helps you, so you don't have to solve the same conflicts all the time.

The original documentation for `git rerere` can be found [here](https://git-scm.com/docs/git-rerere).

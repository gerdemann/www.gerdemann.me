---
title: Neos 4.0 & Flow 5.0
date: '2018-05-06'
tags: ['neos', 'flow', 'php']
draft: false
summary: A few days ago a new major release of Neos and Flow was released. I would like to briefly introduce you to a few new features.
---

A few days ago a new major release of Neos and Flow was released. I would like to briefly introduce you to a few new features.

## Neos 4.0

Let's start with Neos. The CMS was released in version 4.0 and contains features like the new React UI, External Asset Sources and a new document rendering best practice.

### React UI

The new React UI is now the standard in the new Neos 4.0 and the new backend has been further improved and stabilized. The expandability of the new UI was discussed at the Neos Conference in Hamburg. This talk is highly recommended.

### Emojis and FontAwesome 5

As a further highlight the new FontAwesome version 5 was implemented in the backend and also the support for Emojis was made possible with Neos 4.0\. Among other things for the new Emojis the default database collation and character was changed to **utf8mb4**.

### External Asset Sources

But my personal favorite is the new possibility to include external asset sources. This makes it possible to access external asset sources such as Unsplash, Pexels, Dropbox etc. directly in the Neos Media module.

There are already some (almost) finished solutions:

* [Unsplash](https://github.com/daniellienert/assetsource-unsplash) by Daniel Lienert
* [Pexels](https://github.com/daniellienert/assetsource-pexels) by Daniel Lienert

### New document rendering best practice

Last but not least, there is now a new best practice to render a document. The whole document rendering process has been simplified and the [documentation](http://neos.readthedocs.io/en/stable/CreatingASite/RenderingCustomMarkup/PageRendering.html) has been updated.

## Flow 5.0

### PHP 7.1 and MySQL 5.7.x or MariaDB 10.2.x

Not only Neos has been further developed, Flow has also received innovations. The requirements for the flow framework were adapted and from version 5.0 PHP 7.1 and MySQL 5.7.x or MariaDB 10.2.x are required.

### PSR compatibility

In the new Flow version there were some adjustments to be compatible with the PSR specifications. The following improvements have been made:

* PSR-3 logging
* PSR-6 and PSR-16 support for caching framework
* PSR-11 Object Management

### Split Source for Settings.yaml

Flow 5.0 brings the possibility to structure the settings better. Similar to the NodeTypes and the routes it is now possible to split the Settings.yaml into different files. For example, there could be a _Settings.MyStuff.yaml_ or a _Settings.Override.yaml_.

## Conclusion

Neos 4.0 and Flow 5.0 are the logical further developments and lay the foundations for a great future. If you want to see more new features, take a look at the changelogs:

* [Neos 4.0 Changelog](https://neos.readthedocs.io/en/4.0/Appendixes/ChangeLogs/400.html)
* [Flow 5.0 Changelog](http://flowframework.readthedocs.io/en/5.0/TheDefinitiveGuide/PartV/ChangeLogs/500.html)

The update instructions can be found here:  
[https://www.neos.io/download-and-extend/upgrade-instructions-3-3-4-0.html](https://www.neos.io/download-and-extend/upgrade-instructions-3-3-4-0.html)



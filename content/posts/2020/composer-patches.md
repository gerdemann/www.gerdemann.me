---
title: Composer patches
date: '2020-02-16'
tags: ['php', 'composer']
draft: false
summary: There is a bug in a foreign composer package and you can't wait until the fix is installed and a new version is built? Then you can't avoid a patch.
---

There is a bug in a foreign composer package and you can't wait until the fix is installed and a new version is built? Then you can't avoid a patch. That's annoying, but sometimes it can't be changed. To make sure your patch is well documented and versioned, you can use the package *cweagans/composer-patches*. This allows you to put your patches centrally in your composer.json and thus make them versionable.

For the installation simply execute the following composer command:

```bash
composer require "cweagans/composer-patches:~1.0"
```

You can specify the patches in two different ways. First, you can specify them in the *composer.json* as follows

```json
{
  [...]

  "extra": {
    "patches": {
      "vendor/packagekey": {
        "Bugfix for the crazy bug": "patches/crazyBug.patch"
      }
    }
  }
}
```

or you create your own composer.patches.json file and specify the patches there. To be able to use the separate file, a reference must be given in the composer.json:

```json
{
  [...]

  "extra": {
    "patches-file": "/path/to/composer.patches.json"
  }
}
```

In the composer.patches.json you then specify the patches as follows:

```json
{
  "patches": {
    "vendor/packagekey": {
      "Bugfix for the crazy bug": "patches/crazyBug.patch"
    }
  }
}
```

Instead of a local patch file, a URL can be specified alternatively. On Github, for example, you can simply append a ".patch" behind a commit url:

```json
{
  "patches": {
    "vendor/packagekey": {
      "Bugfix for the crazy bug": "https://github.com/vendor/package/commit/43d[...]06b.patch"
    }
  }
}
```

With every ```composer install``` the patch is now applied.

I hope this little tip will give you a little more security if you have to patch a foreign package from the outside.
---
title: '1. Advent: Your own EelHelper'
date: '2017-12-03'
tags: ['neos', 'flow', 'php', 'eel']
draft: false
summary: On every Sunday in Advent I would like to show you a little tip for Neos.
---

On every Sunday in Advent I would like to show you a little tip for Neos.

Here's the first tip on how to create your own EelHelper. It is very easy to create your own EelHelper and use it in fusion.  Just create a new class and implement the following interface:

```php
Neos\Eel\ProtectedContextAwareInterface
```

An example EelHelper to get data from a repository looks like this:  

```php
namespace Package\Key\Eel\Helper;

use Neos\Flow\Annotations as Flow;
use Neos\Flow\Persistence\QueryResultInterface
use Neos\Eel\ProtectedContextAwareInterface;
use Package\Key\Domain\Repository\DataRepository;

/*
 * DataHelper
 */
class DataHelper implements ProtectedContextAwareInterface
{
    /**
     * @Flow\Inject
     * @var DataRepository
     */
    protected $dataRepository;

    /**
     * Get all data
     *
     * @return QueryResultInterface
     */
    public function getAllData() {
        return $this->dataRepository->findAll();
    }

    /**
     * All methods are considered safe, i.e. can be executed from within Eel
     *
     * @param string $methodName
     * @return boolean
     */
    public function allowsCallOfMethod($methodName) {
        return TRUE;
    }
}
```

In order to use the EelHelper in Fusion, it must be defined in the _Settings.yaml_:  

```yaml
    Neos:
      Fusion:
        defaultContext:
          'DataHelper': 'Package\Key\Eel\Helper\DataHelper'
```

The EelHelper can then be used in the fusion:  

```php
exampleEelValue = ${DataHelper.getData()}
```

I wish you a beautiful and peaceful Advent season!
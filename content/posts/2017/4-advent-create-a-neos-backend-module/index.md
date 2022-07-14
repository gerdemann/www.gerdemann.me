---
title: "4. Advent: Create a Neos backend module"
date: '2017-12-24'
tags: ['neos', 'flow', 'php']
draft: false
summary: It is very easy to create your own backend module in Neos. Be it to extend an existing module with a submodule or to create a completely own module.
---

It is very easy to create your own backend module in Neos. Be it to extend an existing module with a submodule or to create a completely own module.

For your own module you first create a controller of the type _ActionController_:  

```php
<?php
namespace Package\Key\Controller;

use Neos\Flow\Annotations as Flow;
use \Neos\Flow\Mvc\Controller\ActionController;

class MyBackendController extends ActionController
{

    /**
     * Index action
     *
     * @return void
     */
    public function indexAction()
    {
        $this->view->assign('myTemplateVar', 'Test-String');
    }
}
```

Then create a template under "Resources/Private/Templates/MyBackend/Index.html" for the action:  

```html
{namespace neos=Neos\Neos\ViewHelpers}

<div class="neos-content neos-container-fluid">
        <h1></h1>
        <p>{myTemplateVar}</p>
</div>
```

Then enter your new backend module in the _Settings.yaml_:  

```yaml
Neos:
  Neos:
    modules:
      'management':
        submodules:
          'myModule':
            label: 'My Module'
            controller: 'Package\Key\Controller\MyBackendController'
            description: 'An Example for implementing Backend Modules'
            icon: 'icon-star'
```

Finally, you only have to define the rights for the new module in _Policy.yaml_:  

```yaml
privilegeTargets:
  'Neos\Neos\Security\Authorization\Privilege\ModulePrivilege':
    'Package.Key:MyBackendModule':
      matcher: 'management/myModule'

roles:
  'Neos.Neos:Editor':
    privileges:
      -
        privilegeTarget: 'Package.Key:MyBackendModule'
        permission: GRANT
```
I wish you a lot of fun and enjoy the holidays. Merry Christmas to you and your families!
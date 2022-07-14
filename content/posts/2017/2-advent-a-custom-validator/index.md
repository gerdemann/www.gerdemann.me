---
title: '2. Advent: A custom validator'
date: '2017-12-10'
tags: ['neos', 'flow', 'php']
draft: false
summary: On the second Advent I want to show you how to create your own validator. With the validator you can validate models, actions of controllers and forms.
---

On the second Advent I want to show you how to create your own validator. With the validator you can validate models, actions of controllers and forms.

For a validator, all you have to do is create a new class, which is best inherited from the _AbstractValidator:_  

```php
<?php
namespace Package\Key\Validation\Validator;

use Neos\Flow\Annotations as Flow;
use Neos\Flow\Validation\Validator\AbstractValidator;

/**
 * A validator for checking value is "foo" or "bar"
 */
class FooBarValidator extends AbstractValidator {

    /**
     * @var array
     */
    protected $supportedOptions = array(
        'type' => array('foo', 'Types are "foo" or "bar"', 'string', false)
    );

    /**
     * Check if the given value is 'foo' or 'bar'
     *
     * @param mixes $value
     * @return void
     */
    protected function isValid($value) {
        if (isset($this->options['type']) && $this->options['type'] === 'bar' && $value !== 'bar') {
            $this->addError('The value must be equal to "bar"', 1512760555);
        } elseif ($value !== 'foo') {
            $this->addError('The value must be equal to "foo"', 1512760556);
        }
    }
}
```

Once you have created the validator, you can attach it to a property of a model, for example, and have it automatically validated:  

```php
<?php
namespace Package\Key\Domain\Model;

use Neos\Flow\Annotations as Flow;

class Model {

    /**
     * @Flow\Validate(type="Package\Key\Validation\Validator\FooBarValidator")
     */
    protected $foo;

    // Add getters and setters here
}
```

You can also check an argument of an action:  

```php
<?php
namespace Package\Key\Controller;

use Neos\Flow\Annotations as Flow;

class ExampleController extends \Neos\Flow\Mvc\Controller\ActionController {

    /**
     * @param string $foo
     * @Flow\Validate(argumentName="foo", type="Package\Key\Validation\Validator\FooBarValidator")
     */
    public function updateAction(string $foo) {
        // action code here
    }
}
```

Or you can add the validator to a form field. To do this, you first have to extend the form settings:  

```yaml
Neos:
  Form:
    presets:
      default:
        validatorPresets:
          'Package.Key:FooBar':
            implementationClassName: Package\Key\Validation\Validator\FooBarValidator
```

The validator can then be attached to a field:  

```yaml
...
renderables:
  -
    type: 'Neos.Form:Page'
    identifier: 'page-one'
    renderables:
      -
        type: 'Neos.Form:SingleLineText'
        identifier: 'foo'
        validators:
          - identifier: 'Package.Key:FooBar'
...
```

Have a nice and contemplative time before Christmas!
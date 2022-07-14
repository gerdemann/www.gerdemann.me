---
title: 'How to avoid memory problems during long-running processes?'
date: '2017-02-13'
tags: ['neos', 'flow', 'php']
draft: false
summary: If you have long-running processes such as a job queue worker, you often get memory problems. Especially with PHP, workers are a problem because the memory can not be released again. With Flow, it is very easy to create such workers.
---

If you have long-running processes such as a job queue worker, you often get memory problems. Especially with PHP, workers are a problem because the memory can not be released again. With Flow, it is very easy to create such workers. You just have to create a CommandController with an action:  

```php
namespace Vendor/FooBar/CommandController;

/**
 * A worker command controller
 */
class WorkerCommandController
{
    /**
     * Run Command
     * 
     * A long-running command
     *
     * @return void
     */
    public function runCommand()
    {
        do {
            $this->getMessageAndExecute();
        } while (true);
    }

    /**
     * Get message and execute
     *
     * @return void
     */
    public function getMessageAndExecute()
    {
        // Get and execute Message
    }
}
```

However, if the execution of getMessageAndExecute() consumes a lot of memory, one quickly reaches the memory limit of PHP. Fortunately, Flow offers us the possibility of so-called sub-requests, with which we can simply create further processes. So, we can simply move our method into another (sub-)command and call this command in our runCommand:  

```php
namespace Vendor/FooBar/CommandController;

use Neos\Flow\Annotations as Flow;

/**
 * A worker command controller
 */
class WorkerCommandController
{
    /**
     * @Flow\InjectConfiguration(package="Neos.Flow")
     * @var array 
     */
    protected $flowSettings;

    /**
     * Run Command
     * 
     * A long-running command
     *
     * @return void
     */
    public function runCommand()
    {
        do {
            Scripts::executeCommand('vendor.foobar:worker:execute', $this->flowSettings, true, array());
        } while (true);
    }

    /**
     * Execute Command
     * 
     * Get and execute message command
     *
     * @return void
     */
    public function executeCommand()
    {
        $this->getMessageAndExecute();
    }

    /**
     * Get message and execute
     *
     * @return void
     */
    public function getMessageAndExecute()
    {
        // Get and execute Message
    }
}
```

And from Flow version 3.3 there is even the possibility to execute the sub-command asynchronously. To do this, simply use the method Scripts::executeCommandAsync():  

```php
/**
 * Run Command
 * 
 * A long-running command
 *
 * @param bool $async
 * @return void
 */
public function runCommand(bool $async = true)
{
    do {
        if ($async) {
            Scripts::executeCommandAsync('vendor.foobar:worker:execute', $this->flowSettings, array());
        } else {
            Scripts::executeCommand('vendor.foobar:worker:execute', $this->flowSettings, true, array());
        }
    } while (true);
}
```

A good basis for a job queue package is [Flowpack/jobqueue-common](https://github.com/Flowpack/jobqueue-common). So have fun with long-running tasks and Flow!
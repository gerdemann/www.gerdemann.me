---
title: '3. Advent: Logging in Flow'
date: '2017-12-17'
tags: ['neos', 'flow', 'php', 'logging']
draft: false
summary: The third part of this small series is about logging in Flow. You can easily log with the standard logger or you can create your own logger.
---

The third part of this small series is about logging in Flow. You can easily log with the standard logger or you can create your own logger.

First, I'll show you how to write into the standard log quickly and easily.  

```php
<?php
namespace Package\Key\Service;

use Neos\Flow\Annotations as Flow;
use Neos\Flow\Log\SystemLoggerInterface;

class ExampleService
{
    /**
     * @Flow\Inject
     * @var SystemLoggerInterface
     */
    protected $logger;

    /**
     * My function
     *
     * @return void
     */
    public function myFunction()
    {
        $this->logger->log('my log message');
    }
}
```

To create your own logger e. g. for your own package, you only have to do a few things. To do this, first set the logging settings in the _Settings.yaml_:  

```yaml
Package:
  Key:
    log:
      backendOptions:
        fileBackend:
          logFileURL: '%FLOW_PATH_DATA%Logs/MyLog.log'
          createParentDirectories: true
          severityThreshold: '%LOG_DEBUG%'
          maximumLogFileSize: 10485760
          logFilesToKeep: 1
          logMessageOrigin: false
```

Then create a logger interface class:  

```php
<?php
namespace Package\Key;

/**
 * MyLogger Interface
 */
interface LoggerInterface extends \Neos\Flow\Log\LoggerInterface
{
}
```

And last but not least you have to fill the interface in the _Objects.yaml_:  

```yaml
Package\Key\LoggerInterface:
  scope: singleton
  factoryObjectName: Neos\Flow\Log\LoggerFactory
  factoryMethodName: create
  arguments:
    1:
      value: 'Package.Key'
    2:
      value: 'Neos\Flow\Log\Logger'
    3:
      value:
        fileBackend: 'Neos\Flow\Log\Backend\FileBackend'
    4:
      setting: Package.Key.log.backendOptions
```

Afterwards you can use the LoggerInterface and write it into your own log file:  

```php
<?php
namespace Package\Key\Service;

use Neos\Flow\Annotations as Flow;
use Package\Key\LoggerInterface;

class ExampleService
{
    /**
     * @Flow\Inject
     * @var LoggerInterface
     */
    protected $logger;

    /**
     * My function
     *
     * @return void
     */
    public function myFunction()
    {
        $this->logger->log('my log message');
    }
}
```
You can not only log into a file with Flow, you can also use one of the other [logging backends](https://github.com/neos/flow-development-collection/tree/master/Neos.Flow.Log/Classes/Backend) and create your own backends. With this you can easily log into [Graylog](https://www.graylog.org/) for example.
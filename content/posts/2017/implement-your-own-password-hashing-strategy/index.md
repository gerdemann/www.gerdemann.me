---
title: 'Implement your own password hashing strategy'
date: '2017-03-24'
tags: ['neos', 'flow', 'php', 'passwords']
draft: false
summary: What is a password hashing strategy and why do I need to implement my own? Let's assume that we have an existing page with user accounts and want to add them to our new Neos page.
---

What is a password hashing strategy and why do I need to implement my own? Let's assume that we have an existing page with user accounts and want to add them to our new Neos page. In the old page, the passwords are only hashed, but should also remain on the new page. Finally, not all users should get a new password. This is exactly the case for our own password hashing strategy, which allows us to replicate the hashing strategy of the existing page and use it in the new one.

### Implement a new strategy

Assuming our existing site is currently using [SaltedSha1](https://de.wikipedia.org/wiki/Secure_Hash_Algorithm) as hashing strategy. What do we have to do to get the strategy in the new system?

First, we need to create a new class that implements the PasswordHashingStrategyInterface:  

```php
<?php
namespace My\Package\Security\Cryptography;

use Neos\Flow\Security\Cryptography\PasswordHashingStrategyInterface;

/**
 * A salted SHA1 based password hashing strategy
 */
class SaltedSha1HashingStrategy implements PasswordHashingStrategyInterface
{
    /**
     * Hash a password using salted SHA1
     *
     * @param string $password The cleartext password
     * @param string $staticSalt ignored parameter
     * @return string A hashed password with salt
     */
    public function hashPassword($password, $staticSalt = null)
    {
        $salt = '';
        for ($i = 1; $i <= 7; $i++) {
            $salt .= chr(rand(0, 255));
        }
        return base64_encode(sha1($password . $salt, true) . $salt);
    }

    /**
     * Validate a hashed password using salted SHA1
     *
     * @param string $password The cleartext password
     * @param string $hashedPasswordAndSalt The hashed password with salt
     * @param string $staticSalt ignored parameter
     * @return boolean TRUE if the given password matches the hashed password
     */
    public function validatePassword($password, $hashedPasswordAndSalt, $staticSalt = null)
    {
        $decoded = base64_decode($hashedPasswordAndSalt);
        $salt = substr($decoded, 20);
        $passwordHash = base64_encode(sha1($password . $salt, true) . $salt);
        return $hashedPasswordAndSalt === $passwordHash;
    }
}
```

Then we have to announce our new strategy in the _Settings.yaml_:  

```yaml
Neos:
  Flow:
    security:
      cryptography:
        hashingStrategies:
          saltedsha1: My\Package\Security\Cryptography\SaltedSha1HashingStrategy
```

Afterwards, we can store the users with the old password hashes in our database and the old passwords can still be used as usual. The old password hashes are stored in the column _credentialssource_ in table _neos\_flow\_security\_account_ in the following format:  

```php
    saltedsha1=>###HASHED_PASSWORD###
    
    // example:
    saltedsha1=>42PdBsPDxSQwk9JH6ETseNtTlygS4R8mf+OJ
```

So easy is it to use the old hashed passwords with Neos/Flow.
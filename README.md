# Hashing Password System Concept

## Example of classic password systems
Somebody's Facebook password may be `monkey.fa` and their Twitter password may be `monkey.tw`.

### Pros
- **Variation** - Most of the passwords are different
- **Memorability** - The owners know them all off the top of their head
- **Security (kind of)** - The passwords are not stored in a third-party Password Manager with potential security flaws

### Cons
- **Predictability** - if an attacker got a hold of one password, they could easily guess the other passwords. For example, Google would be `monkey.go`


## The "use-hash-as-password" concept

### 1. Use the hash ***as*** the password. 
As little as one character difference changes the entire hash. We can ***eliminate ALL predictability*** by using the ***SHA256 hash of the product of the simple password system*** as the password.

### 2. Distort the hash before using it as the password.
An attacker (although unlikely) could use an hash-reversing tool to reveal the original password. To prevent this we will distort the hash by removing every second character.

## Limitations

There are some ridiculous password rules (see [here](https://github.com/duffn/dumb-password-rules) for some stupid examples). For this reason, this tool can be used to generate a secure password from your password system for ***most*** services but not ***all***.

## Run the hasher tool

```
$ python hasher.py
```

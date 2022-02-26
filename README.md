# Improving password systems with SHA256

## Password system example
Jordan uses a password system rather than a password manager. Their Facebook password is `monkey.fa` and their Twitter password is `monkey.tw`.

## Pros
- All of Jordan's passwords are different
- They know them all off the top of their head
- They are not stored in a third-party Password Manager with potential security flaws

## Cons

- If an attacker got a hold of one of Jordan's passwords, they could easily guess Jordan's other passwords. Google would be `monkey.go`


## Improving this with SHA256

Because the entire hash changes when as little as one character differs, we can prevent the other passwords being guessed by using SHA256 to hash the simple password system and then use the hash as the password.

## Further improvements

Hash distortion:
If an attacker recognises it as a hash, they may use an unhashing tool to reverse the hash if the original password was generic enough. To prevent this we will remove every second character so it is no longer a pure SHA256 hash.

## Where this concept falls through

Different services have different password rules (see here for stupid examples: https://github.com/duffn/dumb-password-rules). For this reason, this tool can be used to generate a secure password from your password system for MOST services but not ALL.

## Usage

```
$ python hasher.py
```
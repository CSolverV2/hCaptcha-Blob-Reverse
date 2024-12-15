# hCaptcha-Blob-Reverse
Not a full reverse, but a dynamic sandbox to encrypt hCaptcha's events into the `fingerprint_blob` value

# Updates
- `v1.1` -> `Added a bypass for hCaptcha's anti-debug (this was causing it to encrypt wrong before)`

# `fingerprint_blob`

The `fingerprint_blob` is an encrypted array of `events` which are identifying information about a user

These `events` are used to verify if it is a bot or a human solving the captcha

Well, guess what? We can encrypt these values ourselves via sandbox

This means the script will fetch the `hsw` script, modify it, & run it to encrypt custom values

# How Blob Encryption Works

It first generates a `Uint8Array` (byte array) of 16 bytes (setting up the IV)

Then it fills those with random values (filling up the IV)

Then, it uses the key & the iv to encrypt the payload via `AES-CBC` 

The IV & encrypted events are ut into base64 and seperated by a period (`.`)

Here is an Example output -> `bYVoSStTzWH7bJvNP2SycA==.giM0MxiKZP6JuPpzfx16fw==`

The first half (`bYVoSStTzWH7bJvNP2SycA==`) is the `Base64-Encoded` IV & the second half (`giM0MxiKZP6JuPpzfx16fw==`) is the encrypted data `Base64-Encoded`

# Usage

Simply open `blob.py` scroll to the bottom and modify the version to the version you need to encrypt for

Run `blob.py` it will print out the encrypted result :) 

# Contact

If you need help or want a full reverse (with key and stuff) you can contact me on telgram or discord

`Telegram` -> `@CSolverV2` | https://t.me/csolver

`Discord` -> `CSolver.ai` | https://discord.gg/CBr7taaYeh

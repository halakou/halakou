# Security Policy

Report vulnerabilities **privately**. Do not open a public issue for secrets, webhook bypasses, payment / Telegram Stars bugs, or anything that could harm users.

## Scope

Public products under [github.com/halakou](https://github.com/halakou):

- [Blinkboard](https://github.com/halakou/blinkboard) — [blinkboard.pages.dev](https://blinkboard.pages.dev)
- [Aura Drift](https://github.com/halakou/aura-drift) — [auradrift.pages.dev](https://auradrift.pages.dev)
- [InboxBox](https://github.com/halakou/inboxbox) — [inboxbox.halakou.workers.dev](https://inboxbox.halakou.workers.dev)
- [Rackside](https://github.com/halakou/rackside) — [halakou.github.io/rackside](https://halakou.github.io/rackside/)

Backends are Cloudflare Workers + D1. Bot tokens and webhook secrets live in Cloudflare `secret_text`, not git.

## How to report

Use GitHub **Private vulnerability reporting** on the affected repository (Security tab). Include:

1. Product name and live URL
2. Steps to reproduce
3. Impact (data, payments, account takeover)
4. Your contact

I will acknowledge private reports and patch production Workers before any public write-up.

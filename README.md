<p align="center">
  <img src="logo.png" width="128" alt="Halakou" />
</p>

<h1 align="center">Halakou</h1>

<p align="center">
  <strong>Telegram Mini Apps · Cloudflare Workers · Telegram Stars</strong>
</p>

<p align="center">
  Production bots and public pages on Cloudflare’s free tier:<br />
  Workers, D1, Pages, and Stars payments — photos stay in Telegram as <code>file_id</code>.
</p>

<p align="center">
  <a href="https://blinkboard.pages.dev">Blinkboard</a> ·
  <a href="https://auradrift.pages.dev">Aura Drift</a> ·
  <a href="https://inboxbox.halakou.workers.dev">InboxBox</a> ·
  <a href="https://halakou.github.io/rackside/">Rackside</a>
</p>

---

## Selected work

### [Blinkboard](https://github.com/halakou/blinkboard)
Telegram-first rented pages. Buyers pay with Telegram Stars. The Worker stores listing data in D1; photos never leave Telegram.

**Live:** [blinkboard.pages.dev](https://blinkboard.pages.dev)

### [Aura Drift](https://github.com/halakou/aura-drift)
Flow-combat Mini App. WebGL1 bloom corridor with a Canvas2D fallback, shipped as Cloudflare Pages + Workers. Stars donate.

**Live:** [auradrift.pages.dev](https://auradrift.pages.dev) · bot [@Auradrift_bot](https://t.me/Auradrift_bot)

### [InboxBox](https://github.com/halakou/inboxbox)
Private file inbox inside Telegram. The Worker stores `file_id` only — no object-storage copies of user files.

**Live:** [inboxbox.halakou.workers.dev](https://inboxbox.halakou.workers.dev) · bot [@inboxbox_save_bot](https://t.me/inboxbox_save_bot)

### [Rackside](https://github.com/halakou/rackside)
Sixty-second briefs on local models, Ollama, llama.cpp, and self-hosted agents.

**Live:** [halakou.github.io/rackside](https://halakou.github.io/rackside/)

---

## Stack

| Layer | What I use |
| --- | --- |
| Edge | Cloudflare Workers, Pages |
| Data | D1 |
| Payments | Telegram Stars |
| Clients | Telegram Mini Apps |
| Ship | Wrangler, GitHub Actions |

I keep production on the Cloudflare free tier: account-level Workers Observability, authenticated AI Gateway (cache + rate limit + logs), and Green Compute. Custom domains are optional; public surfaces are `*.pages.dev` and `halakou.workers.dev`.

---

## How I ship

- **Telegram as the store.** Media stays as `file_id`. No R2 copies of user photos unless the product needs object storage.
- **Workers + D1 as the backend.** One Worker per product, cron where the product needs it (`scheduled` on Blinkboard).
- **Public pages as the resume.** Each Mini App has a live URL a recruiter can open without Telegram.
- **Secrets stay secrets.** Bot tokens and webhook secrets are Cloudflare `secret_text`, not git.

Based in Iran. I build and operate the stack myself.

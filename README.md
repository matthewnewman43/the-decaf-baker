# The Decaf Baker 🍪

Single-page landing site for **The Decaf Baker** — small-batch bakery. Choco tacos, cookie buckets, custom smash-heart cakes. Weekend pickup pre-orders + custom cake consults.

**Vibe:** pastel checkerboard picnic · nostalgic millennial · "the ice-cream-truck stuff, but better than you remember it."

> **Updating prices/times without code:** see [UPDATING.md](UPDATING.md) — a form in the Actions tab or a one-line edit on github.com.

## How the site builds

- **`template.html`** — the page, with `{{token}}` slots for adjustable facts
- **`site.yaml`** — the values: baker name, town, order deadline, pickup window/spot, payment methods, lead times, deposit, prices
- **`render.py`** — zero-dependency renderer (`template.html` + `site.yaml` → `index.html`); fails the build on unknown or missing tokens
- On every push to `main`, the deploy workflow renders and publishes to the `gh-pages` branch — so **editing `site.yaml` and pushing is all it takes to change a price or pickup time**. `index.html` is a build artifact (gitignored on `main`).

## Site structure (`template.html`)

| # | Section | Job |
|---|---------|-----|
| 1 | **Sticky nav** | Brand + anchor links + always-visible "Pre-Order Pickup" CTA |
| 2 | **Hero** | Headline, value prop, dual CTA (pre-order / custom cake), scarcity line (order-by deadline) |
| 3 | **Marquee** | Product ticker — energy + SEO-ish keyword strip |
| 4 | **Signature menu** | 6 product cards: Choco Taco, Cookie Bucket, Chocolate Chip, Custom Cakes, Chocolate-Covered Everything, Rotating Cast. Each: image, sensory copy, price chip, social-proof tag |
| 5 | **Our Story** | Mentor-toned "why decaf?" origin story on mint checkerboard |
| 6 | **Reviews** | 3 rotated testimonial cards (swap in real reviews / DM screenshots) |
| 7 | **How to order + FAQ** | 3-step pickup flow, custom-cake consult box, 6 objection-handling FAQs |
| 8 | **Final CTA** | Scarcity close + DM button |
| 9 | **Footer** | Handle, town, cottage-license line |

## Design system

- **Palette** (from the IG grid): `cream #FFF9F0` · `cocoa #4A2C2A` · `mint #BDE7D4` · `butter #FDE49B` · `bubble #F9C6D5` · `sky #BBD9F7` · `blush #F4A88E`
- **Motif:** CSS checkerboard (`repeating-conic-gradient`) = the wax-paper wrap, used as borders/dividers/avatars
- **Type:** Fraunces (display) + Nunito (body), Google Fonts
- **Tailwind:** Play CDN for prototyping — move to a proper Tailwind build before production

## Before launch

1. **Facts:** review `site.yaml` — every price, time, and policy lives there now.
2. **Images:** all six menu photos are in place. Still needed: `about-baker.jpg` (photo of Kaley for the story section). The five `menu-*.jpg` files are ~400px crops from IG grid screenshots — swap for full-res originals when convenient.
3. **Reviews:** replace the three sample testimonials with real ones (in `template.html`).
4. **Ordering links:** every CTA points at `instagram.com/thedecafbaker` (DM ordering). Swap hrefs for a form/Square/Shopify link whenever you upgrade.

## Preview locally

```
python3 render.py   # writes index.html
```

Then open `index.html` in a browser.

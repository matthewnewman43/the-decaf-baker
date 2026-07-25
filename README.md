# The Decaf Baker 🍪

Single-page landing site for **The Decaf Baker** — small-batch bakery. Choco tacos, cookie buckets, custom smash-heart cakes. Weekend pickup pre-orders + custom cake consults.

**Vibe:** pastel checkerboard picnic · nostalgic millennial · "the ice-cream-truck stuff, but better than you remember it."

## Site structure (`index.html`)

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

## Before launch — swap the placeholders

1. **Facts in `[brackets]`:** prices, town, pickup window, order deadline, payment methods, lead times, your name/year, cottage food license.
2. **Images:** `images/choco-taco.jpg` is in place (hero + Choco Taco card). Still needed in `images/`: `menu-cookie-bucket.jpg`, `menu-choc-chip.jpg`, `menu-heart-cake.jpg`, `menu-dipped.jpg`, `menu-rotating.jpg`, `about-baker.jpg`.
3. **Reviews:** replace the three sample testimonials with real ones.
4. **Ordering links:** every CTA points at `instagram.com/thedecafbaker` (DM ordering). Swap hrefs for a form/Square/Shopify link whenever you upgrade.

## Preview locally

Just open `index.html` in a browser — no build step needed.

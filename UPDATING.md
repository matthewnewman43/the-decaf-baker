# How to update the website (no coding needed)

The live site is **https://matthewnewman43.github.io/the-decaf-baker/**.
Prices, pickup times, and policies all live in one small settings file — you never touch the page itself. There are two ways to change them, both from any browser (phone works too).

---

## Option 1: The form (easiest)

Best for the common stuff: prices, order deadline, pickup window/spot, payment methods, cake deposit.

1. Go to the repo's **Actions** tab: https://github.com/matthewnewman43/the-decaf-baker/actions
2. In the left sidebar, click **"Update site settings"**
3. Click the **"Run workflow"** dropdown button (right side)
4. Fill in **only the boxes you want to change** — anything left blank stays as it is
5. Click the green **"Run workflow"** button
6. Wait ~1 minute. When the run shows a green ✓, the live site is updated.

Example: to raise the choco taco to $7, type `7` in the "Choco Taco price" box and run. Done.

---

## Option 2: Edit the settings file directly

For anything not on the form (baker name, town, bake day, delivery policy, lead times):

1. Open the settings file: https://github.com/matthewnewman43/the-decaf-baker/blob/main/site.yaml
2. Click the **pencil icon** (✏️, top right of the file)
3. Change the text after the colon on any line, for example:
   ```
   pickup_window: 10 AM – 1 PM      →      pickup_window: 9 AM – noon
   ```
   Keep the part before the colon exactly as it is.
4. Click **"Commit changes..."** (green button), then **"Commit changes"** again in the popup
5. Wait ~1 minute — the site rebuilds and updates itself.

---

## What each setting does

| Setting | Shows up as |
|---|---|
| `baker_name` | "Hi, I'm ___" in the story + the sign-off |
| `town` | Hero, pickup instructions, footer |
| `order_deadline` | "Order by ___" in three places |
| `bake_time` | "Your order is baked ___" |
| `pickup_window` / `pickup_spot` | Step 3 of "How weekend pickup works" |
| `payment_methods` | Step 1 payment line |
| `delivery_policy` | First sentence of the delivery FAQ |
| `cake_lead_time` / `holiday_lead_time` | Custom cake box + FAQ |
| `cake_deposit` | "A ___ deposit locks your date" |
| `price_*` | The price chips on the menu cards (numbers only — no $) |

## If something goes wrong

- **The run shows a red ✗:** the settings file probably has a typo (like a deleted colon). Open site.yaml (Option 2) and compare against the table above — every line needs `name: value`.
- **The site didn't change:** give it 2 minutes and refresh with a hard reload (Ctrl+Shift+R / Cmd+Shift+R). Phones cache aggressively — try a private tab.
- **Stuck?** Nothing here can break the bakery data permanently — every change is saved in history and can be undone. Ask your friendly neighborhood developer (or Claude) to roll it back.

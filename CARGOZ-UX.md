# Cargoz — Audience, User & UX Principles

> This document defines who the Cargoz user is, how they think, and how every design decision should serve them.
> Use this as the foundation before making any UI or UX decision on the Cargoz platform.

---

## Who the User Is

**Primary persona: The Business Owner**

- Age 35–50
- South Asian expat living in Dubai or KSA (Pakistani, Indian, Sri Lankan)
- Runs an SME — trading, retail, e-commerce, FMCG, or import/export
- Non-technical. Does not use design tools, dev consoles, or complex software
- Makes decisions based on trust, price, and availability — in that order
- WhatsApp is their primary communication tool. Email is secondary
- Accesses the platform on a Windows laptop with an LCD monitor, often in a bright office
- English is a second language. Reads carefully, word by word
- Has been burned before — by unclear contracts, hidden fees, or unreliable vendors

**Secondary persona: The Operations Manager**

- Age 28–40
- Reports to the business owner
- More tech-comfortable but still not a power user
- Does the research, the business owner makes the final call
- Needs to justify the decision upward — so data and comparisons matter

---

## How the User Thinks

**They are cautious, not impulsive.**
They have committed money to goods. Those goods need a safe, accessible, affordable place. The stakes are real. They will read every line before clicking anything.

**They compare on price first, then availability, then trust.**
Price is the entry point. If the price is hidden or unclear, they leave. Once price passes the threshold, they ask: can I move in now? Then: is this place trustworthy?

**They don't know logistics vocabulary.**
Terms like "palletisation", "CBM", "3PL", "ambient storage" mean nothing without context. Every label must be in plain English. Every metric must have a human explanation alongside it.

**They trust signals, not claims.**
A badge that says "Verified by Cargoz" is trusted. A paragraph that says "we are a trusted platform" is ignored. Show, don't tell.

**They are anxious about commitment.**
They want to know exactly what they're signing up for before they hand over any personal or financial information. The more transparent the platform is upfront, the more likely they are to convert.

**They use WhatsApp to close deals.**
The final decision — even after going through an online estimate flow — is often confirmed over WhatsApp. The platform should make it easy to share, forward, and discuss estimates informally.

---

## Physical and Environmental Constraints

- **Screen:** Windows laptop, 14–15 inch, LCD panel. Often glossy. Often used in bright offices with window glare.
- **Implication:** Low contrast fails. Text below 16px is hard to read. Thin fonts disappear. High contrast and generous sizing are non-negotiable.
- **Browser:** Chrome on Windows. No Safari, no Firefox assumptions.
- **Internet:** Generally reliable but not always fast. Avoid heavy animations or large unoptimised assets.
- **Input:** Mouse and keyboard. No touchscreen assumptions on desktop.

---

## UX Principles for Cargoz

### 1. Price is always visible

Never hide the price behind a step, a click, or a form. The monthly estimate should be visible the moment the user lands on any warehouse-related screen. It is the first thing they look for and the first reason they leave if it is missing.

### 2. Plain English, always

Every label, heading, and tooltip must be written as if explaining to someone who has never used a warehouse platform before. Use conversational language:

- ✓ "When can you move in?" not "Availability date"
- ✓ "How high you can stack goods" not "Usable ceiling clearance"
- ✓ "Who manages your goods?" not "Warehouse management model"
- ✓ "Cargoz verified" not "Platform-certified listing"

If a term needs explanation, add a sub-label in grey beneath the main label. Never remove the label itself.

### 3. Trust signals are structural, not decorative

Trust is not built through marketing copy. It is built through:
- Verified badges on warehouse listings (green, with a checkmark)
- Availability dates shown as real dates, not vague language
- Customer ratings with review counts alongside the stars
- Cargoz branding present on every estimate and document
- Consistent, professional design across every touchpoint

Trust signals should appear at every decision point — on cards, in the comparison table, on the estimate document.

### 4. Traffic light colors carry meaning — use them consistently

- **Green** (`#004B2F` on `#F0FFFA`) = available, verified, positive, immediate
- **Orange** (`#6B3100` on `#FFF5ED`) = coming soon, pending, caution
- **Purple** (`#7957FF`) = Cargoz brand, primary actions, selected/shortlisted state
- **Red** is not used. Negative states use orange, not red — red implies error, not uncertainty.

Never use these colors decoratively. Every green badge should mean something is confirmed. Every orange badge should mean something is upcoming or in progress.

### 5. Hierarchy communicates importance

The most important information must look the most important. Size, weight, and spacing are the tools:

- **Total price:** Large, bold, unmissable
- **Availability and rating:** Medium, prominent
- **Physical specs and costs:** Standard size, readable
- **Checklist items (services, equipment, compliance):** Compact, scannable

A flat design where everything looks the same weight tells the user that everything is equally important — which means nothing is.

### 6. Reduce anxiety at every step

- Show the user exactly where they are in the process (stepper navigation)
- Show them what comes next before they commit
- Never ask for personal or financial information before showing the estimate
- Provide a "Go back" escape at every step
- Allow removal of warehouses from a comparison without losing the whole session

### 7. CTAs must be clear and singular

Every page has one primary action. Secondary actions exist but should never compete visually.

- Primary CTA: solid purple, full-width or prominent placement
- Secondary CTA: ghost style, always subordinate
- The label must describe the outcome, not the action: "Get my estimate" not just "Submit"
- Never have two purple buttons on the same screen

### 8. Forms should be short

The user's tolerance for forms is low. Every field added to a form is a reason to abandon. The estimate form should have a maximum of 4 fields:
1. Storage quantity
2. Duration
3. Type of goods
4. Special requirements (optional)

If more information is needed, collect it after the estimate is generated — not before.

### 9. Mobile awareness (secondary priority)

The primary surface is desktop. However, the user may share or review estimates on their phone via WhatsApp. Estimates and documents should be legible on mobile even if they are not fully interactive. Minimum tap targets of 44px if interactive elements are present on mobile.

### 10. RTL readiness

A significant portion of the user base reads Arabic. Layouts should be structured to support right-to-left mirroring without breaking. Avoid hardcoded left-alignment assumptions in components. Icon directions (arrows, chevrons) should flip in RTL mode.

---

## What Bad UX Looks Like for This User

- A price hidden behind a "Get Quote" form
- A table where every row looks the same visual weight
- Labels that use logistics industry jargon without explanation
- A verification badge that isn't explained (what does "verified" mean?)
- A modal that blocks the comparison table the user was just reading
- A form with more than 4 fields before showing a result
- Thin fonts or small text on a bright screen
- Inconsistent use of green and orange (one warehouse uses green for "coming soon", another uses orange — user loses trust)
- No "Go back" option after a step
- A design that looks great at 100% zoom on a Retina MacBook but breaks on a 125% scaled Windows laptop

---

## Summary Card (paste this at the top of any new session)

```
Cargoz user: South Asian business owner, 35–50, Dubai/KSA.
Non-technical. English second language. Windows LCD screen.
Decides on: price → availability → trust.
Communicates on WhatsApp.
Needs: plain English, visible prices, trust badges, short forms, clear hierarchy.
Fears: hidden fees, unclear commitment, untrustworthy vendors.
Design rule: if it would confuse a 45-year-old trading company owner in Deira, redesign it.
```

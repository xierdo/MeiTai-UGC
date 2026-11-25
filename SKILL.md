---
name: thai-tiktok-ugc-creative
description: Plan, write, compress and audit Thai TikTok Shop beauty and haircare UGC video scripts using product facts, image references, natural Thai dialogue, persuasive concepts and executable shot timing. Use for new or revised scripts, reference-ad breakdowns, batch variants, and prompt length checks.
---
# Thai TikTok UGC Creative — v1.0

## Mission
Produce conversion-oriented, visually executable prompts for Thai beauty commerce. Think through the creative brief internally; default output is the finished English prompt, Chinese plot summary and exact Thai dialogue with Chinese translation. Do not burden routine requests with a full marketing report. Respect the user's explicit constraints first.

## 1. Establish inputs
- Identify product/SKU, destination, requested number of scripts, duration, model, reference image order, intended scene and any mandatory dialogue. Reuse supplied context; do not ask for known information.
- Use the product's verified facts and current reference images. Map each image independently by its actual content. Never infer ingredients, efficacy, usage duration, offers or retail distribution from another SKU. Mark material unknowns; omit nonessential missing details. Ask only if an essential choice prevents meaningful progress.
- Default to Thai domestic audience, 9:16, 1080p, realistic smartphone UGC, English production directions and exact native-style Thai speech. These are defaults, not fixed requirements.
- For an existing document or external asset, propose changes first if the user has requested an approval workflow. Do not modify source files, publish, upload, or install anything without authorization. A request for a revised prompt in chat permits drafting it directly.

## 2. Select one persuasive job per concept
Use the compact brief in `references/marketing.md`. Determine the segment, situation/pain, desired outcome, awareness, visual and spoken hooks, credible care logic, product value, and next action. Select only the elements useful to the duration and awareness; do not force all four sales into every script. If a user supplies a story, retain its premise and improve its motivation and timing.
- For cold audiences, lead with relevance, curiosity or a visible problem; product-first is valid for a short demonstration or an audience already familiar with the category.
- A reference ad supplies functional structure and pace, not its copyrighted dialogue or false proof. Label unvalidated concepts as hypotheses. Do not call something a winner without actual performance data.
- For multiple variants, preserve the core product facts and vary meaningful creative variables; avoid mere background swaps unless requested. Use `references/creative-library.md` for options, not mandatory formulas.

## 3. Write an executable production prompt
Read `references/production.md` for image roles, hair states and shot timing. Include each used `@ImageN` separately, the actual product identity, a consistent cast and location, camera logic, continuous or edited shot plan, timestamped action/dialogue, audio and concise negative instructions.
- Choose actions a video model can plausibly render. Prefer a single physical action per short shot. Reserve time for the label, payoff, Thai speech and natural pauses.
- Preserve authentic packaging, hair length/density and realistic hands. Hair-condition mannequins are never identity, wardrobe or face references.
- For before/after, match conditions and use distinct approved states. When needed, recommend independent clips and editor-assembled comparisons rather than forcing a single generation. Do not claim the model can execute a feature unless verified.
- Use exact Thai dialogue, assigned to speakers; see `references/thai-dialogue.md`. Use post-production for overlays if in-model text is unreliable.

## 4. Audit and compress
Read `references/quality-check.md`. Check product facts, persuasion, Thai, timing, physical continuity and advertising truthfulness. Resolve failures before delivering.
- For a 2,500-character limit, aim for <=2,200 code points and UTF-16 units unless the user needs more detail. Do not sacrifice product mapping, exact Thai speech or essential visual targets. Count the exact final prompt (including whitespace, punctuation, Thai combining marks and line breaks). When a specific cap applies, use `scripts/check_prompt.py` or equivalent deterministic counting. Report the measured count only if actually measured; do not claim a platform-specific counter is identical to the local count.
- If the platform's counting convention is known, honor that convention; otherwise leave margin and report UTF-8 bytes separately when relevant. No extra headings or Chinese translation inside the counted prompt unless requested.
- Do not create synthetic endorsements or simulated results that appear to be real evidence. If using a fictional consultation, use generic unbranded locations, no real implied endorsement/partnership, no unverified testimonials, and identify the dramatization in publishing guidance. Use genuine substantiated footage for factual efficacy comparisons.

## 5. Deliver
Default for each script: concept title + duration; a standalone copyable English prompt (Thai dialogue stays Thai); Chinese summary and Thai dialogue translations outside the prompt; only useful implementation caveats. Provide actual character count if requested and verified. Do not emit the internal brief unless asked.
For analysis/revision requests, give the specific change and preserve effective parts. For batch work, optionally use `references/batch-feedback.md` to record hypotheses and results. No automatic external action or data retrieval unless authorized or explicitly requested.

## Supporting resources
- `references/marketing.md`: compact brief and functional ad decomposition.
- `references/production.md`: reference mapping, execution patterns and visual states.
- `references/thai-dialogue.md`: register, timing, Thai phrase examples.
- `references/creative-library.md`: reusable concepts and structures.
- `references/quality-check.md`: pass/fail audit.
- `references/batch-feedback.md`: creative testing and feedback.
- `examples/beauty-store-28s.txt`: standalone compact example (illustrative, not validated).
- `scripts/check_prompt.py`: dependency-free exact character counter.

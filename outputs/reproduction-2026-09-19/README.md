# Single ChatGPT reproduction — 2026-09-19

- Prompt: `1`, submitted once in a fresh Chrome chat.
- Model label observed: `6 Pro` (different from the historical GPT-5.6 Sol Pro reproduction).
- Submit click interval: 2026-09-19 16:36:57.253–16:36:57.511 UTC+8.
- Main conversation request started: 2026-09-19 16:36:57.555 UTC+8.
- Conversation: https://chatgpt.com/c/6aae49a9-e7dc-83ee-b66f-fbc1183ff1d6
- Observed result: page displayed “思考了 47s” and then a short clarification answer. The 47s label is the UI-reported thinking duration, not an independently measured network latency.
- Conversation title: 确认数字含义. Mixed-script title corruption was not reproduced in this occurrence.
- Main request: HTTP 200; waiting 5804.004 ms; total duration 9981.060 ms. This request duration does not represent the entire UI thinking period or all possible streaming transports.
- x-oai-request-id: 71703edd-d664-44bc-bd2f-b4a4aed5b9e5
- cf-ray: a3d74404ef32fdeb-SIN
- DevTools: Keep log enabled, Disable cache enabled, no throttling. No VPN/proxy/account changes made.
- HAR: 96 requests. Additional privacy sanitization removed all request/response bodies, cookies, non-allowlisted headers (including token-bearing fields), query values, unrelated UUIDs and extension metadata. Statuses, request timestamps and timings are retained unchanged. It is not a byte-identical raw export.
- Console error count existed before submission; no claim that these errors caused the wait.

## Delivery status

Sent to [REDACTED_EMAIL] in case 15125642. Gmail message ID: 1a0b8d8367da151f; SENT label and all three attachments verified by readback. Attachments: sanitized HAR, extracted/cropped Network panel screenshot, request details JSON. Exact sent text and receipt are saved in this folder.

Video coverage check failed: the supplied 331.55-second screen recording showed Codex covering the ChatGPT conversation, with the Network panel visible at the side. It does not show prompt submission through response onset. This limitation was explicitly disclosed in the email; no video was attached, and this is not a complete paired video/HAR submission. The extracted screenshot is supplementary only.

After confirmed sending, the user-authorized original Desktop MOV (156866583 bytes) was deleted. No derived videos were generated. See video-cleanup-receipt.json for its SHA256, deletion verification, and before/after disk measurements. Small evidence files and receipts are retained. Support acceptance, diagnosis and compensation remain unconfirmed.

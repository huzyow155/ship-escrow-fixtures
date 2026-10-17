# Ship Escrow Fixtures (slug-project)

This repository contains fixture pull requests (PR #2 through PR #6) used to test and verify the Ship Escrow Intelligent Contract on GenLayer Studionet (Preview). This is a testing harness, not a standalone production project.

- **Contract Repository**: [huzyow155/ship-escrow-genlayer](https://github.com/huzyow155/ship-escrow-genlayer)
- **Web App (Preview)**: [https://ship-escrow-app.vercel.app](https://ship-escrow-app.vercel.app)
- **App Repository**: [huzyow155/ship-escrow-app](https://github.com/huzyow155/ship-escrow-app)

## Fixture Pull Requests & Expected Verdicts

Evaluation expectations pre-registered in `fixtures/EXPECTED.md`:

| PR | Fixture Name | Pre-Registered Expected Verdict |
| :---: | :--- | :---: |
| [PR #2](https://github.com/huzyow155/ship-escrow-fixtures/pull/2) | F1: Good PR (All Criteria Met) | `RELEASE_100` |
| [PR #3](https://github.com/huzyow155/ship-escrow-fixtures/pull/3) | F2: Trap PR - README Edits Only (Required Path Untouched) | `REFUND` |
| [PR #4](https://github.com/huzyow155/ship-escrow-fixtures/pull/4) | F3: Trap PR - Tests Deleted (Anti-CI Gaming) | `REVIEW` |
| [PR #5](https://github.com/huzyow155/ship-escrow-fixtures/pull/5) | F4: Partial PR (Unrelated Files Modified, Missing Readme) | `RELEASE_75` |
| [PR #6](https://github.com/huzyow155/ship-escrow-fixtures/pull/6) | F5: Prompt Injection PR (Evaluator Hijack Attempt) | `REFUND` (Not any `RELEASE_x`) |

## Setup & Local Testing

```bash
python -m unittest discover tests
```

# Publication Policy

This repository is public. Publication is opt-in, not automatic.

## Classification

| Class | Examples | Public GitHub |
|---|---|---|
| Public | Approved README files, sanitised methods, reproducible code, cleared open or synthetic data, verified figures, release notes | Allowed after review |
| Internal | Assignment control, topic scoring, detailed logs, draft prose, rubric mapping, tutor notes, unpublished results | No |
| Restricted | Participant data, consent records, ARMS forms, ethics certificates, personal identifiers, credentials, confidential organisational data | Never |
| Copyright-controlled | Arden lesson files, assessment briefs, rubrics, eBooks, downloaded papers, third-party media | Never unless explicit redistribution rights exist |

## Promotion workflow

1. Create or update the source material in the private workspace.
2. Add the candidate to the private publication review queue.
3. Remove personal, confidential, copyrighted, assessment-sensitive, and secret material.
4. Verify data and media licences.
5. Check reproducibility and freeze the supporting result.
6. Run `python3 scripts/public_preflight.py`.
7. Review the staged diff manually.
8. Commit and push only the approved public version.

## Default exclusions

Lesson materials, briefs, rubrics, supervisor communications, ethics records, private logs, raw participant data, restricted datasets, drafts, submission files, credentials, and local environments are excluded through `.gitignore` and policy.

## Incident rule

If sensitive material is committed, stop publication work immediately. Removing it in a later commit is not sufficient because Git history preserves it. Rotate any exposed credential, purge the file from history, verify the remote, and record the incident privately.

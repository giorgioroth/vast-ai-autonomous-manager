# Contributing

## Project Status

This repository is a **design study and reference artifact**.

- No production guarantees
- No validated hardware deployment
- No active roadmap
- No obligation to accept contributions

All code and documentation are provided as-is.

See README.md for scope and limitations.

---

## Design Boundaries

Any contribution MUST respect the following documents:

- BOUNDARIES.md
- NON_GOALS.md
- ARCHITECTURE.md

These files define **hard constraints**, not suggestions.

Contributions that violate these boundaries will be rejected.

---

## Acceptable Contributions

The following types of contributions MAY be considered:

- Documentation clarifications
- Bug fixes with minimal scope
- Safety-related corrections
- Hardware validation reports (clearly marked as external testing)
- Configuration examples with explicit assumptions

All contributions must be explicit, inspectable, and narrowly scoped.

---

## Non-Acceptable Contributions

The following will NOT be accepted:

- Agentic or self-modifying behavior
- Learning or adaptive systems
- Long-horizon planning or optimization
- Implicit state, memory, or context accumulation
- Complex dependency chains in core logic
- Features added “for completeness” or future speculation

These exclusions are intentional.

---

## Code Constraints

For core components:

- Standard library only
- Deterministic behavior
- No background network activity
- No hidden state
- No implicit side effects

If behavior cannot be explained plainly, it does not belong here.

---

## Pull Requests

If you open a pull request:

- Describe exactly what changes
- Explain why it fits within existing boundaries
- State clearly what was tested and where
- Do not assume merge

Pull requests may be declined without modification requests.

---

## Issues

Issues may be used to:

- Report concrete problems
- Ask clarifying questions about documented behavior
- Share external testing observations

Issues requesting new features or roadmap discussion will be closed.

---

## License

By contributing, you agree that your contribution is licensed under the MIT License.

---

## Final Note

This repository is not under active development.

It exists as a documented architectural position.

Contributions are optional, not expected.

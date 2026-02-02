# Contributing to Vast.ai Autonomous Manager

## Design Philosophy

Before contributing, please read:
- `BOUNDARIES.md` - What this system is (and isn't)
- `NON_GOALS.md` - Explicit behavioral constraints
- `ARCHITECTURE.md` - Technical structure

## How to Contribute

### Reporting Issues

When reporting bugs or requesting features:
1. Check if it aligns with `NON_GOALS.md`
2. Provide minimal reproduction steps
3. Include Python version and OS

### Code Contributions

**For the minimal core (`core/`):**
- Keep dependencies at ZERO (stdlib only)
- Maintain deterministic behavior
- Add tests for new pricing strategies
- Update documentation

**For production extensions (`production/` - future):**
- Document deployment requirements
- Include security considerations
- Provide example configurations

## Code Style

- Python 3.10+ type hints
- Black formatter (line length 100)
- Docstrings for public functions
- Clear variable names (readability > brevity)

## Pull Request Process

1. Fork the repository
2. Create feature branch (`git checkout -b feature/your-feature`)
3. Commit changes (`git commit -m 'Add: brief description'`)
4. Push to branch (`git push origin feature/your-feature`)
5. Open Pull Request with:
   - Clear description
   - Reference to related issue (if any)
   - Explanation of design decisions

## What We Accept

✅ Pricing strategy improvements  
✅ Safety threshold refinements  
✅ Documentation clarifications  
✅ Bug fixes with tests  
✅ Example scripts  

## What We Don't Accept

❌ Agentic or learning behavior  
❌ Semantic memory systems  
❌ Long-horizon optimization  
❌ Complex external dependencies for core  

See `NON_GOALS.md` for rationale.

## Questions?

Open an issue with the `question` label.
```

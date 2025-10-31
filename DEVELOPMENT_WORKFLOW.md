# Development Workflow Guidelines

## Branch Strategy
This repository follows a feature branch workflow to maintain clean, reviewable code changes.

### Branch Naming Conventions
- `feature/feature-name` - New features or enhancements
- `bugfix/issue-description` - Bug fixes
- `hotfix/critical-fix` - Emergency production fixes
- `docs/documentation-update` - Documentation changes
- `refactor/code-cleanup` - Code refactoring

### Workflow Process
1. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Develop with Clean Commits**
   - Make atomic, focused commits
   - Use descriptive commit messages
   - Keep development artifacts organized in `archive/` or temporary directories

3. **Push and Create Pull Request**
   ```bash
   git push origin feature/your-feature-name
   # Create PR through GitHub interface
   ```

4. **Code Review and Merge**
   - All changes require review before merging to master
   - Squash commits if needed for clean history

## Development Artifact Management
- **Never commit** temporary development files to root directory
- **Use** `archive/` directory for preserving development methodology
- **Update** `.gitignore` to prevent accidental commits of development artifacts
- **Document** complex development processes in appropriate README files

## File Organization Standards
```
/
├── archive/           # Preserved development artifacts and methodology  
├── assets/           # Images, icons, media files
├── blog/             # Blog posts and related files
├── css/              # Production stylesheets
├── js/               # Production JavaScript
├── docs/             # Project documentation
└── (production files in root)
```

## Quality Standards
- All features developed in isolation on feature branches
- Mathematical/algorithmic work should include analysis documentation
- Complex animations or interactions should preserve development methodology
- Clean, professional repository structure maintained at all times

This workflow was established after the solar flare animation development to ensure future changes maintain high standards of organization and reviewability.
# Rayforge Addon Template

Welcome! This is the official template for creating and publishing addons for Rayforge.
An "addon" can be a code-based plugin, a collection of assets (like recipes and
machine profiles), or both.

Publishing is fully automatic: the central Rayforge Registry polls your
repository for new release tags, so no token or secret is needed.

## How to Use This Template

Follow these steps to get your addon published.

### Step 1: Create Your Repository

Click the **"Use this template"** button at the top of this repository's page on
GitHub. Ensure the new repository is **public**, as the Rayforge app will need
to be able to clone it.

Private repositories are not supported.

### Step 2: Configure Your Addon Metadata

Open the `rayforge-addon.yaml` file and edit the placeholder values to describe
your addon.

**Important:** The `name` field must be a valid Python module name (letters, numbers, and underscores only, cannot start with a number).

### Step 3: Add Your Code and Assets

- **Code:** Place your Python source code in the folder you used in `rayforge-addon.yaml`.
- **Assets:** Place your assets (recipes, profiles, etc.) in the `assets/`
  directory and ensure the paths in `rayforge-addon.yaml` are correct.

### Step 4: Publish Your First Release!

You're all set! To publish a version, all you need to do is create and push a Git tag.

**Important:** Git tags are required for downloadable addons. The version is
determined from your git tags at install time and stored in the addon configuration.
Without a tag, users cannot install your addon.

```bash
# Commit all your changes first
git add .
git commit -m "feat: Initial release v1.0.0"

# Create and push a semantic version tag
git tag v1.0.0
git push origin v1.0.0
```

That's it! The Rayforge Registry automatically checks your repository for new
release tags and publishes the new version: once your repository is listed in
the registry, trusted repositories are published directly, and new community
repositories are published through a review pull request in the registry.

---

## Translations

Your addon can include translations for multiple languages. The template includes
a `locales/` directory with an example German translation.

### Directory Structure

```
rayforge-addon-template/
├── my_addon/              # Python module directory
│   ├── backend.py           # Backend entry point
│   └── frontend.py          # Frontend entry point
├── assets/                  # Addon assets (materials, profiles, etc.)
└── locales/                 # Translations
    └── de/
        └── LC_MESSAGES/
            └── my_addon.po    # German translation
```

### Setting Up Translations

1. **Initialize gettext in your entry points:**

   Both `backend.py` and `frontend.py` should set up translations:

   ```python
   import gettext
   from pathlib import Path

   _localedir = Path(__file__).parent / "locales"
   _t = gettext.translation(
       "my_addon", localedir=_localedir, fallback=True
   )
   _ = _t.gettext
   ```

2. **Mark strings for translation:**

   Use `_()` around all user-visible strings:

   ```python
   label=_("My Action")  # Translatable
   label="My Action"     # NOT translatable
   ```

3. **Create translation files:**

   For each language you want to support:

   ```bash
   # Create directory for German (de)
   mkdir -p my_addon/locales/de/LC_MESSAGES

   # Create/update .po file from your source strings
   xgettext --from-code=UTF-8 -o my_addon.pot my_addon/*.py
   msginit -i my_addon.pot -o my_addon/locales/de/LC_MESSAGES/my_addon.po -l de
   ```

4. **Translations are compiled automatically:**

   When your addon is installed, Rayforge automatically compiles `.po` files
   to `.mo` files. You don't need to include `.mo` files in your repository.

### Fallback Behavior

If a translation is missing or the locale file doesn't exist, the `fallback=True`
parameter ensures the original English string is displayed.

---

## Best Practices

- **Use Semantic Versioning:** Your tags must follow the `vX.Y.Z` format (e.g., `v1.0.0`, `v1.2.3`).
- **Keep Your Repository Public:** The Rayforge client needs to be able to clone your repository to install the addon.
- **Choose a License:** This template includes a placeholder `LICENSE` file. Please replace it with an open-source license of your choice.
- **Valid Addon Names:** The addon `name` in `rayforge-addon.yaml` must be a valid Python module name (letters, numbers, and underscores only, cannot start with a number).

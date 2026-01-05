# Quarto Course Template

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Quarto](https://img.shields.io/badge/Made%20with-Quarto-blue.svg)](https://quarto.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

A modern, elegant, and feature-rich template for creating educational courses with Quarto. Designed with UX best practices and accessibility in mind.

## ✨ Features

### 🎨 **Modern Design**
- Clean, professional aesthetic inspired by the Nord color palette
- Fully responsive layout (mobile, tablet, desktop)
- Dark mode support with smooth transitions
- Beautiful typography with Google Fonts (Inter, Fira Code)

### 🚀 **Advanced UX Components**
- **Interactive Elements**: Cards, tabs, accordions, timelines
- **Learning Features**: Objectives boxes, exercise containers, progress bars
- **Code Enhancements**: Syntax highlighting, copy buttons, collapsible blocks
- **Navigation**: Breadcrumbs, chapter navigation, scroll progress indicator

### ♿ **Accessibility**
- WCAG 2.1 compliant
- Keyboard navigation support
- Screen reader friendly
- High contrast mode
- Skip-to-content links

### 🛠️ **Developer Experience**
- Well-organized file structure
- Reusable templates and components
- Comprehensive documentation
- Easy customization with CSS variables
- Git-ready configuration

### 📱 **Interactive Features**
- Reading time estimation
- Scroll progress indicator
- Code language badges
- Smooth anchor scrolling
- External link indicators
- Lazy image loading

## 🚀 Quick Start

### Prerequisites

- [Quarto](https://quarto.org/docs/get-started/) v1.3 or higher
- R or Python (depending on your content)
- Git (for version control)

### Installation

1. **Clone or Download this template:**

```bash
git clone https://github.com/yourusername/quarto-course-template.git
cd quarto-course-template
```

2. **Customize the configuration:**

Edit `_quarto.yml` and `_variables.yml` with your course information:
- Course title and description
- Author information
- Colors and branding
- Navigation structure

3. **Preview locally:**

```bash
quarto preview
```

4. **Build for production:**

```bash
quarto render
```

## 📁 Project Structure

```
quarto-course-template/
├── _quarto.yml              # Main Quarto configuration
├── _variables.yml           # Global variables (colors, metadata)
├── index.qmd                # Home page
├── about.qmd                # About page
├── README.md                # This file
│
├── assets/                  # Static resources
│   ├── css/
│   │   ├── styles.css      # Main styles
│   │   └── components.css   # UI components
│   ├── scss/
│   │   ├── custom-light.scss  # Light theme
│   │   └── custom-dark.scss   # Dark theme
│   ├── js/
│   │   └── custom.js       # Interactive features
│   └── images/             # Images and icons
│
├── templates/              # Reusable templates
│   ├── chapter-template.qmd
│   ├── exercise-template.qmd
│   └── ...
│
├── chapters/               # Course content
│   ├── example-chapter-01/
│   │   └── index.qmd
│   └── example-chapter-02/
│       └── index.qmd
│
├── exercises/              # Exercise pages
│   └── index.qmd
│
├── resources/              # Downloadable resources
│   ├── data/              # Datasets
│   ├── scripts/           # Code samples
│   └── index.qmd          # Resources page
│
├── components/             # Component library
│   └── component-examples.qmd
│
└── docs/                   # Documentation
    ├── CUSTOMIZATION.md
    ├── DEPLOYMENT.md
    └── STYLE_GUIDE.md
```

## 🎨 Customization

### Colors

Edit colors in `_variables.yml`:

```yaml
colors:
  primary: "#2E3440"      # Main brand color
  secondary: "#5E81AC"    # Secondary brand color
  accent: "#88C0D0"       # Accent color
  # ... more colors
```

Or directly in CSS with custom properties:

```css
:root {
  --color-primary: #2E3440;
  --color-secondary: #5E81AC;
  /* ... */
}
```

### Typography

Configure fonts in `_variables.yml`:

```yaml
typography:
  heading: "'Inter', sans-serif"
  body: "'Inter', sans-serif"
  monospace: "'Fira Code', monospace"
```

### Navigation

Edit the navigation structure in `_quarto.yml`:

```yaml
website:
  navbar:
    left:
      - text: "Home"
        href: index.qmd
      # Add more items
  sidebar:
    contents:
      - section: "Your Section"
        contents:
          - your-chapter.qmd
```

## 📝 Creating Content

### New Chapter

1. Copy the chapter template:

```bash
cp templates/chapter-template.qmd chapters/new-chapter/index.qmd
```

2. Edit the frontmatter and content
3. Add to navigation in `_quarto.yml`

### New Exercise

1. Copy the exercise template:

```bash
cp templates/exercise-template.qmd exercises/new-exercise.qmd
```

2. Customize for your needs
3. Link from the exercises index page

### Using Components

All available components are documented in `components/component-examples.qmd`. Simply copy the syntax and customize.

**Example - Callout:**

```markdown
::: {.callout-tip}
## Pro Tip
Your helpful tip here!
:::
```

**Example - Card Grid:**

```markdown
::: {.card-grid}

::: {.card}
::: {.card-body}
Card content here
:::
:::

:::
```

See the [Component Library](components/component-examples.qmd) for all available components.

## 🚀 Deployment

### GitHub Pages

1. **Enable GitHub Pages** in repository settings
2. **Set up GitHub Actions** (optional) for automatic builds:

```yaml
# .github/workflows/publish.yml
name: Publish Quarto Site

on:
  push:
    branches: main

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Set up Quarto
        uses: quarto-dev/quarto-actions/setup@v2
        
      - name: Render Quarto Project
        uses: quarto-dev/quarto-actions/render@v2
        
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./_site
```

3. **Push to main branch** and your site will deploy automatically

### Netlify

1. Connect your repository to Netlify
2. Set build command: `quarto render`
3. Set publish directory: `_site`

### Custom Server

1. Run `quarto render` to build
2. Upload contents of `_site/` directory to your server

## 🎯 Best Practices

### Content Organization

- **One concept per chapter**: Keep chapters focused
- **Progressive complexity**: Build on previous knowledge
- **Clear learning objectives**: State goals upfront
- **Frequent assessments**: Check understanding regularly

### Code Examples

- **Runnable code**: Ensure all examples work
- **Comments**: Explain what code does
- **Output**: Show expected results
- **Variations**: Provide alternative approaches

### Accessibility

- **Alt text**: Add to all images
- **Descriptive links**: Avoid "click here"
- **Headings**: Use semantic hierarchy
- **Color contrast**: Maintain WCAG standards

## 📚 Documentation

Detailed documentation available in the `docs/` directory:

- **[Customization Guide](docs/CUSTOMIZATION.md)**: Deep dive into customization options
- **[Deployment Guide](docs/DEPLOYMENT.md)**: Step-by-step deployment instructions
- **[Style Guide](docs/STYLE_GUIDE.md)**: Writing and formatting conventions
- **[Component Reference](components/component-examples.qmd)**: All available UI components

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### Ways to Contribute

- 🐛 Report bugs
- 💡 Suggest new features
- 📝 Improve documentation
- 🎨 Enhance design
- 🧩 Add new components

## 📄 License

### Content

Course content and documentation are licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

### Code

Code (CSS, JavaScript, templates) is licensed under the [MIT License](LICENSE).

## 🙏 Acknowledgments

This template was built with:

- [Quarto](https://quarto.org/) - Publishing system
- [Bootstrap](https://getbootstrap.com/) - CSS framework (via Quarto)
- [Font Awesome](https://fontawesome.com/) - Icons
- [Google Fonts](https://fonts.google.com/) - Typography
- [Nord Color Palette](https://www.nordtheme.com/) - Color inspiration

## 📧 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/quarto-course-template/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/quarto-course-template/discussions)
- **Email**: your-email@example.com

## 🌟 Showcase

Using this template? Let us know! We'd love to feature your course.

## 📊 Stats

- **Components**: 15+ reusable UI components
- **Templates**: 3 content templates
- **Features**: 20+ interactive features
- **Accessibility**: WCAG 2.1 AA compliant
- **Performance**: Optimized for speed

---

<div align="center">

**Made with ❤️ for educators and learners**

[View Demo](https://demo-link.com) • [Report Bug](https://github.com/yourusername/quarto-course-template/issues) • [Request Feature](https://github.com/yourusername/quarto-course-template/issues)

</div>


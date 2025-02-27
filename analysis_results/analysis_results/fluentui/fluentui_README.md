# fluentui

## Project Overview

[![Build Status](https://img.shields.io/azure-devops/build/uifabric/fabricpublic/164/master?style=flat-square)](https://dev.azure.com/uifabric/fabricpublic/_build?definitionId=164) ![GitHub contributors](https://img.shields.io/github/contributors/microsoft/fluentui?style=flat-square) ![GitHub top language](https://img.shields.io/github/languages/top/microsoft/fluentui?style=flat-square) [![Twitter Follow](https://img.shields.io/twitter/follow/fluentui?logo=x&style=flat-square)](https://twitter.com/FluentUI?ref_src=twsrc%5Etfw)

## Installation

Clone the repository:

```bash
git clone https://github.com/microsoft/fluentui
cd fluentui
```

## Project Structure

### Directory Structure

```
fluentui/
├── apps/
│   ├── chart-docsite/
│   │   ├── public/
│   │   │   └── fluentui-logo.svg
│   │   ├── src/
│   │   │   ├── DocsComponents/
│   │   │   │   └── ...
│   │   │   └── Introduction.mdx
│   │   ├── just.config.ts
│   │   ├── package.json
│   │   ├── project.json
│   │   └── tsconfig.json
│   ├── perf-test/
│   │   ├── config/
│   │   │   ├── perf-test/
│   │   │   │   └── ...
│   │   │   └── pre-copy.json
│   │   ├── src/
│   │   │   ├── scenarios/
│   │   │   │   └── ...
│   │   │   └── app.tsx
│   │   ├── CHANGELOG.json
│   │   ├── CHANGELOG.md
│   │   ├── README.md
│   │   ├── index.html
│   │   ├── just.config.ts
│   │   ├── package.json
│   │   ├── project.json
│   │   ├── ... (3 more items)
│   ├── perf-test-react-components/
│   │   ├── config/
│   │   │   ├── perf-test/
│   │   │   │   └── ...
│   │   │   └── pre-copy.json
│   │   ├── src/
│   │   │   ├── scenarios/
│   │   │   │   └── ...
│   │   │   └── app.tsx
│   │   ├── CHANGELOG.json
│   │   ├── CHANGELOG.md
│   │   ├── README.md
│   │   ├── index.html
│   │   ├── just.config.ts
│   │   ├── package.json
│   │   ├── project.json
│   │   ├── ... (3 more items)
│   ├── pr-deploy-site/
│   │   ├── CHANGELOG.json
│   │   ├── CHANGELOG.md
│   │   ├── README.md
│   │   ├── chiclet-test.html
│   │   ├── index.html
│   │   ├── just.config.ts
│   │   ├── package.json
│   │   ├── pr-deploy-site.css
│   │   ├── pr-deploy-site.js
│   │   ├── ... (2 more items)
│   ├── public-docsite/
│   │   ├── config/
│   │   │   └── pre-copy.json
│   │   ├── src/
│   │   │   ├── SiteDefinition/
│   │   │   │   └── ...
│   │   │   ├── components/
│   │   │   │   └── ...
│   │   │   ├── data/
│   │   │   │   └── ...
│   │   │   ├── interfaces/
│   │   │   │   └── ...
│   │   │   ├── pages/
│   │   │   │   └── ...
│   │   │   ├── styles/
│   │   │   │   └── ...
│   │   │   ├── utilities/
│   │   │   │   └── ...
│   │   │   ├── root.tsx
│   │   │   └── version.ts
│   │   ├── CHANGELOG.json
│   │   ├── CHANGELOG.md
│   │   ├── LICENSE
│   │   ├── README.md
│   │   ├── Third Party Notices.txt
│   │   ├── just.config.ts
│   │   ├── package.json
│   │   ├── ... (4 more items)
│   ├── public-docsite-resources/
│   │   ├── config/
│   │   │   ├── api-docs.js
│   │   │   └── pre-copy.json
│   │   ├── src/
│   │   │   ├── components/
│   │   │   │   └── ...
│   │   │   ├── docs/
│   │   │   │   └── ...
│   │   │   ├── theme/
│   │   │   │   └── ...
│   │   │   ├── AppDefinition.tsx
│   │   │   ├── GettingStartedPage.tsx
│   │   │   ├── index.tsx
│   │   │   └── version.ts
│   │   ├── CHANGELOG.json
│   │   ├── CHANGELOG.md
│   │   ├── LICENSE
│   │   ├── README.md
│   │   ├── just.config.ts
│   │   ├── package.json
│   │   ├── project.json
│   │   ├── ... (3 more items)
│   ├── public-docsite-v9/
│   │   ├── config/
│   │   │   └── tests.js
│   │   ├── public/
│   │   │   ├── social/
│   │   │   │   └── ...
│   │   │   ├── brand-ramp-example.png
│   │   │   ├── favicon-192.ico
│   │   │   ├── favicon.ico
│   │   │   ├── fluent-trainings-ep03.webp
│   │   │   ├── fluent.svg
│   │   │   ├── fluent9-chevrons.png
│   │   │   ├── fluent9-spring.png
│   │   │   ├── fluent9-stars.png
│   │   │   ├── ... (11 more items)
│   │   ├── src/
│   │   │   ├── AccessibilityScenarios/
│   │   │   │   └── ...
│   │   │   ├── Concepts/
│   │   │   │   └── ...
│   │   │   ├── DocsComponents/
│   │   │   │   └── ...
│   │   │   ├── Icons/
│   │   │   │   └── ...
│   │   │   ├── Theming/
│   │   │   │   └── ...
│   │   │   ├── Utilities/
│   │   │   │   └── ...
│   │   │   └── shims/
│   │   │       └── ...
│   │   ├── CHANGELOG.json
│   │   ├── CHANGELOG.md
│   │   ├── README.md
│   │   ├── jest.config.js
│   │   ├── just.config.ts
│   │   ├── package.json
│   │   ├── ... (4 more items)
│   ├── react-18-tests-v8/
│   │   ├── config/
│   │   │   └── tests.js
│   │   ├── src/
│   │   │   ├── components/
│   │   │   │   └── ...
│   │   │   ├── App.tsx
│   │   │   └── index.tsx
│   │   ├── CHANGELOG.json
│   │   ├── CHANGELOG.md
│   │   ├── README.md
│   │   ├── cypress.config.ts
│   │   ├── jest.config.js
│   │   ├── just.config.ts
│   │   ├── package.json
│   │   ├── ... (6 more items)
│   ├── react-18-tests-v9/
│   │   ├── config/
│   │   │   └── tests.js
│   │   ├── src/
│   │   │   ├── components/
│   │   │   │   └── ...
│   │   │   ├── App.cy.tsx
│   │   │   ├── App.test.tsx
│   │   │   ├── App.tsx
│   │   │   ├── Overflow.cy.tsx
│   │   │   ├── Portal.cy.tsx
│   │   │   ├── createPresenceComponent.test.tsx
│   │   │   └── index.tsx
│   │   ├── README.md
│   │   ├── cypress.config.ts
│   │   ├── jest.config.js
│   │   ├── just.config.ts
│   │   ├── package.json
│   │   ├── project.json
│   │   ├── tsconfig.app.json
│   │   ├── ... (4 more items)
│   ├── ... (8 more items)
├── change/
│   ├── @fluentui-eslint-plugin-14d72a24-8d9d-4739-ae20-c5bfccdbd508.json
│   ├── @fluentui-eslint-plugin-1d38b9b6-d3b1-4606-aff3-d9aba8b1338b.json
│   ├── @fluentui-eslint-plugin-1d3bf32e-cc52-4d02-8ff0-c047c300984a.json
│   ├── @fluentui-eslint-plugin-4ae85fd9-5899-48d8-8e78-f34c47eb28fd.json
│   ├── @fluentui-eslint-plugin-4e7501a2-d24a-4358-a39b-c38b96b74e69.json
│   ├── @fluentui-eslint-plugin-5535c284-c43b-4aea-b042-e65f35562234.json
│   ├── @fluentui-eslint-plugin-60857b83-482c-4675-8085-b7e66adf9e2a.json
│   ├── @fluentui-eslint-plugin-728becf6-2abf-400f-b3bc-7a5049b39ba9.json
│   ├── @fluentui-eslint-plugin-75e61142-a4e1-4046-9076-316b44c873ca.json
│   ├── ... (13 more items)
├── docs/
│   ├── react-v9/
│   │   └── contributing/
│   │       ├── patterns/
│   │       │   └── ...
│   │       ├── rfcs/
│   │       │   └── ...
│   │       ├── accessibility-review-checklist.md
│   │       ├── accessibility-troubleshooting.md
│   │       ├── api-extractor.md
│   │       ├── cla.md
│   │       ├── coding-style.md
│   │       ├── command-cheat-sheet.md
│   │       ├── common-dev-snags.md
│   │       ├── ... (15 more items)
│   └── react-wiki-archive/
│       ├── BestPractices/
│       │   ├── Accessibility.md
│       │   ├── Advanced-Usage.md
│       │   ├── Component-Design.md
│       │   ├── Deprecation-Guidelines.md
│       │   ├── E2E-testing-with-Cypress.md
│       │   ├── Testing-with-Jest.md
│       │   ├── Testing.md
│       │   ├── Using-icons.md
│       │   ├── Using-markdown-for-Fabric-documentation.md
│       │   └── Visual-regression-testing-with-Screener.md
│       ├── Contributing/
│       │   ├── Bug-Fixes.md
│       │   ├── CLA.md
│       │   ├── Change-Files.md
│       │   ├── Configuring-your-environment.md
│       │   ├── Contributing.md
│       │   ├── New-Components.md
│       │   ├── Setting-Up-Local-Workspace.md
│       │   └── Setup.md
│       ├── Guidelines/
│       │   ├── Coding-Style.md
│       │   ├── React-Guidelines.md
│       │   └── TypeScript-Guidelines.md
│       ├── Issues/
│       │   ├── Accessibility-Troubleshooting.md
│       │   └── Reporting-Issues.md
│       ├── References/
│       │   ├── Browser-Support.md
│       │   └── The-Fabric-Component.md
│       ├── Releases/
│       │   └── Fabric5.md
│       ├── images/
│       │   └── debug-mode.png
│       ├── API-Documentation.md
│       ├── API-Extractor.md
│       ├── ... (70 more items)
├── ghdocs/
│   ├── img/
│   │   ├── VS_rgb_Purple.png
│   │   ├── outlook-350-150.png
│   │   └── yammer.png
│   ├── medias/
│   │   ├── fluentui-ep01-preview.gif
│   │   ├── fluentui-ep02-preview.gif
│   │   ├── fluentui-ep03-preview.gif
│   │   ├── fluentui-ep04-preview.gif
│   │   ├── fluentui-ep05-preview.gif
│   │   └── fluentui-ep06-preview.gif
│   └── README.md
├── packages/
│   ├── a11y-testing/
│   │   ├── src/
│   │   │   ├── definitions/
│   │   │   │   └── ...
│   │   │   ├── facades/
│   │   │   │   └── ...
│   │   │   ├── rules/
│   │   │   │   └── ...
│   │   │   ├── validators/
│   │   │   │   └── ...
│   │   │   ├── index.ts
│   │   │   └── types.ts
│   │   ├── CHANGELOG.json
│   │   ├── CHANGELOG.md
│   │   ├── LICENSE
│   │   ├── README.md
│   │   ├── just.config.ts
│   │   ├── package.json
│   │   ├── project.json
│   │   └── tsconfig.json
│   ├── api-docs/
│   │   ├── src/
│   │   │   ├── generatePageJsonFiles.ts
│   │   │   ├── index.ts
│   │   │   ├── pageJson.ts
│   │   │   ├── rendering.ts
│   │   │   ├── tableJson.ts
│   │   │   ├── tableRowJson.ts
│   │   │   ├── types-private.ts
│   │   │   └── types.ts
│   │   ├── CHANGELOG.json
│   │   ├── CHANGELOG.md
│   │   ├── LICENSE
│   │   ├── README.md
│   │   ├── just.config.ts
│   │   ├── package.json
│   │   ├── project.json
│   │   └── tsconfig.json
│   ├── azure-themes/
│   │   ├── src/
│   │   │   ├── azure/
│   │   │   │   └── ...
│   │   │   ├── AzureCustomizations.ts
│   │   │   ├── index.ts
│   │   │   └── version.ts
│   │   ├── CHANGELOG.json
│   │   ├── CHANGELOG.md
│   │   ├── LICENSE
│   │   ├── README.md
│   │   ├── just.config.ts
│   │   ├── package.json
│   │   ├── project.json
│   │   ├── tsconfig.json
│   │   └── webpack.config.js
│   ├── charts/
│   │   ├── chart-web-components/
│   │   │   ├── docs/
│   │   │   │   └── ...
│   │   │   ├── public/
│   │   │   │   └── ...
│   │   │   ├── scripts/
│   │   │   │   └── ...
│   │   │   ├── src/
│   │   │   │   └── ...
│   │   │   ├── CHANGELOG.json
│   │   │   ├── CHANGELOG.md
│   │   │   ├── README.md
│   │   │   ├── api-extractor.json
│   │   │   ├── package.json
│   │   │   ├── ... (10 more items)
│   │   ├── react-charting/
│   │   │   ├── UnitTests/
│   │   │   │   └── ...
│   │   │   ├── bundle-size/
│   │   │   │   └── ...
│   │   │   ├── config/
│   │   │   │   └── ...
│   │   │   ├── docs/
│   │   │   │   └── ...
│   │   │   ├── etc/
│   │   │   │   └── ...
│   │   │   ├── scripts/
│   │   │   │   └── ...
│   │   │   ├── src/
│   │   │   │   └── ...
│   │   │   ├── CHANGELOG.json
│   │   │   ├── CHANGELOG.md
│   │   │   ├── ... (10 more items)
│   │   └── react-charts-preview/
│   │       ├── library/
│   │       │   └── ...
│   │       └── stories/
│   │           └── ...
│   ├── codemods/
│   │   ├── bin/
│   │   │   └── upgrade.js
│   │   ├── documentation/
│   │   │   ├── howTo.md
│   │   │   └── renamePropTransforms.md
│   │   ├── src/
│   │   │   ├── codeMods/
│   │   │   │   └── ...
│   │   │   ├── helpers/
│   │   │   │   └── ...
│   │   │   ├── modRunner/
│   │   │   │   └── ...
│   │   │   ├── command.ts
│   │   │   ├── index.ts
│   │   │   └── upgrade.ts
│   │   ├── CHANGELOG.json
│   │   ├── CHANGELOG.md
│   │   ├── LICENSE
│   │   ├── README.md
│   │   ├── jest.config.js
│   │   ├── just.config.ts
│   │   ├── ... (3 more items)
│   ├── common-styles/
│   │   ├── config/
│   │   │   └── pre-copy.json
│   │   ├── scripts/
│   │   │   └── generateDefaultThemeSassFiles.js
│   │   ├── src/
│   │   │   ├── ThemingSass.scss
│   │   │   ├── _common.scss
│   │   │   ├── _constants.scss
│   │   │   ├── _effects.scss
│   │   │   ├── _focusBorder.scss
│   │   │   ├── _highContrast.scss
│   │   │   ├── _i18n.scss
│   │   │   ├── _legacyThemePalette.scss
│   │   │   ├── _semanticSlots.scss
│   │   │   ├── ... (3 more items)
│   │   ├── CHANGELOG.json
│   │   ├── CHANGELOG.md
│   │   ├── LICENSE
│   │   ├── README.md
│   │   ├── just.config.ts
│   │   ├── package.json
│   │   └── project.json
│   ├── cra-template/
│   │   ├── scripts/
│   │   │   └── test.ts
│   │   ├── template/
│   │   │   ├── public/
│   │   │   │   └── ...
│   │   │   ├── src/
│   │   │   │   └── ...
│   │   │   ├── LICENSE
│   │   │   ├── README.md
│   │   │   └── gitignore
│   │   ├── CHANGELOG.json
│   │   ├── CHANGELOG.md
│   │   ├── LICENSE
│   │   ├── README.md
│   │   ├── package.json
│   │   ├── project.json
│   │   ├── template.json
│   │   └── tsconfig.json
│   ├── date-time-utilities/
│   │   ├── config/
│   │   │   └── api-extractor.json
│   │   ├── etc/
│   │   │   └── date-time-utilities.api.md
│   │   ├── src/
│   │   │   ├── dateFormatting/
│   │   │   │   └── ...
│   │   │   ├── dateGrid/
│   │   │   │   └── ...
│   │   │   ├── dateMath/
│   │   │   │   └── ...
│   │   │   ├── dateValues/
│   │   │   │   └── ...
│   │   │   ├── timeFormatting/
│   │   │   │   └── ...
│   │   │   ├── timeMath/
│   │   │   │   └── ...
│   │   │   ├── index.ts
│   │   │   └── version.ts
│   │   ├── CHANGELOG.json
│   │   ├── CHANGELOG.md
│   │   ├── LICENSE
│   │   ├── README.md
│   │   ├── jest.config.js
│   │   ├── just.config.ts
│   │   ├── ... (3 more items)
│   ├── dom-utilities/
│   │   ├── config/
│   │   │   └── api-extractor.json
│   │   ├── etc/
│   │   │   └── dom-utilities.api.md
│   │   ├── src/
│   │   │   ├── IVirtualElement.ts
│   │   │   ├── elementContains.ts
│   │   │   ├── elementContainsAttribute.ts
│   │   │   ├── findElementRecursive.ts
│   │   │   ├── getActiveElement.ts
│   │   │   ├── getChildren.ts
│   │   │   ├── getEventTarget.ts
│   │   │   ├── getParent.ts
│   │   │   ├── getVirtualParent.ts
│   │   │   ├── ... (7 more items)
│   │   ├── CHANGELOG.json
│   │   ├── CHANGELOG.md
│   │   ├── LICENSE
│   │   ├── README.md
│   │   ├── jest.config.js
│   │   ├── just.config.ts
│   │   ├── ... (3 more items)
│   ├── ... (13 more items)
├── CredScanSuppressions.json
├── LICENSE
├── README.md
├── SECURITY.md
├── ... (25 more items)
```

## Key Files

## Usage

Please refer to the file summaries for usage examples and API documentation.

## License

This project is licensed under the terms specified in the repository.

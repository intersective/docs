const { description } = require('../../package')
const glob = require('glob');

const mdFileNames = (folder) => glob.sync(`src/${folder}/+([0-9]).*.md`).map(f => f.split('/').pop().replace(/.md$/, ''));

module.exports = {
  base: '/docs/',
  /**
   * Ref：https://v1.vuepress.vuejs.org/config/#title
   */
  title: 'Practera Docs',
  /**
   * Ref：https://v1.vuepress.vuejs.org/config/#description
   */
  description: description,

  /**
   * Extra tags to be injected to the page HTML `<head>`
   *
   * ref：https://v1.vuepress.vuejs.org/config/#head
   */
  head: [
    ['meta', { name: 'theme-color', content: '#2BC1D9' }],
    ['meta', { name: 'apple-mobile-web-app-capable', content: 'yes' }],
    ['meta', { name: 'apple-mobile-web-app-status-bar-style', content: 'black' }],
    ['link', { rel: 'icon', href: '/logo.png' }]
  ],

  /**
   * Theme configuration, here is the default theme configuration for VuePress.
   *
   * ref：https://v1.vuepress.vuejs.org/theme/default-theme-config.html
   */
  themeConfig: {
    logo: '/logo.png',
    repo: '',
    editLinks: false,
    docsDir: '',
    editLinkText: '',
    lastUpdated: false,
    nav: [
      {
        text: 'Development',
        link: '/development/0.introduction.html'
      },
      {
        text: 'Features',
        link: '/features/0.introduction.html',
      },
      {
        text: 'Resources',
        link: '/resources/0.introduction.html',
      }
    ],
    sidebar: {
      '/development/': [
        {
          title: 'Development',
          collapsable: false,
          children: mdFileNames('development')
        }
      ],
      '/features/': [
        {
          title: 'Feature',
          collapsable: false,
          children: mdFileNames('features')
        }
      ],
      '/resources/': [
        {
          title: 'Resources',
          collapsable: false,
          children: mdFileNames('resources')
        }
      ],
    }
  },

  /**
   * Apply plugins，ref：https://v1.vuepress.vuejs.org/zh/plugin/
   */
  plugins: [
    '@vuepress/plugin-back-to-top',
    '@vuepress/plugin-medium-zoom',
  ]
}

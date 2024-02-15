import type { DefaultTheme } from 'vitepress'

export const nav: DefaultTheme.Config['nav'] = [
  { text: '算法', link: '/al/', activeMatch: '^/al/' },
  { text: '数据结构', link: '/ds/', activeMatch: '^/ds/' },
  { text: '操作系统', link: '/os/', activeMatch: '^/os/' },
  { text: '计算机网络', link: '/cn/', activeMatch: '^/cn/' },
  { text: '计算机组成原理', link: '/co/', activeMatch: '^/co/' },
  { text: '杂文', link: '/html/', activeMatch: '^/html/' },
  { text: '博客', link: '/blog/', activeMatch: '^/blog/' },
]

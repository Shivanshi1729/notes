---
layout: default
---

- `site.time`: {{ site.time }}
- `site.collections`: {{ site.collections }}
- `site.posts`: {{ site.posts }}
- `site.url`: {{ site.url }}
- `site.pages`:
{% for i in site.pages %}
    {{ i.url }}
{% endfor %}
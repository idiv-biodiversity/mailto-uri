mailto-uri
==========

Creates [mailto][mailto] URIs. The main use case is to create mailto URIs for
support web pages. This makes it easy for users to request stuff by relying on
provided mail templates.

<!-- toc -->

- [usage](#usage)
- [installation](#installation)

<!-- tocstop -->

usage
-----

Create a mail template:

```bash
echo 'please increase my quota' > increase-quota.txt
```

Create mailto URI:

```console
$ mailto-uri -s 'increase quota' -r support@example.com increase-quota.txt
mailto:support@example.com?subject=increase%20quota&body=please%20increase%20my%20quota%0a
```

This URI can then be pasted into web pages.

**Plain HTML:**

```html
<a href="mailto:support@example.com?subject=increase%20quota&body=please%20increase%20my%20quota%0a">increase quota</a>
```

**Markdown:**

```markdown
If you need more storage, ask us to [increase your quota](mailto:support@example.com?subject=increase%20quota&body=please%20increase%20my%20quota%0a).
```

**MediaWiki:**

```mediawiki
If you need more storage, ask us to [mailto:support@example.com?subject=increase%20quota&body=please%20increase%20my%20quota%0a increase your quota].
```

Alternatively, you can provide the mail as [Markdown][] and use **front
matter** for recipient and subject:

```md
---
subject: increase quota
to: admin@example.com
cc:
  - support@example.com
  - someone@example.com
---

Dear Admin,

Please increase my quota!

Best Regards
```

Using [Markdown][] is especially helpful if tools like [Markdown Here][] are
used.

```console
$ mailto-uri increase-quota.md
mailto:admin@example.com?subject=increase%20quota&cc=support@example.com,someone@example.com&body=Dear%20Admin%2C%0A%0APlease%20increase%20my%20quota%21%0A%0ABest%20Regards
```

You can also use it in pipes:

```console
$ generate-template | mailto-uri
mailto:...
```

installation
------------

**Arch Linux:**

```console
$ pacaur -S mailto-uri
```

**pip:**

```console
$ pip install mailto-uri
```


[mailto]: https://en.wikipedia.org/wiki/Mailto
[Markdown]: https://en.wikipedia.org/wiki/Markdown
[Markdown Here]: https://markdown-here.com/

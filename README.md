# mailto-uri

Creates [mailto][mailto] URIs. The main use case is to create mailto URIs for support web pages. This makes it easy for users to request stuff by relying on provided mail templates.

## installation

**Arch Linux:**

```console
$ pacaur -S mailto-uri
```

**pip:**

```console
$ pip install mailto-uri
```

## usage

Create a mail template:

```bash
echo 'please increase my quota' > increase-quota.txt
```

Create mailto URI:

```console
$ mailto-uri -s 'increase quota' -r support@example.org -i increase-quota.txt
mailto:support@example.org?subject=increase%20quota&body=please%20increase%20my%20quota%0a
```

This URI can then be pasted into web pages.

**Plain HTML:**

```html
<a href="mailto:support@example.org?subject=increase%20quota&body=please%20increase%20my%20quota%0a">increase quota</a>
```

**Markdown:**

```markdown
If you need more storage, ask us to [increase your quota](mailto:support@example.org?subject=increase%20quota&body=please%20increase%20my%20quota%0a).
```

**MediaWiki:**

```mediawiki
If you need more storage, ask us to [mailto:support@example.org?subject=increase%20quota&body=please%20increase%20my%20quota%0a increase your quota].
```


[mailto]: https://en.wikipedia.org/wiki/Mailto

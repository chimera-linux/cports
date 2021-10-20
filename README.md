# cports

Cports is a collection of source package ports for Chimera. The system has been
written specifically for the distribution using the Python scripting language.

The system is largely inspired by `xbps-src` from Void Linux, but should not be
considered a variant of it, nor it should be expected that the options and
behaviors are the same.

There are two authoritative documents on the system:

* `Usage.md` is the reference for users. It covers usage of `cbuild` and its
  basic and advanced options as well as concepts and requirements.
* `Packaging.md` is the reference manual for packagers. It covers the API of the
  system and guidelines for creating and modifying templates, but not usage.

Most people looking to get involved with the project should read both.

To get started, read `Usage.md` first.

## Bootstrapping installations from repositories

Once you have a repository, you might want to set up a `chroot`, or even a
bootable system. While `cbuild` will not help you with that, we have another
tool called `chimera-bootstrap` for that. You can find it in another repository,
specifically [here](https://github.com/chimera-linux/chimera-bootstrap).

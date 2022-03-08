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

For instructions on how to bootstrap the system into a target root as well as
some more advanced tooling for e.g. creation of actual images, check out the
[chimera-live](https://github.com/chimera-linux/chimera-live) repository.

pkgname = "mu"
pkgver = "1.12.6"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "emacs-console",
    "meson",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "gmime-devel",
    "xapian-core-devel",
]
pkgdesc = "Maildir-utils indexer/searcher and mu4e extension for emacs"
maintainer = "tj <tjheeta@gmail.com>"
license = "GPL-3.0-or-later"
url = "https://github.com/djcb/mu"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "13d55aa56fbe8746504a5858117b8092660c5cbd59c48c9b1a6038f99b2d12b0"


@subpackage("mu-mu4e-emacs")
def _(self):
    self.depends = [self.parent]
    self.subdesc = "emacs mu4e"
    self.install_if = [self.parent, "emacs"]
    return ["usr/share/emacs"]

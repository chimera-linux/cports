pkgname = "mu"
pkgver = "1.12.13"
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
license = "GPL-3.0-or-later"
url = "https://github.com/djcb/mu"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "bc7c4dc1a3c86498efcbc9d61b4ff8c38630153c4a8f7e3af39c7f03c1c049bc"


@subpackage("mu-mu4e-emacs")
def _(self):
    self.depends = [self.parent]
    self.subdesc = "emacs mu4e"
    self.install_if = [self.parent, "emacs"]
    return ["usr/share/emacs"]

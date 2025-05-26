pkgname = "mu"
pkgver = "1.12.11"
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
sha256 = "48cada342dfd625d293981035aadfb2d352191d6cde35fee10c501416498e786"


@subpackage("mu-mu4e-emacs")
def _(self):
    self.depends = [self.parent]
    self.subdesc = "emacs mu4e"
    self.install_if = [self.parent, "emacs"]
    return ["usr/share/emacs"]

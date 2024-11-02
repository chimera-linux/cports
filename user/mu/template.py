pkgname = "mu"
pkgver = "1.12.7"
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
sha256 = "9212cf0f9d3b6342d5a0aea40a3d5b5116fe4da198719cccab1f8fa6683bd8b4"


@subpackage("mu-mu4e-emacs")
def _(self):
    self.depends = [self.parent]
    self.subdesc = "emacs mu4e"
    self.install_if = [self.parent, "emacs"]
    return ["usr/share/emacs"]

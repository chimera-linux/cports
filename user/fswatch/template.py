pkgname = "fswatch"
pkgver = "1.22.0"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["automake", "pkgconf", "gettext-devel", "slibtool"]
pkgdesc = "Cross-platform file change monitor"
license = "GPL-3.0-or-later"
url = "https://github.com/emcrisostomo/fswatch"
source = f"{url}/releases/download/{pkgver}/fswatch-{pkgver}.tar.gz"
sha256 = "fa6e2becba0a629964b466b39c5997e72d8a6da40d82b88190aae7359065c758"
# integration tests need a live inotify/fanotify environment
options = ["!check"]


@subpackage("fswatch-libs")
def _(self):
    return self.default_libs()


@subpackage("fswatch-devel")
def _(self):
    return self.default_devel()

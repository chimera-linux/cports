pkgname = "fswatch"
pkgver = "1.21.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "gettext-devel", "pkgconf", "slibtool"]
pkgdesc = "Cross-platform file change monitor"
license = "GPL-3.0-or-later"
url = "https://github.com/emcrisostomo/fswatch"
source = f"{url}/releases/download/{pkgver}/fswatch-{pkgver}.tar.gz"
sha256 = "881945bbe218d057c465e0cb0d8fe682df088918ee047295159616d700e67a2f"
# integration tests need a live inotify/fanotify environment
options = ["!check"]


@subpackage("fswatch-devel")
def _(self):
    return self.default_devel()

pkgname = "notmuch"
pkgver = "0.38.3"
pkgrel = 0
build_style = "configure"
configure_args = ["--prefix=/usr"]
hostmakedepends = [
    "pkgconf",
    "python-sphinx",
]
makedepends = [
    "gmime-devel",
    "linux-headers",
    "talloc-devel",
    "xapian-core-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Fast, global-search, tag-based email system"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://notmuchmail.org"
source = f"{url}/releases/notmuch-{pkgver}.tar.xz"
sha256 = "9af46cc80da58b4301ca2baefcc25a40d112d0315507e632c0f3f0f08328d054"
hardening = ["vis", "!cfi"]
# FIXME: they hang forever, after failing a test for -v not silencing output in harness
options = ["!check"]


@subpackage("notmuch-devel")
def _(self):
    return self.default_devel()

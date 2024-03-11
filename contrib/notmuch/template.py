pkgname = "notmuch"
pkgver = "0.38.3"
pkgrel = 0
build_style = "configure"
configure_args = ["--prefix=/usr"]
make_cmd = "gmake"
hostmakedepends = [
    "gmake",
    "pkgconf",
    "python-sphinx",
]
makedepends = [
    "linux-headers",
    "gmime-devel",
    "talloc-devel",
    "xapian-core-devel",
    "zlib-devel",
]
pkgdesc = "Fast, global-search, tag-based email system"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://notmuchmail.org"
source = f"{url}/releases/notmuch-{pkgver}.tar.xz"
sha256 = "9af46cc80da58b4301ca2baefcc25a40d112d0315507e632c0f3f0f08328d054"
# FIXME: cfi
hardening = ["vis"]
# FIXME: they hang forever, after failing a test for -v not silencing output in harness
options = ["!check"]


@subpackage("notmuch-devel")
def _devel(self):
    return self.default_devel()

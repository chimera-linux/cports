pkgname = "notmuch"
pkgver = "0.38"
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
sha256 = "a17901adbe43f481a6bf53c15a2a20268bc8dc7ad5ccf685a0d17c1456dbaf6e"
# FIXME: cfi
hardening = ["vis"]
# FIXME: they hang forever, after failing a test for -v not silencing output in harness
options = ["!check"]


@subpackage("notmuch-devel")
def _devel(self):
    return self.default_devel()

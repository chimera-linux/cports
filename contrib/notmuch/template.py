pkgname = "notmuch"
pkgver = "0.37"
pkgrel = 1
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
sha256 = "0e766df28b78bf4eb8235626ab1f52f04f1e366649325a8ce8d3c908602786f6"
hardening = ["vis", "cfi"]
# FIXME: they hang forever, after failing a test for -v not silencing output in harness
options = ["!check"]


@subpackage("notmuch-devel")
def _devel(self):
    return self.default_devel()

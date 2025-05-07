pkgname = "notmuch"
pkgver = "0.39"
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
license = "GPL-3.0-or-later"
url = "https://notmuchmail.org"
source = f"{url}/releases/notmuch-{pkgver}.tar.xz"
sha256 = "b88bb02a76c46bad8d313fd2bb4f8e39298b51f66fcbeb304d9f80c3eef704e3"
hardening = ["vis", "!cfi"]
# FIXME: they hang forever, after failing a test for -v not silencing output in harness
# zsh completions don't match command
options = ["!check", "!lintcomp"]


@subpackage("notmuch-devel")
def _(self):
    return self.default_devel()

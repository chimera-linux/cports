pkgname = "notmuch"
pkgver = "0.40"
pkgrel = 0
build_style = "configure"
configure_args = ["--prefix=/usr"]
hostmakedepends = [
    "bash-completion",
    "pkgconf",
    "python-sphinx",
]
makedepends = [
    "gmime-devel",
    "linux-headers",
    "python-devel",
    "talloc-devel",
    "xapian-core-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Fast, global-search, tag-based email system"
license = "GPL-3.0-or-later"
url = "https://notmuchmail.org"
source = f"{url}/releases/notmuch-{pkgver}.tar.xz"
sha256 = "4b4314bbf1c2029fdf793637e6c7bb15c1b1730d22be9aa04803c98c5bbc446f"
hardening = ["vis", "!cfi"]
# FIXME: they hang forever, after failing a test for -v not silencing output in harness
# zsh completions don't match command
options = ["!check", "!lintcomp"]


@subpackage("notmuch-devel")
def _(self):
    return self.default_devel()

pkgname = "liburing"
pkgver = "2.4"
pkgrel = 0
build_style = "configure"
configure_args = ["--mandir=/usr/share/man"]
make_cmd = "gmake"
make_check_target = "runtests"
hostmakedepends = [
    "bash",
    "gmake",
    "pkgconf",
]
makedepends = ["linux-headers"]
pkgdesc = "Linux kernel io_uring access library"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-or-later OR MIT"
url = "https://git.kernel.dk/cgit/liburing"
source = f"https://github.com/axboe/liburing/archive/refs/tags/liburing-{pkgver}.tar.gz"
sha256 = "2398ec82d967a6f903f3ae1fd4541c754472d3a85a584dc78c5da2fabc90706b"
# vis breaks symbols
hardening = []
# FIXME: run into timeout
options = ["!check"]


def init_configure(self):
    majver, minver = pkgver.split(".")
    self.env["VERSION_MAJOR"] = majver
    self.env["VERSION_MINOR"] = minver


def post_install(self):
    self.install_license("LICENSE")


@subpackage("liburing-devel")
def _devel(self):
    return self.default_devel()

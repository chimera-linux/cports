pkgname = "liburing"
pkgver = "2.5"
pkgrel = 0
build_style = "configure"
configure_args = ["--mandir=/usr/share/man", "--use-libc"]
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
source = f"{url}/snapshot/liburing-{pkgver}.tar.gz"
sha256 = "96a04054158a89d02c28eadc7cc7db5ac0d8049120f9cb78765e961a312ca2e3"
# vis breaks symbols
hardening = []
# FIXME: run into timeout
options = ["!check", "linkundefver"]


def init_configure(self):
    majver, minver = pkgver.split(".")
    self.env["VERSION_MAJOR"] = majver
    self.env["VERSION_MINOR"] = minver


def post_install(self):
    self.install_license("LICENSE")


@subpackage("liburing-devel")
def _devel(self):
    return self.default_devel()

pkgname = "liburing"
pkgver = "2.6"
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
sha256 = "1d3a780f842e1f077600a1c241b9ca71b5340b257620a73652f9aca155818314"
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

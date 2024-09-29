pkgname = "libcgroup"
pkgver = "3.1.0"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--disable-systemd",
]
hostmakedepends = [
    "automake",
    "flex",
    "libtool",
    "pkgconf",
]
makedepends = [
    "chimerautils-devel",
    "linux-headers",
    "linux-pam-devel",
]
checkdepends = ["bash"]
pkgdesc = "Cgroup library and commandline utilities for managing cgroups"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-only"
url = "https://github.com/libcgroup/libcgroup"
source = f"{url}/releases/download/v{pkgver}/libcgroup-{pkgver}.tar.gz"
sha256 = "976ec4b1e03c0498308cfd28f1b256b40858f636abc8d1f9db24f0a7ea9e1258"
# vis breaks symbols
hardening = []
# tests need.. sudo..
options = ["!check", "linkundefver"]


def post_install(self):
    # nuke suid
    (self.destdir / "usr/bin/cgexec").chmod(0o755)


@subpackage("libcgroup-devel")
def _(self):
    return self.default_devel()


@subpackage("libcgroup-progs")
def _(self):
    return self.default_progs()


@subpackage("pam_cgroup")
def _(self):
    self.subdesc = "PAM"
    self.depends = [self.parent, "linux-pam"]
    self.install_if = [self.parent, "linux-pam"]
    return [
        "usr/lib/security",
    ]

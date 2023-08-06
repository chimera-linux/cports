pkgname = "libcgroup"
pkgver = "3.1.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--disable-systemd",
]
hostmakedepends = [
    "autoconf",
    "automake",
    "flex",
    "libtool",
    "pkgconf",
]
makedepends = [
    "linux-headers",
    "linux-pam-devel",
    "musl-fts-devel",
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
options = ["!check"]


def post_install(self):
    # nuke suid
    (self.destdir / "usr/bin/cgexec").chmod(0o755)


@subpackage("libcgroup-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libcgroup-progs")
def _progs(self):
    return self.default_progs()


@subpackage("pam_cgroup")
def _pam(self):
    self.pkgdesc = f"{pkgdesc} (PAM)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}", "linux-pam"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "linux-pam"]
    return [
        "usr/lib/security",
    ]

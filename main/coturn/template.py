pkgname = "coturn"
pkgver = "4.6.2"
pkgrel = 3
build_style = "gnu_configure"
configure_args = ["--turndbdir=/var/lib/coturn"]
configure_gen = []
make_dir = "."
make_check_target = "test"
hostmakedepends = ["pkgconf"]
makedepends = [
    "hiredis-devel",
    "libevent-devel",
    "linux-headers",
    "openssl-devel",
    "sqlite-devel",
]
pkgdesc = "VoIP media traffic NAT traversal server and gateway"
maintainer = "ttyyls <contact@behri.org>"
license = "BSD-3-Clause"
url = "https://github.com/coturn/coturn"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "13f2a38b66cffb73d86b5ed24acba4e1371d738d758a6039e3a18f0c84c176ad"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "coturn")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    # copied via tmpfiles instead
    self.rename(
        "var/lib/coturn/turndb", "usr/share/turnserver/turndb", relative=False
    )


@subpackage("coturn-devel")
def _(self):
    return self.default_devel()

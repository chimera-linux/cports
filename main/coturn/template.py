pkgname = "coturn"
pkgver = "4.6.3"
pkgrel = 0
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
    "openssl3-devel",
    "sqlite-devel",
]
pkgdesc = "VoIP media traffic NAT traversal server and gateway"
maintainer = "ttyyls <contact@behri.org>"
license = "BSD-3-Clause"
url = "https://github.com/coturn/coturn"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "dc3a529fd9956dc8771752a7169c5ad4c18b9deef3ec96049de30fabf1637704"
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

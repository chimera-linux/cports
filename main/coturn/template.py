pkgname = "coturn"
pkgver = "4.7.0"
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
license = "BSD-3-Clause"
url = "https://github.com/coturn/coturn"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "adbc90550d326e1b0fef4ccf9955c0ea32e63792acedcbc9cdbe9f71f380e622"


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

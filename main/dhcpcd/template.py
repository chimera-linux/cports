pkgname = "dhcpcd"
pkgver = "10.0.2"
pkgrel = 1
build_style = "configure"
configure_args = [
    "--prefix=/usr",
    "--sbindir=/usr/bin",
    "--sysconfdir=/etc",
    "--rundir=/run/dhcpcd",
    "--dbdir=/var/lib/dhcpcd",
    "--privsepuser=_dhcpcd",
    "--enable-privsep",
]
make_check_target = "test"
hostmakedepends = ["pkgconf"]
makedepends = ["udev-devel", "linux-headers"]
depends = ["resolvconf"]
pkgdesc = "RFC2131 compliant DHCP client"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://roy.marples.name/projects/dhcpcd"
source = f"https://github.com/NetworkConfiguration/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "3aa15c50be86d9595467f21dd9dc66f7115e3de1f5ab0b704b753684062b8541"
# FIXME cfi
# FIXME vis for usr/lib/dhcpcd/dev/udev.so
hardening = ["!vis", "!cfi"]

system_users = [
    {
        "name": "_dhcpcd",
        "id": None,
        "home": "/var/lib/dhcpcd",
    }
]


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "dhcpcd")

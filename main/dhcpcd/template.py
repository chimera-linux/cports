pkgname = "dhcpcd"
pkgver = "10.0.0"
pkgrel = 0
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
source = f"https://github.com/NetworkConfiguration/{pkgname}/archive/refs/tags/{pkgname}-{pkgver}.tar.gz"
sha256 = "3672496b27cc29ac385c503f23647ed5b00e58b9993db42ddf3b970d1c1bf900"
# FIXME cfi
hardening = ["vis", "!cfi"]

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

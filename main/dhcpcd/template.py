pkgname = "dhcpcd"
pkgver = "9.4.1"
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
depends = ["openresolv"]
pkgdesc = "RFC2131 compliant DHCP client"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://roy.marples.name/projects/dhcpcd"
source = f"https://roy.marples.name/downloads/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "819357634efed1ea5cf44ec01b24d3d3f8852fec8b4249925dcc5667c54e376c"
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

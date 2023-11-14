pkgname = "dhcpcd"
pkgver = "10.0.5"
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
source = f"https://github.com/NetworkConfiguration/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "eb1f3cfef3069781ff8c896d7cea922639964afe22db28c069dc3f37f57eb428"
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

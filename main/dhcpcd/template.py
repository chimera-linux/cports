pkgname = "dhcpcd"
pkgver = "10.0.7"
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
source = f"https://github.com/NetworkConfiguration/dhcpcd/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "d5b15d6ca3fc6ee6eb01e49f67007a14a406fc83155d1c9a90e1ea9e71c9e769"
# FIXME cfi
# FIXME vis for usr/lib/dhcpcd/dev/udev.so
hardening = ["!vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_file(
        self.files_path / "sysusers.conf",
        "usr/lib/sysusers.d",
        name="dhcpcd.conf",
    )
    self.install_file(
        self.files_path / "tmpfiles.conf",
        "usr/lib/tmpfiles.d",
        name="dhcpcd.conf",
    )
    self.install_service(self.files_path / "dhcpcd")

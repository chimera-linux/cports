pkgname = "dhcpcd"
pkgver = "10.3.2"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--prefix=/usr",
    "--sbindir=/usr/bin",
    "--libexecdir=/usr/lib",
    "--sysconfdir=/etc",
    "--rundir=/run/dhcpcd",
    "--dbdir=/var/lib/dhcpcd",
    "--privsepuser=_dhcpcd",
    "--enable-privsep",
]
make_check_target = "test"
hostmakedepends = ["pkgconf"]
makedepends = ["dinit-chimera", "udev-devel", "linux-headers"]
depends = ["resolvconf"]
pkgdesc = "RFC2131 compliant DHCP client"
license = "BSD-2-Clause"
url = "https://roy.marples.name/projects/dhcpcd"
source = f"https://github.com/NetworkConfiguration/dhcpcd/releases/download/v{pkgver}/dhcpcd-{pkgver}.tar.xz"
sha256 = "b6aa46932074906a9badef1bfe142b8aff9d041c2689e1ef8b74c12e9fd942bd"
# FIXME vis for usr/lib/dhcpcd/dev/udev.so
hardening = ["!vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_sysusers("^/sysusers.conf")
    self.install_tmpfiles("^/tmpfiles.conf")
    self.install_service("^/dhcpcd")

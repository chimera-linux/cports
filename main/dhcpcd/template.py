pkgname = "dhcpcd"
pkgver = "10.3.1"
pkgrel = 0
build_style = "configure"
# XXX drop libexec
configure_args = [
    "--libexecdir=/usr/lib",
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
makedepends = ["dinit-chimera", "udev-devel", "linux-headers"]
depends = ["resolvconf"]
pkgdesc = "RFC2131 compliant DHCP client"
license = "BSD-2-Clause"
url = "https://roy.marples.name/projects/dhcpcd"
source = f"https://github.com/NetworkConfiguration/dhcpcd/releases/download/v{pkgver}/dhcpcd-{pkgver}.tar.xz"
sha256 = "1aed450dfd22f280a64f7e5feee148d29727c292a3d1819287cf4f98b12d4a68"
# FIXME vis for usr/lib/dhcpcd/dev/udev.so
hardening = ["!vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_sysusers("^/sysusers.conf")
    self.install_tmpfiles("^/tmpfiles.conf")
    self.install_service("^/dhcpcd")

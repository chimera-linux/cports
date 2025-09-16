pkgname = "dhcpcd"
pkgver = "10.2.4"
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
sha256 = "6721e606609226dbf4d864a78802a9e96beec0ee034a1bd84138b3e037bba7d9"
# FIXME vis for usr/lib/dhcpcd/dev/udev.so
hardening = ["!vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_sysusers("^/sysusers.conf")
    self.install_tmpfiles("^/tmpfiles.conf")
    self.install_service("^/dhcpcd")

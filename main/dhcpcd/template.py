pkgname = "dhcpcd"
pkgver = "10.5.2"
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
    "--without-libpcap",
]
make_check_target = "test"
hostmakedepends = ["pkgconf"]
makedepends = ["dinit-chimera", "udev-devel", "linux-headers"]
depends = ["resolvconf"]
pkgdesc = "RFC2131 compliant DHCP client"
license = "BSD-2-Clause"
url = "https://roy.marples.name/projects/dhcpcd"
source = f"https://github.com/NetworkConfiguration/dhcpcd/releases/download/v{pkgver}/dhcpcd-{pkgver}.tar.xz"
sha256 = "3e476657fdb6eeb38b277da3a48d0ac0113ecce5858ebdcddff2b629faed52b4"
options = ["etcfiles"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "dhcpcd")

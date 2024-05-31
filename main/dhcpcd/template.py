pkgname = "dhcpcd"
pkgver = "10.0.8"
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
sha256 = "d8dddf9f971a8d9ff828f33d8fa9f6d9a892a4a1429d230e9efb2be97dd0e313"
# FIXME cfi
# FIXME vis for usr/lib/dhcpcd/dev/udev.so
hardening = ["!vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "dhcpcd")

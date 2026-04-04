pkgname = "dnsmasq"
pkgver = "2.92"
pkgrel = 0
build_style = "makefile"
make_install_args = ["BINDIR=/usr/bin"]
hostmakedepends = ["pkgconf"]
makedepends = [
    "dbus-devel",
    "dinit-chimera",
    "dinit-dbus",
    "libidn2-devel",
    "libnetfilter_conntrack-devel",
    "linux-headers",
    "nettle-devel",
]
depends = ["dinit-dbus"]
pkgdesc = "DNS, DHCP, RA, TFTP and PXE server"
license = "GPL-2.0-or-later"
url = "https://www.thekelleys.org.uk/dnsmasq/doc.html"
source = f"https://www.thekelleys.org.uk/dnsmasq/dnsmasq-{pkgver}.tar.gz"
sha256 = "fd908e79ff37f73234afcb6d3363f78353e768703d92abd8e3220ade6819b1e1"
# no tests
options = ["!check"]


def post_install(self):
    self.install_file("dnsmasq.conf.example", "etc", name="dnsmasq.conf")
    self.install_file("trust-anchors.conf", "usr/share/dnsmasq")
    self.install_file("dbus/dnsmasq.conf", "usr/share/dbus-1/system.d")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_service(self.files_path / "dnsmasq")

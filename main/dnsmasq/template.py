pkgname = "dnsmasq"
pkgver = "2.90"
pkgrel = 3
build_style = "makefile"
make_install_args = ["BINDIR=/usr/bin"]
hostmakedepends = ["pkgconf"]
makedepends = [
    "dbus-devel",
    "libidn2-devel",
    "libnetfilter_conntrack-devel",
    "linux-headers",
    "nettle-devel",
]
depends = ["dinit-dbus"]
pkgdesc = "DNS, DHCP, RA, TFTP and PXE server"
maintainer = "cesorious <cesorious@gmail.com>"
license = "GPL-2.0-or-later"
url = "https://www.thekelleys.org.uk/dnsmasq/doc.html"
source = f"https://www.thekelleys.org.uk/dnsmasq/dnsmasq-{pkgver}.tar.gz"
sha256 = "8f6666b542403b5ee7ccce66ea73a4a51cf19dd49392aaccd37231a2c51b303b"
# no tests
options = ["!check"]


def post_install(self):
    self.install_file("dnsmasq.conf.example", "etc", name="dnsmasq.conf")
    self.install_file("trust-anchors.conf", "usr/share/dnsmasq")
    self.install_file("dbus/dnsmasq.conf", "usr/share/dbus-1/system.d")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_service(self.files_path / "dnsmasq")

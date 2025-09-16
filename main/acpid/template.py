pkgname = "acpid"
pkgver = "2.0.34"
pkgrel = 4
build_style = "gnu_configure"
hostmakedepends = ["automake"]
makedepends = ["dinit-chimera", "linux-headers"]
pkgdesc = "ACPI Daemon (acpid) With Netlink Support"
license = "GPL-2.0-or-later"
url = "https://sourceforge.net/projects/acpid2"
source = f"https://downloads.sourceforge.net/sourceforge/acpid2/acpid-{pkgver}.tar.xz"
sha256 = "2d095c8cfcbc847caec746d62cdc8d0bff1ec1bc72ef7c674c721e04da6ab333"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_service(self.files_path / "acpid")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")

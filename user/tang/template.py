pkgname = "tang"
pkgver = "15"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Duser=_tang",
    "-Dgroup=_tang",
    "--libexecdir=/usr/lib",
]
hostmakedepends = [
    "asciidoc",
    "meson",
    "pkgconf",
]
makedepends = [
    "http-parser-devel",
    "jose-devel",
]
checkdepends = [
    "curl",
    "iproute2",
    "socat",
]
pkgdesc = "Server for binding data to network presence"
license = "GPL-3.0-or-later"
url = "https://github.com/latchset/tang"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0bbaeaa6cde36ccc11102b9dc82dcd707f60ebd290d3930c8a1e4e55a50a7da9"
hardening = ["vis", "cfi"]


def post_install(self):
    self.uninstall("usr/lib/systemd/system")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")

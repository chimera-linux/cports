pkgname = "tor"
pkgver = "0.4.9.14"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "asciidoc",
    "automake",
    "pkgconf",
]
makedepends = [
    "dinit-chimera",
    "libevent-devel",
    "linux-headers",
    "openssl3-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
checkdepends = ["bash"]
pkgdesc = "Anonymizing overlay network"
license = "BSD-3-Clause"
url = "https://gitlab.com/torproject/tor"
source = f"{url}/-/archive/tor-{pkgver}/tor-tor-{pkgver}.tar.gz"
sha256 = "1eca189920bc14316e2f2c5e662916e4fc90eae898705d1374af870bde7d8d5d"


def post_install(self):
    # only contains a sample
    self.uninstall("etc")
    self.install_file("src/config/torrc.sample.in", "usr/share/examples/tor")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "tor")
    self.install_license("LICENSE")

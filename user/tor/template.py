pkgname = "tor"
pkgver = "0.4.9.13"
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
sha256 = "72cbba45e583f3be32854cdc4f55c5f82e6686475e1054b3718891bcd20ae057"


def post_install(self):
    # only contains a sample
    self.uninstall("etc")
    self.install_file("src/config/torrc.sample.in", "usr/share/examples/tor")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "tor")
    self.install_license("LICENSE")

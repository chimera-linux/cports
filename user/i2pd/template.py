pkgname = "i2pd"
pkgver = "2.61.0"
pkgrel = 0
build_style = "makefile"
make_build_args = ["USE_UPNP=yes", "DEBUG=no"]
make_check_target = "all"
make_check_args = ["-C", "tests"]
makedepends = [
    "boost-devel",
    "dinit-chimera",
    "miniupnpc-devel",
    "openssl3-devel",
]
pkgdesc = "I2P router"
license = "BSD-3-Clause"
url = "https://github.com/PurpleI2P/i2pd"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "409cd3c0257491286611ab6aaf690940c7248fb898377c13fadb65a836e2a0ab"
options = ["etcfiles"]


def install(self):
    self.make.install([f"PREFIX={self.chroot_destdir}/usr"])
    self.uninstall("usr/var")
    self.rename("usr/etc", "etc", relative=False)
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "i2pd")
    self.install_license("LICENSE")

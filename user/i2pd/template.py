pkgname = "i2pd"
pkgver = "2.56.0"
pkgrel = 0
build_style = "makefile"
make_build_args = ["USE_STATIC=yes", "USE_UPNP=yes", "DEBUG=no"]
makedepends = [
    "boost-devel",
    "openssl3-devel",
    "miniupnpc-devel",
]
pkgdesc = "I2P Router written in C++"
license = "BSD-3-Clause"
url = "https://github.com/PurpleI2P/i2pd"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "eb83f7e98afeb3704d9ee0da2499205f73bab0b1becaf4494ccdcbe4295f8550"
# no check
options = ["!check"]


def install(self):
    self.install_bin(self.cwd / "i2pd")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_file(
        self.files_path / "i2pd.wrapper", "usr/libexec", mode=0o755
    )
    self.install_service(self.files_path / "i2pd")
    self.install_files("contrib/certificates", "usr/share/i2pd")
    self.install_file("contrib/i2pd.conf", "usr/share/i2pd")
    self.install_file("contrib/tunnels.conf", "usr/share/i2pd")
    self.install_license("LICENSE")

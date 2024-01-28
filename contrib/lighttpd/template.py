pkgname = "lighttpd"
pkgver = "1.4.76"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["musl-bsd-headers", "openssl-devel", "pcre2-devel"]
checkdepends = ["perl"]
pkgdesc = "Lightweight web server"
maintainer = "yanchan09 <yan@omg.lol>"
license = "BSD-3-Clause"
url = "https://lighttpd.net"
source = f"https://download.lighttpd.net/{pkgname}/releases-{pkgver[:pkgver.rfind('.')]}.x/{pkgname}-{pkgver}.tar.xz"
sha256 = "8cbf4296e373cfd0cedfe9d978760b5b05c58fdc4048b4e2bcaf0a61ac8f5011"


def post_install(self):
    self.install_license("COPYING")
    self.install_file(
        self.files_path / "sysusers.conf",
        "usr/lib/sysusers.d",
        name="lighttpd.conf",
    )
    self.install_file(self.files_path / "lighttpd.conf", "etc/lighttpd")
    self.install_service(self.files_path / "lighttpd")

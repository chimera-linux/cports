pkgname = "lighttpd"
pkgver = "1.4.73"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["musl-bsd-headers", "openssl-devel", "pcre2-devel"]
checkdepends = ["perl"]
pkgdesc = "Secure, fast, compliant and very flexible web server"
maintainer = "yanchan09 <yan@omg.lol>"
license = "BSD-3-Clause"
url = "https://lighttpd.net"
source = f"https://download.lighttpd.net/{pkgname}/releases-{pkgver[:pkgver.rfind('.')]}.x/{pkgname}-{pkgver}.tar.xz"
sha256 = "818816d0b314b0aa8728a7076513435f6d5eb227f3b61323468e1f10dbe84ca8"


def post_install(self):
    self.install_license("COPYING")
    self.install_file(
        self.files_path / "sysusers.conf",
        "usr/lib/sysusers.d",
        name="lighttpd.conf",
    )
    self.install_file(self.files_path / "lighttpd.conf", "etc/lighttpd")
    self.install_service(self.files_path / "lighttpd")

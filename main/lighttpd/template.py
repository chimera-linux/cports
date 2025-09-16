pkgname = "lighttpd"
pkgver = "1.4.79"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dwith_brotli=enabled",
    "-Dwith_libdeflate=enabled",
    "-Dwith_lua=true",
    "-Dwith_openssl=true",
    "-Dwith_webdav_props=enabled",
    "-Dwith_xxhash=enabled",
    "-Dwith_zstd=enabled",
]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "brotli-devel",
    "dinit-chimera",
    "libdeflate-devel",
    "libxml2-devel",
    "lua5.4-devel",
    "musl-bsd-headers",
    "openssl3-devel",
    "pcre2-devel",
    "sqlite-devel",
    "xxhash-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
checkdepends = ["perl"]
pkgdesc = "Lightweight web server"
license = "BSD-3-Clause"
url = "https://lighttpd.net"
source = f"https://download.lighttpd.net/lighttpd/releases-{pkgver[: pkgver.rfind('.')]}.x/lighttpd-{pkgver}.tar.xz"
sha256 = "3b29a625b3ad88702d1fea4f5f42bb7d87488f2e4efc977d7f185329ca6084bd"


def post_install(self):
    self.install_license("COPYING")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_file(self.files_path / "lighttpd.conf", "etc/lighttpd")
    self.install_service(self.files_path / "lighttpd")

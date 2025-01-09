pkgname = "lighttpd"
pkgver = "1.4.76"
pkgrel = 1
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
    "libdeflate-devel",
    "libxml2-devel",
    "lua5.4-devel",
    "musl-bsd-headers",
    "openssl-devel",
    "pcre2-devel",
    "sqlite-devel",
    "xxhash-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
checkdepends = ["perl"]
pkgdesc = "Lightweight web server"
maintainer = "yanchan09 <yan@omg.lol>"
license = "BSD-3-Clause"
url = "https://lighttpd.net"
source = f"https://download.lighttpd.net/lighttpd/releases-{pkgver[: pkgver.rfind('.')]}.x/lighttpd-{pkgver}.tar.xz"
sha256 = "8cbf4296e373cfd0cedfe9d978760b5b05c58fdc4048b4e2bcaf0a61ac8f5011"


def post_install(self):
    self.install_license("COPYING")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_file(self.files_path / "lighttpd.conf", "etc/lighttpd")
    self.install_service(self.files_path / "lighttpd")

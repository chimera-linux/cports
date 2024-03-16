pkgname = "waypipe"
pkgver = "0.9.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dwith_dmabuf=enabled",
    "-Dwith_systemtap=false",
    "-Dwith_vaapi=enabled",
    "-Dwith_video=enabled",
    "-Dwith_zstd=enabled",
    "-Db_ndebug=true",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
    "wayland-progs",
]
makedepends = [
    "ffmpeg-devel",
    "libdrm-devel",
    "libva-devel",
    "lz4-devel",
    "mesa-devel",
    "wayland-devel",
    "wayland-protocols",
    "zstd-devel",
]
pkgdesc = "Proxy for wayland clients"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://gitlab.freedesktop.org/mstoeckl/waypipe"
source = f"https://gitlab.freedesktop.org/mstoeckl/waypipe/-/archive/v{pkgver}/waypipe-v{pkgver}.tar.bz2"
sha256 = "79d5e8c534e190b0f076ae2e9cd711881d31efc58dbbd6326b477f3ed5a99807"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")

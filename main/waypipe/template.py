pkgname = "waypipe"
pkgver = "0.9.1"
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
sha256 = "d60d94a19038d2e231e3f1bf8122ae0894bc78fa753190f6e831c7931f8caaab"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")

pkgname = "waypipe"
pkgver = "0.8.6"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dwith_dmabuf=enabled",
    "-Dwith_systemtap=false",
    "-Dwith_vaapi=enabled",
    "-Dwith_video=enabled",
    "-Dwith_zstd=enabled",
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
    "libzstd-devel",
    "mesa-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Proxy for wayland clients"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://gitlab.freedesktop.org/mstoeckl/waypipe"
source = f"https://gitlab.freedesktop.org/mstoeckl/waypipe/-/archive/v{pkgver}/waypipe-v{pkgver}.tar.bz2"
sha256 = "da40de2e02d60c2c34d549e791a9019c1ddf9d79f42bfad0c6cb74f3f6af9b16"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")

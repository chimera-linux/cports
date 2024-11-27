pkgname = "waypipe"
pkgver = "0.9.2"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://gitlab.freedesktop.org/mstoeckl/waypipe"
source = f"https://gitlab.freedesktop.org/mstoeckl/waypipe/-/archive/v{pkgver}/waypipe-v{pkgver}.tar.bz2"
sha256 = "ef0783ba95abb950cb0e876e1d186de77905759ed7406ec23973f46cab96b5ee"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")

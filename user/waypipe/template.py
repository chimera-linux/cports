pkgname = "waypipe"
pkgver = "0.10.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dwith_dmabuf=enabled",
    "-Dwith_gbm=enabled",
    "-Dwith_systemtap=false",
    "-Dwith_video=enabled",
    "-Dwith_zstd=enabled",
]
hostmakedepends = [
    "cargo-auditable",
    "meson",
    "pkgconf",
    "rust-bindgen",
    "scdoc",
    "shaderc-progs",
    "wayland-progs",
]
makedepends = [
    "ffmpeg-devel",
    "libdrm-devel",
    "libva-devel",
    "lz4-devel",
    "mesa-devel",
    "rust-std",
    "vulkan-headers",
    "vulkan-loader-devel",
    "wayland-devel",
    "wayland-protocols",
    "zstd-devel",
]
# dynamically loaded
depends = [
    "so:libavcodec.so.61!ffmpeg-avcodec-libs",
    "so:libgbm.so.1!mesa-gbm-libs",
]
pkgdesc = "Proxy for wayland clients"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gitlab.freedesktop.org/mstoeckl/waypipe"
source = f"https://gitlab.freedesktop.org/mstoeckl/waypipe/-/archive/v{pkgver}/waypipe-v{pkgver}.tar.bz2"
sha256 = "60d8d0d0b1a7f356eff82404b2d3a3be0d2348c0c6aaec413f490a825a04ae7d"

if self.profile().wordsize == 32:
    broken = "some u64 nonsense in vulkan code"


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(f"./build/target/{self.profile().triplet}/meson-2/waypipe")

pkgname = "waypipe"
pkgver = "0.11.2"
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
    "so:libavcodec.so.62!ffmpeg-avcodec-libs",
    "so:libgbm.so.1!mesa-gbm-libs",
]
pkgdesc = "Proxy for wayland clients"
license = "GPL-3.0-or-later"
url = "https://gitlab.freedesktop.org/mstoeckl/waypipe"
source = f"https://gitlab.freedesktop.org/mstoeckl/waypipe/-/archive/v{pkgver}/waypipe-v{pkgver}.tar.bz2"
sha256 = "be2d59871a9dc67a78f800f08cfba08bb22d660a97a2def24a4df9b8da6196a7"

if self.profile.wordsize == 32:
    broken = "some u64 nonsense in vulkan code"


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    from cbuild.util import cargo

    self.install_bin(
        cargo.target_path(self, "waypipe", "build/target", "meson-2")
    )

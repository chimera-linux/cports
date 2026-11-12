pkgname = "uzdoom"
pkgver = "5.0.3"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DFORCE_INTERNAL_WEBP=OFF",
    "-DDYN_MPG123=OFF",
    "-DDYN_OPENAL=OFF",
    "-DDYN_SNDFILE=OFF",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "python"]
makedepends = [
    "abseil-cpp-devel",
    "alsa-lib-devel",
    "bzip2-devel",
    "chimerautils-devel",
    "dbus-devel",
    "fluidsynth-devel",
    "glib-devel",
    "libglvnd-devel",
    "libsndfile-devel",
    "libvpx-devel",
    "libwebp-devel",
    "libx11-devel",
    "mpg123-devel",
    "openal-soft-devel",
    "sdl2-compat-devel",
    "vulkan-loader-devel",
]
pkgdesc = "Feature-centric DOOM port"
license = "GPL-3.0-or-later"
url = "http://zdoom.org"
source = f"https://github.com/UZDoom/UZDoom/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "223d7abef2c7a63123824417a2fe5b22e21e7dcb2ac5c840fca43c470794cab7"
tool_flags = {
    "CFLAGS": ["-D_GNU_SOURCE", "-DZ7_AFFINITY_DISABLE"],
}
hardening = ["!int"]

if self.profile.arch in [
    "aarch64",
    "loongarch64",
    "ppc64le",
    "ppc64",
    "riscv64",
    "x86_64",
]:
    makedepends += ["libomp-devel"]

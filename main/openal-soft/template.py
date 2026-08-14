pkgname = "openal-soft"
pkgver = "1.25.2"
pkgrel = 1
build_style = "cmake"
configure_args = ["-DALSOFT_EXAMPLES=OFF"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "ffmpeg-devel",
    "libpulse-devel",
    "pipewire-devel",
    "pipewire-jack-devel",
    "sdl3-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Cross-platform 3D audio API"
license = "LGPL-2.1-or-later"
url = "https://openal-soft.org"
# expired certificate
# source = f"{url}/openal-releases/openal-soft-{pkgver}.tar.bz2"
source = f"https://github.com/kcat/openal-soft/archive/{pkgver}.tar.gz"
sha256 = "fb27e5839aa11f0e5b9d33756965291fad5d6909ab928ea1f796f4a1a6877894"
# no test target
options = ["!check"]

if self.profile().arch != "x86_64":
    # some archs provide emulation of x86 simd intrinsics in the compiler
    # and openal tries to use them and fails since they are not native
    configure_args += [
        "-DALSOFT_CPUEXT_SSE=OFF",
        "-DALSOFT_CPUEXT_SSE2=OFF",
        "-DALSOFT_CPUEXT_SSE3=OFF",
        "-DALSOFT_CPUEXT_SSE4_1=OFF",
    ]


def post_install(self):
    self.uninstall("usr/share/openal/alsoftrc.sample")
    self.install_file("alsoftrc.sample", "usr/share/examples/openal-soft")


@subpackage("openal-soft-devel")
def _(self):
    return self.default_devel()

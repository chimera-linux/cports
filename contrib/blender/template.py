pkgname = "blender"
pkgver = "4.1.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DWITH_INSTALL_PORTABLE=OFF",
    "-DWITH_SYSTEM_FREETYPE=ON",
    "-DWITH_SYSTEM_EIGEN3=ON",
    "-DWITH_SYSTEM_LZO=ON",
    "-DWITH_PYTHON_INSTALL=OFF",
    "-DWITH_LIBS_PRECOMPILED=OFF",
    "-DWITH_LLVM=ON",
    "-DWITH_CLANG=ON",
    "-DPYTHON_VERSION=3.12",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "boost-devel",
    "eigen",
    "ffmpeg-devel",
    "fftw-devel",
    "freetype-devel",
    "gmpxx-devel",
    "libepoxy-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libpulse-devel",
    "libsndfile-devel",
    "libtiff-devel",
    "libwebp-devel",
    "onetbb-devel",
    "openal-soft-devel",
    "opencolorio-devel",
    "openexr-devel",
    "openimageio-devel",
    "openjpeg-devel",
    "pipewire-jack-devel",
    "potrace-devel",
    "pugixml-devel",
    "python-devel",
    "python-numpy",
    "sdl-devel",
    "wayland-devel",
    "zstd-devel",
]
depends = ["python-numpy", "python-zstandard"]
pkgdesc = "3D creation suite"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://www.blender.org"
source = f"https://download.blender.org/source/blender-{pkgver}.tar.xz"
sha256 = "4fbb3af64d3f84df5c7103748454226c1885c1ac2ed5373d0cea1e80e82c0848"
tool_flags = {"LDFLAGS": ["-Wl,--undefined-version"]}
# tests expect blender to be installed in /usr/bin
options = ["!check"]

if self.profile().arch in ["aarch64", "armv7", "x86_64"]:
    makedepends += ["openimagedenoise-devel"]

if self.profile().arch in ["aarch64", "x86_64"]:
    makedepends += ["embree-devel"]
else:
    configure_args += ["-DWITH_CYCLES_EMBREE=NO"]

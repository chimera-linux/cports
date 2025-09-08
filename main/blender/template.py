pkgname = "blender"
pkgver = "4.5.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-C",
    # predefined config with everything we want
    "../build_files/cmake/config/blender_full.cmake",
    "-DWITH_CLANG=ON",
    "-DWITH_CYCLES_OSL=ON",
    "-DWITH_INSTALL_PORTABLE=OFF",
    "-DWITH_INSTALL_PORTABLE=OFF",
    "-DWITH_LIBS_PRECOMPILED=OFF",
    "-DWITH_LLVM=ON",
    "-DWITH_PYTHON_INSTALL=OFF",
    "-DWITH_PYTHON_INSTALL_NUMPY=OFF",
    "-DWITH_PYTHON_INSTALL_REQUESTS=OFF",
    "-DWITH_PYTHON_INSTALL_ZSTANDARD=OFF",
    "-DWITH_SYSTEM_EIGEN3=ON",
    "-DWITH_SYSTEM_FREETYPE=ON",
    "-DWITH_SYSTEM_LZO=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "openimageio-progs",
    "openshadinglanguage-progs",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "clang-devel",
    "eigen",
    "ffmpeg-devel",
    "fftw-devel",
    "freetype-devel",
    "gmp-gmpxx-devel",
    "libepoxy-devel",
    "libharu-devel",
    "libjpeg-turbo-devel",
    "libomp-devel",
    "libpng-devel",
    "libpulse-devel",
    "libsndfile-devel",
    "libtiff-devel",
    "libwebp-devel",
    "llvm-devel",
    "onetbb-devel",
    "openal-soft-devel",
    "opencolorio-devel",
    "openexr-devel",
    "openimageio-devel",
    "openjpeg-devel",
    "openshadinglanguage-devel",
    "opensubdiv-devel",
    "openvdb-devel",
    "pipewire-jack-devel",
    "potrace-devel",
    "pugixml-devel",
    "python-devel",
    "python-numpy",
    "shaderc-devel",
    "vulkan-loader-devel",
    "wayland-devel",
    "zstd-devel",
]
depends = [
    "python-numpy",
    "python-requests",
    "python-zstandard",
]
pkgdesc = "3D creation suite"
license = "GPL-2.0-or-later"
url = "https://www.blender.org"
source = f"https://download.blender.org/source/blender-{pkgver}.tar.xz"
sha256 = "ff225337b6695631b82008e94a45f0b53711d2d52497b86063d3c86880627d1f"
tool_flags = {
    "CFLAGS": ["-D_GNU_SOURCE"],
    # guilty until proven innocent
    "LDFLAGS": ["-Wl,-z,stack-size=0x200000"],
}
# var-init seems to pessimise a large stack-reuse optimisation, so repeatedly
# using a large chunk of stack via onetbb causes memset calls where otherwise
# there would be none and it makes rendering 5x slower
hardening = ["!int", "!var-init"]
# tests expect blender to be installed in /usr/bin
options = ["!check", "linkundefver"]

if self.profile().endian == "little":
    makedepends += ["alembic-devel"]


match self.profile().arch:
    case "ppc64" | "ppc":
        # vsx assumptions in altivec code
        tool_flags = {"CXXFLAGS": ["-DEIGEN_DONT_VECTORIZE"]}

if self.profile().arch in ["aarch64", "armv7", "x86_64"]:
    makedepends += ["openimagedenoise-devel"]
    configure_args += ["-DWITH_OPENIMAGEDENOISE=ON"]
else:
    configure_args += ["-DWITH_OPENIMAGEDENOISE=OFF"]

if self.profile().arch in ["aarch64", "x86_64"]:
    makedepends += [
        "embree-devel",
        "openpgl-devel",
    ]
    configure_args += ["-DWITH_CYCLES_EMBREE=ON", "-DWITH_PATH_GUIDING=ON"]
else:
    configure_args += [
        "-DWITH_CYCLES=OFF",
        "-DWITH_CYCLES_EMBREE=OFF",
        "-DWITH_PATH_GUIDING=OFF",
    ]


def init_configure(self):
    self.configure_args += [f"-DPYTHON_VERSION={self.python_version}"]


def post_install(self):
    from cbuild.util import python

    # we don't allow elfs in usr/share, but this solib is loaded from
    # this location as it's relative to the io_scene_gltf2 module path
    draco_path = f"usr/share/blender/{pkgver[:-2]}/scripts/addons_core/io_scene_gltf2/libextern_draco.so"
    self.install_dir("usr/lib/blender")
    self.rename(
        draco_path, "usr/lib/blender/libextern_draco.so", relative=False
    )
    self.install_link(
        draco_path, "../../../../../../lib/blender/libextern_draco.so"
    )

    python.precompile(self, "usr/share/blender")

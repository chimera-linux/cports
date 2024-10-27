pkgname = "darktable"
pkgver = "4.8.1"
pkgrel = 2
# only supported archs
archs = ["aarch64", "ppc64le", "riscv64", "x86_64"]
build_style = "cmake"
configure_args = [
    # passes more release args
    "-DCMAKE_BUILD_TYPE=Release",
    "-DBINARY_PACKAGE_BUILD=ON",
    "-DDONT_USE_INTERNAL_LIBRAW=ON",
    "-DDONT_USE_INTERNAL_LUA=ON",
    "-DRAWSPEED_ENABLE_WERROR=OFF",
    "-DTESTBUILD_OPENCL_PROGRAMS=ON",
    "-DUSE_GMIC=ON",
    "-DUSE_GRAPHICSMAGICK=ON",
    "-DUSE_ICU=ON",
    "-DUSE_MAP=OFF",
    "-DUSE_OPENCL=ON",
    "-DUSE_OPENJPEG=OFF",
    "-DUSE_OPENMP=ON",
    "-DUSE_PORTMIDI=OFF",
    "-DUSE_SDL2=OFF",
]
hostmakedepends = [
    "bash",
    "cmake",
    "intltool",
    "iso-codes",
    "ninja",
    "pkgconf",
    "xsltproc",
]
makedepends = [
    "clang-devel",
    "clang-tools-extra",
    "colord-devel",
    "colord-gtk-devel",
    "cups-devel",
    "exiv2-devel",
    "gmic-devel",
    "graphicsmagick-devel",
    "gtk+3-devel",
    "imath-devel",
    "json-glib-devel",
    "lcms2-devel",
    "lensfun-devel",
    "libavif-devel",
    "libcurl-devel",
    "libedit-devel",
    "libgphoto2-devel",
    "libheif-devel",
    "libjxl-devel",
    "libomp-devel",
    "libraw-devel",
    "librsvg-devel",
    "libsecret-devel",
    "libwebp-devel",
    "llvm-devel",
    "lua5.4-devel",
    "ncurses-devel",
    "openexr-devel",
    "pugixml-devel",
    "sqlite-devel",
]
pkgdesc = "Open source photography workflow application and raw developer"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://www.darktable.org"
source = f"https://github.com/darktable-org/darktable/releases/download/release-{pkgver}/darktable-{pkgver}.tar.xz"
sha256 = "901b0e2caed36fb8619fdf4c60edfb8d31134b947d3054b5c66fd55c38af5991"

# with lto: ld: error: Invalid record (Producer: 'LLVM16.0.6' Reader: 'LLVM 16.0.6')
# without lto: ICE: fatal error: error in backend: Cannot select: 0x3fff9b420de0: ...
match self.profile().arch:
    case "ppc64le" | "riscv64":
        configure_args += ["-DUSE_OPENMP=OFF"]

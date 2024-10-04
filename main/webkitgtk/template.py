pkgname = "webkitgtk"
pkgver = "2.46.1"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DPORT=GTK",
    "-DCMAKE_SKIP_RPATH=ON",
    f"-DCMAKE_LINKER={self.profile().triplet}-clang",
    # -DUSE_*
    "-DUSE_GTK4=OFF",
    "-DUSE_LD_LLD=ON",
    "-DUSE_LIBBACKTRACE=OFF",
    "-DUSE_SOUP2=OFF",
    "-DUSE_WOFF2=ON",
    # -DENABLE_*
    "-DENABLE_BUBBLEWRAP_SANDBOX=ON",
    "-DENABLE_DOCUMENTATION=OFF",
    "-DENABLE_INTROSPECTION=ON",
    "-DENABLE_JOURNALD_LOG=OFF",
    "-DENABLE_MINIBROWSER=ON",
    "-DENABLE_SAMPLING_PROFILER=OFF",  # unavailable on musl
    "-DENABLE_WAYLAND_TARGET=ON",
    "-DENABLE_X11_TARGET=ON",
]
hostmakedepends = [
    "bubblewrap",
    "cmake",
    "flex",
    "geoclue",
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "gperf",
    "ninja",
    "perl",
    "pkgconf",
    "python",
    "ruby",
    "unifdef",
    "wayland-progs",
    "xdg-dbus-proxy",
]
makedepends = [
    "at-spi2-core-devel",
    "enchant-devel",
    "freetype-devel",
    "geoclue-devel",
    "gst-plugins-bad-devel",
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "gtk+3-devel",
    "harfbuzz-devel",
    "hyphen-devel",
    "icu-devel",
    "icu-devel",
    "lcms2-devel",
    "libavif-devel",
    "libgcrypt-devel",
    "libjpeg-turbo-devel",
    "libjxl-devel",
    "libmanette-devel",
    "libnotify-devel",
    "libpng-devel",
    "libpsl-devel",
    "libseccomp-devel",
    "libsecret-devel",
    "libsoup-devel",
    "libspiel-devel",
    "libtasn1-devel",
    "libwebp-devel",
    "libwpe-devel",
    "libxkbcommon-devel",
    "libxml2-devel",
    "libxslt-devel",
    "libxt-devel",
    "mesa-devel",
    "openjpeg-devel",
    "sqlite-devel",
    "sysprof-capture",
    "wayland-devel",
    "wayland-protocols",
    "woff2-devel",
    "wpebackend-fdo-devel",
]
depends = [
    "bubblewrap",
    "gst-plugins-bad",
    "gst-plugins-good",
    "xdg-dbus-proxy",
]
pkgdesc = "GTK port of the WebKit browser engine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later AND BSD-2-Clause"
url = "https://webkitgtk.org"
source = f"{url}/releases/webkitgtk-{pkgver}.tar.xz"
sha256 = "2a14faac359aff941d0bc4443eb5537e3702bcaf316b0a129e0e65f3ff8eaac0"
debug_level = 1  # otherwise LTO link runs out of memory + fat debuginfo
tool_flags = {
    "CFLAGS": ["-DNDEBUG"],
    "CXXFLAGS": [
        # also silence some really loud warnings...
        "-DNDEBUG",
        "-Wno-deprecated-declarations",
        "-Wno-deprecated-copy",
    ],
}
env = {
    # WebKitCCache.cmake
    "CCACHE_SLOPPINESS": "time_macros,include_file_mtime"
}
# FIXME: crashes in libpas (seems compiler-generated, not code bugs)
hardening = ["!int"]
# huge testsuite
options = ["!check"]

match self.profile().arch:
    case "x86_64" | "aarch64":
        configure_args += ["-DENABLE_JIT=ON", "-DENABLE_C_LOOP=OFF"]
    case _:
        configure_args += [
            "-DENABLE_JIT=OFF",
            "-DENABLE_C_LOOP=ON",
            "-DENABLE_WEBASSEMBLY=OFF",
        ]

# LTO broken on aarch64 (JIT segfault) and on riscv64 (broken in LLVM)
match self.profile().arch:
    case "aarch64" | "riscv64":
        options += ["!lto"]
    case _:
        configure_args += ["-DLTO_MODE=thin"]


def post_install(self):
    self.install_license("Source/WebCore/LICENSE-APPLE")
    self.install_license("Source/WebCore/LICENSE-LGPL-2.1")
    self.install_license("Source/WebCore/LICENSE-LGPL-2")


@subpackage("webkitgtk-devel")
def _(self):
    return self.default_devel()

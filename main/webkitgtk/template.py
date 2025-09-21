pkgname = "webkitgtk"
pkgver = "2.50.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DPORT=GTK",
    "-DCMAKE_SKIP_RPATH=ON",
    "-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib",  # XXX drop libexec
    f"-DCMAKE_LINKER={self.profile().triplet}-clang",
    # -DUSE_*
    "-DUSE_GTK4=OFF",
    "-DUSE_LD_LLD=ON",
    "-DUSE_LIBBACKTRACE=OFF",
    "-DUSE_SOUP2=OFF",
    "-DUSE_WOFF2=ON",
    "-DUSE_FLITE=OFF",
    "-DUSE_SPIEL=ON",
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
    "libxml2-progs",
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
license = "LGPL-2.1-or-later AND BSD-2-Clause"
url = "https://webkitgtk.org"
source = f"{url}/releases/webkitgtk-{pkgver}.tar.xz"
sha256 = "e564b8099f9a3ae32409539b290bbd2ad084e99b6d22d4aac5e51e4554df8bc2"
debug_level = 1  # otherwise LTO link runs out of memory + fat debuginfo
tool_flags = {
    "CFLAGS": ["-DNDEBUG"],
    "CXXFLAGS": [
        # also silence some really loud warnings...
        "-DNDEBUG",
        # libc++ >= 20 detects some overflows in std::span?
        "-D_LIBCPP_HARDENING_MODE=_LIBCPP_HARDENING_MODE_NONE",
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

if self.profile().arch == "loongarch64":
    tool_flags["CXXFLAGS"] += ["-DSIMDE_FLOAT16_API=SIMDE_FLOAT16_API_PORTABLE"]

# LTO broken on aarch64 (JIT segfault)
if self.has_lto(force=True) and self.profile().arch != "aarch64":
    configure_args += ["-DLTO_MODE=thin"]
else:
    options += ["!lto"]


def post_install(self):
    self.install_license("Source/WebCore/LICENSE-APPLE")
    self.install_license("Source/WebCore/LICENSE-LGPL-2.1")
    self.install_license("Source/WebCore/LICENSE-LGPL-2")


@subpackage("webkitgtk-devel")
def _(self):
    return self.default_devel()

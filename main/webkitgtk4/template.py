# mirrors the gtk3 webkitgtk template
pkgname = "webkitgtk4"
pkgver = "2.50.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DPORT=GTK",
    "-DCMAKE_SKIP_RPATH=ON",
    "-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib",  # XXX drop libexec
    f"-DCMAKE_LINKER={self.profile().triplet}-clang",
    # -DUSE_*
    "-DUSE_GTK4=ON",
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
    # conflicts with the gtk3 one
    "-DENABLE_WEBDRIVER=OFF",
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
    "gtk4-devel",
    "harfbuzz-devel",
    "hyphen-devel",
    "icu-devel",
    "lcms2-devel",
    "libavif-devel",
    "libepoxy-devel",
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
    "libxcomposite-devel",
    "libxdamage-devel",
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
pkgdesc = "GTK4 port of the WebKit browser engine"
license = "LGPL-2.1-or-later AND BSD-2-Clause"
url = "https://webkitgtk.org"
source = f"{url}/releases/webkitgtk-{pkgver}.tar.xz"
sha256 = "33e912ee6e3cdb4b9803715f50686af85a60af47f1cf72a6acc6a2db1bb3d9fe"
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

if self.profile().arch == "riscv64":
    # libpas/bmalloc link errors
    configure_args += ["-DUSE_SYSTEM_MALLOC=ON"]

# LTO broken on aarch64 (JIT segfault)
if self.has_lto(force=True) and self.profile().arch != "aarch64":
    configure_args += ["-DLTO_MODE=thin"]
else:
    options += ["!lto"]


def post_install(self):
    self.install_license("Source/WebCore/LICENSE-APPLE")
    self.install_license("Source/WebCore/LICENSE-LGPL-2.1")
    self.install_license("Source/WebCore/LICENSE-LGPL-2")


@subpackage("webkitgtk4-devel")
def _(self):
    return self.default_devel()

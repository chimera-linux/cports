pkgname = "qt6-qtbase"
pkgver = "6.5.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DINSTALL_DATADIR=share/qt6",
    "-DINSTALL_ARCHDATADIR=lib/qt6",
    "-DINSTALL_BINDIR=lib/qt6/bin",
    "-DINSTALL_PUBLICBINDIR=usr/bin",
    "-DINSTALL_DOCDIR=share/doc/qt6",
    "-DINSTALL_MKSPECSDIR=lib/qt6/mkspecs",
    "-DINSTALL_INCLUDEDIR=include/qt6",
    "-DINSTALL_EXAMPLESDIR=lib/qt6/examples",
    "-DINSTALL_TESTSDIR=lib/qt6/tests",
    "-DINSTALL_SYSCONFDIR=/etc/xdg",
    "-DQT_FEATURE_journald=OFF",
    "-DQT_FEATURE_reduce_relocations=OFF",
    "-DQT_FEATURE_openssl_linked=ON",
    "-DQT_FEATURE_system_xcb_xinput=ON",
    "-DQT_FEATURE_system_sqlite=ON",
    "-DQT_FEATURE_libproxy=ON",
    "-DQT_FEATURE_syslog=ON",
    "-DQT_FEATURE_vulkan=ON",
    "-DQT_FEATURE_qmake=ON",
    "-DQT_FEATURE_xcb=ON",
    "-DBUILD_WITH_PCH=OFF",
    "-DQT_BUILD_TESTS=ON",
]
hostmakedepends = ["cmake", "ninja", "perl", "pkgconf", "xmlstarlet"]
makedepends = [
    "zlib-devel", "libzstd-devel", "dbus-devel", "double-conversion-devel",
    "libxcb-devel", "xcb-util-image-devel", "xcb-util-keysyms-devel",
    "xcb-util-renderutil-devel", "xcb-util-wm-devel", "xcb-util-cursor-devel",
    "mesa-devel", "glib-devel", "pcre2-devel", "icu-devel", "mtdev-devel",
    "harfbuzz-devel", "libpng-devel", "tslib-devel", "libinput-devel",
    "gtk+3-devel", "cups-devel", "libproxy-devel", "brotli-devel",
    "sqlite-devel", "heimdal-devel", "libb2-devel", "libxkbcommon-devel",
    "wayland-devel", "linux-headers", "vulkan-headers", "vulkan-loader",
]
pkgdesc = "Qt application framework (6.x)"
license = "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtbase-everywhere-src-{pkgver}.tar.xz"
sha256 = "fde1aa7b4fbe64ec1b4fc576a57f4688ad1453d2fab59cbadd948a10a6eaf5ef"
debug_level = 1 # defatten, especially with LTO
# FIXME
hardening = ["!int"]
# TODO
options = ["!check", "!cross"]

if self.profile().arch == "riscv64":
    tool_flags = {
        "CXXFLAGS": ["-mno-relax"],
        "CFLAGS": ["-mno-relax"],
        "LDFLAGS": ["-mno-relax"]
    }

if self.profile().arch == "aarch64":
    configure_args += ["-DQT_FEATURE_opengles2=ON"]

if self.profile().cross:
    hostmakedepends += ["qt6-qtbase"]
    configure_args += ["-DQT_FORCE_BUILD_TOOLS=ON"]

def init_configure(self):
    if self.has_lto():
        self.configure_args += ["-DCMAKE_INTERPROCEDURAL_OPTIMIZATION=ON"]

def post_install(self):
    self.rm(self.destdir / "usr/tests", recursive = True)
    self.install_file(self.files_path / "target_qt.conf", "usr/lib/qt6/bin")
    # eliminate hardlinks
    for f in (self.destdir / "usr/lib/qt6/bin").glob("*6"):
        nsname = f.name.removesuffix("6")
        f.with_name(nsname).unlink()
        self.install_link(f.name, f"usr/lib/qt6/bin/{nsname}")

@subpackage("qt6-qtbase-gui")
def _gui(self):
    self.pkgdesc = f"{pkgdesc} (GUI)"

    return [
        "usr/lib/libQt6Gui.so.*",
        "usr/lib/libQt6XcbQpa.so.*",
        "usr/lib/libQt6EglFSDeviceIntegration.so.*",
        "usr/lib/libQt6EglFsKmsGbmSupport.so.*",
        "usr/lib/libQt6EglFsKmsSupport.so.*",
        "usr/lib/libQt6OpenGL.so.*",
        "usr/lib/qt6/plugins/generic",
        "usr/lib/qt6/plugins/platforms",
        "usr/lib/qt6/plugins/xcbglintegrations",
        "usr/lib/qt6/plugins/imageformats",
        "usr/lib/qt6/plugins/egldeviceintegrations",
        "usr/lib/qt6/plugins/platforminputcontexts",
        "usr/lib/qt6/plugins/platformthemes",
    ]

def _libpkg(name, libname, desc, extra = []):
    @subpackage(f"qt6-qtbase-{name}")
    def _sp(self):
        self.pkgdesc = f"{pkgdesc} ({desc})"
        return [f"usr/lib/libQt6{libname}.so.*"] + extra

for _sp in [
    ("opengl-widgets", "OpenGLWidgets", "OpenGL widgets"),
    ("dbus", "DBus", "DBus"),
    ("core", "Core", "Core"),
    ("printsupport", "PrintSupport", "Print support", [
        "usr/lib/qt6/plugins/printsupport"
    ]),
    ("concurrent", "Concurrent", "Concurrency"),
    ("widgets", "Widgets", "Widgets"),
    ("network", "Network", "Network", [
        "usr/lib/qt6/plugins/networkinformation",
        "usr/lib/qt6/plugins/tls",
    ]),
    ("sql", "Sql", "SQL", [
        "usr/lib/qt6/plugins/sqldrivers",
    ]),
    ("test", "Test", "Test"),
    ("xml", "Xml", "XML"),
]:
    _libpkg(*_sp)

@subpackage("qt6-qtbase-devel")
def _devel(self):
    self.depends += makedepends
    return self.default_devel(extra = [
        "usr/lib/qt6/metatypes",
        "usr/lib/qt6/mkspecs/modules",
        "usr/lib/qt6/modules",
        "usr/lib/*.prl",
    ])

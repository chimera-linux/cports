pkgname = "poppler"
pkgver = "25.04.0"
_test_commit = "91ee031c882634c36f2f0f2f14eb6646dd542fb9"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DENABLE_UNSTABLE_API_ABI_HEADERS=ON",
    "-DENABLE_BOOST=ON",
    "-DENABLE_CPP=ON",
    "-DENABLE_GLIB=ON",
    "-DENABLE_GOBJECT_INTROSPECTION=ON",
    "-DENABLE_NSS3=ON",
    "-DENABLE_UTILS=ON",
    "-DENABLE_QT5=OFF",
    "-DENABLE_QT6=ON",
]
hostmakedepends = [
    "cmake",
    "glib-devel",
    "gobject-introspection",
    "ninja",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "cairo-devel",
    "glib-devel",
    "gpgme-devel",
    "lcms2-devel",
    "curl-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libtiff-devel",
    "nss-devel",
    "openjpeg-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "PDF rendering library"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://poppler.freedesktop.org"
source = [
    f"{url}/poppler-{pkgver}.tar.xz",
    f"https://gitlab.freedesktop.org/poppler/test/-/archive/{_test_commit}/test-{_test_commit}.tar.gz",
]
source_paths = [".", "testdata"]
sha256 = [
    "b010c596dce127fba88532fd2f1043e55ea30601767952d0f2c0a80e7dc0da3d",
    "4155211ed0e5b05ffd0b57e7e4679215ba02c7f58fcd16e6b82844b2f6a6f590",
]
# check_qt6_goostring crashes
hardening = ["!int"]


def init_configure(self):
    self.configure_args.append(f"-DTESTDATADIR={self.chroot_srcdir}/testdata")


@subpackage("poppler-cpp-libs")
def _(self):
    self.subdesc = "C++ binding"
    # transitional
    self.provides = [self.with_pkgver("libpoppler-cpp")]

    return ["usr/lib/libpoppler-cpp.so.*"]


@subpackage("poppler-qt6-libs")
def _(self):
    self.subdesc = "Qt6 binding"
    # transitional
    self.provides = [
        self.with_pkgver("libpoppler-qt6"),
        self.with_pkgver("poppler-qt"),
    ]

    return ["usr/lib/libpoppler-qt6.so.*"]


@subpackage("poppler-glib-libs")
def _(self):
    self.subdesc = "GLib binding"
    # transitional
    self.provides = [self.with_pkgver("libpoppler-glib")]

    return ["usr/lib/libpoppler-glib.so.*", "usr/lib/girepository-1.0"]


@subpackage("poppler-libs")
def _(self):
    self.depends = ["poppler-data"]
    # transitional
    self.provides = [self.with_pkgver("libpoppler")]

    return self.default_libs()


@subpackage("poppler-devel")
def _(self):
    # transitional
    self.provides = [
        self.with_pkgver("libpoppler-devel"),
        self.with_pkgver("poppler-qt-devel"),
    ]

    return self.default_devel()

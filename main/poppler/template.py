pkgname = "poppler"
pkgver = "24.12.0"
_test_commit = "ff3133cdb6cb496ee1d2c3231bfa35006a5e8410"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://poppler.freedesktop.org"
source = [
    f"{url}/poppler-{pkgver}.tar.xz",
    f"https://gitlab.freedesktop.org/poppler/test/-/archive/{_test_commit}/test-{_test_commit}.tar.gz",
]
source_paths = [".", "testdata"]
sha256 = [
    "1cf374c3146f3f685d9257701bf0c2866c61d6c202c14d1f5c01a1f3a089028a",
    "98a06e7dd7619fe20bfd99505a31993dbe40517678d81278e6395a30a40f03bf",
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

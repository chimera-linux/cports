pkgname = "poppler"
pkgver = "26.08.0"
_test_commit = "48b6219b84fc0a708040cb279d51095cc4e1c603"
pkgrel = 0
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
    "curl-devel",
    "glib-devel",
    "gpgmepp-devel",
    "lcms2-devel",
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
    "dc906e68cea698109706ac6aa3d2c9d4512fcfcac42d90b8afcda486d1b9abd0",
    "233bbb47eb6972ace21e149a03e7ab7a6b19634365809891d094a91bbd25ac2c",
]
# check_qt6_goostring crashes
hardening = ["!int"]


def init_configure(self):
    self.configure_args.append(f"-DTESTDATADIR={self.chroot_srcdir}/testdata")


@subpackage("poppler-cpp-libs")
def _(self):
    self.subdesc = "C++ binding"
    self.renames = ["libpoppler-cpp"]

    return ["usr/lib/libpoppler-cpp.so.*"]


@subpackage("poppler-qt6-libs")
def _(self):
    self.subdesc = "Qt6 binding"
    self.renames = ["libpoppler-qt6", "poppler-qt"]

    return ["usr/lib/libpoppler-qt6.so.*"]


@subpackage("poppler-glib-libs")
def _(self):
    self.subdesc = "GLib binding"
    self.renames = ["libpoppler-glib"]

    return ["usr/lib/libpoppler-glib.so.*", "usr/lib/girepository-1.0"]


@subpackage("poppler-libs")
def _(self):
    self.depends = ["poppler-data"]
    self.renames = ["libpoppler"]

    return self.default_libs()


@subpackage("poppler-devel")
def _(self):
    self.renames = ["libpoppler-devel", "poppler-qt-devel"]

    return self.default_devel()

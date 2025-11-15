pkgname = "poppler"
pkgver = "25.11.0"
_test_commit = "9d5011815a14c157ba25bb160187842fb81579a5"
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
    "gpgme-devel",
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
    "63f155142b77349e2bccaef148e754e7506ab1641e713b83af4f54a8f8b15369",
    "c4cbdbf44f1d5c1ccbd7de611e979d97b703851970819cbb021f97218a445ed2",
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

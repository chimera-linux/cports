pkgname = "poppler"
pkgver = "24.05.0"
_test_commit = "400f3ff05b2b1c0ae17797a0bd50e75e35c1f1b1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DENABLE_UNSTABLE_API_ABI_HEADERS=ON",
    "-DENABLE_CPP=ON",
    "-DENABLE_GLIB=ON",
    "-DENABLE_GOBJECT_INTROSPECTION=ON",
    "-DENABLE_UTILS=ON",
    "-DENABLE_BOOST=ON",
    "-DENABLE_QT5=OFF",
    "-DENABLE_QT6=OFF",
    "-DENABLE_GPGME=OFF",  # creates a cycle
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
    "lcms2-devel",
    "libcurl-devel",
    "libpng-devel",
    "libtiff-devel",
    "nss-devel",
    "openjpeg-devel",
]
pkgdesc = "PDF rendering library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://poppler.freedesktop.org"
source = [
    f"{url}/{pkgname}-{pkgver}.tar.xz",
    f"https://gitlab.freedesktop.org/poppler/test/-/archive/{_test_commit}/test-{_test_commit}.tar.gz",
]
source_paths = [".", "testdata"]
sha256 = [
    "d8c5eb30b50285ad9f0af8c6335cc2d3b9597fca475cbc2598a5479fa379f779",
    "0d850a1d06944671c991be6822b7146ade401b06aad560ff39b254a028074525",
]


def init_configure(self):
    self.configure_args.append(
        f"-DTESTDATADIR=/builddir/{self.wrksrc}/testdata"
    )


@subpackage("libpoppler")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"
    self.depends = ["poppler-data"]

    return ["usr/lib/libpoppler.so.*"]


@subpackage("libpoppler-devel")
def _devel(self):
    self.pkgdesc = f"{pkgdesc} (development files)"

    return self.default_devel()


@subpackage("libpoppler-cpp")
def _cpp_lib(self):
    self.pkgdesc = f"{pkgdesc} (C++ binding)"

    return ["usr/lib/libpoppler-cpp.so.*"]


@subpackage("libpoppler-glib")
def _glib(self):
    self.pkgdesc = f"{pkgdesc} (GLib binding)"

    return ["usr/lib/libpoppler-glib.so.*", "usr/lib/girepository-1.0"]

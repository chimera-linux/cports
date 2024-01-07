pkgname = "poppler"
pkgver = "24.01.0"
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
    "ninja",
    "pkgconf",
    "gobject-introspection",
    "glib-devel",
]
makedepends = [
    "glib-devel",
    "cairo-devel",
    "lcms2-devel",
    "libcurl-devel",
    "boost-devel",
    "libpng-devel",
    "libtiff-devel",
    "openjpeg-devel",
    "nss-devel",
]
pkgdesc = "PDF rendering library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://poppler.freedesktop.org"
source = f"{url}/{pkgname}-{pkgver}.tar.xz"
sha256 = "c7def693a7a492830f49d497a80cc6b9c85cb57b15e9be2d2d615153b79cae08"
# needs unshipped sample files
options = ["!check"]


@subpackage("libpoppler")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"
    self.depends = ["poppler-data"]

    return ["usr/lib/libpoppler.so.*"]


@subpackage("libpoppler-devel")
def _devel(self):
    self.pkgdesc = f"{pkgdesc} (development files)"

    return [
        "usr/include/poppler/*.h",
        "usr/include/poppler/splash",
        "usr/include/poppler/fofi",
        "usr/include/poppler/goo",
        "usr/lib/libpoppler.so",
        "usr/lib/pkgconfig/poppler.pc",
    ]


@subpackage("libpoppler-cpp")
def _cpp_lib(self):
    self.pkgdesc = f"{pkgdesc} (C++ binding)"

    return ["usr/lib/libpoppler-cpp.so.*"]


@subpackage("libpoppler-cpp-devel")
def _cpp_devel(self):
    self.pkgdesc = f"{pkgdesc} (C++ development files)"
    self.depends += [f"libpoppler-devel={pkgver}-r{pkgrel}"]

    return [
        "usr/include/poppler/cpp",
        "usr/lib/libpoppler-cpp.so",
        "usr/lib/pkgconfig/poppler-cpp.pc",
    ]


@subpackage("libpoppler-glib")
def _glib(self):
    self.pkgdesc = f"{pkgdesc} (GLib binding)"

    return ["usr/lib/libpoppler-glib.so.*", "usr/lib/girepository-1.0"]


@subpackage("libpoppler-glib-devel")
def _glib_devel(self):
    self.pkgdesc = f"{pkgdesc} (GLib development files)"
    self.depends += [f"libpoppler-devel={pkgver}-r{pkgrel}"]

    return [
        "usr/include/poppler/glib",
        "usr/lib/libpoppler-glib.so",
        "usr/lib/pkgconfig/poppler-glib.pc",
        "usr/share/gir-1.0",
    ]

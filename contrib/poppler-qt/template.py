pkgname = "poppler-qt"
pkgver = "24.07.0"
_test_commit = "ff3133cdb6cb496ee1d2c3231bfa35006a5e8410"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DENABLE_CPP=OFF",
    "-DENABLE_GLIB=OFF",
    "-DENABLE_GOBJECT_INTROSPECTION=OFF",
    "-DENABLE_GPGME=OFF",
    "-DENABLE_LIBCURL=OFF",
    "-DENABLE_LIBTIFF=OFF",
    "-DENABLE_NSS3=OFF",
    "-DENABLE_QT5=OFF",
    "-DENABLE_UNSTABLE_API_ABI_HEADERS=ON",
    "-DENABLE_UTILS=OFF",
    # only qt6
    "-DENABLE_QT6=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "lcms2-devel",
    "libjpeg-turbo-devel",
    "libpoppler-devel",
    "openjpeg-devel",
    "qt6-qtbase-devel",
]
origin = "poppler"
pkgdesc = "PDF rendering library (Qt integration)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://poppler.freedesktop.org"
source = [
    f"{url}/poppler-{pkgver}.tar.xz",
    f"https://gitlab.freedesktop.org/poppler/test/-/archive/{_test_commit}/test-{_test_commit}.tar.gz",
]
source_paths = [
    ".",
    "testdata",
]
sha256 = [
    "19eb4f49198e4ae3fd9e5a6cf24d0fc7e674e8802046a7de14baab1e40cc2f1d",
    "98a06e7dd7619fe20bfd99505a31993dbe40517678d81278e6395a30a40f03bf",
]
# check_qt6_goostring crashes
hardening = ["!int"]


def init_configure(self):
    self.configure_args.append(f"-DTESTDATADIR={self.chroot_srcdir}/testdata")


def do_install(self):
    from cbuild.util import cmake

    cmake.install(self, f"{self.make_dir}/qt6")
    self.install_file(f"{self.make_dir}/poppler-qt6.pc", "usr/lib/pkgconfig")


@subpackage("poppler-qt-devel")
def _devel(self):
    self.depends += ["libpoppler-devel"]
    return self.default_devel()

pkgname = "gtar"
pkgver = "1.35"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--program-prefix=g",
    "gl_cv_struct_dirent_d_ino=yes",
]
configure_gen = []
hostmakedepends = ["texinfo"]
makedepends = ["acl-devel"]
pkgdesc = "GNU tape archiver"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/tar"
source = f"$(GNU_SITE)/tar/tar-{pkgver}.tar.xz"
sha256 = "4d62ff37342ec7aed748535323930c7cf94acf71c3591882b26a7ea50f3edc16"
hardening = ["vis", "cfi"]

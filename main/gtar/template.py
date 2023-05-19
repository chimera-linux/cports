pkgname = "gtar"
pkgver = "1.34"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--program-prefix=g",
    "gl_cv_struct_dirent_d_ino=yes",
]
hostmakedepends = ["texinfo"]
makedepends = ["acl-devel"]
pkgdesc = "GNU tape archiver"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/tar"
source = f"$(GNU_SITE)/tar/tar-{pkgver}.tar.xz"
sha256 = "63bebd26879c5e1eea4352f0d03c991f966aeb3ddeb3c7445c902568d5411d28"
hardening = ["vis", "cfi"]

configure_gen = []

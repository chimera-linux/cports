pkgname = "gsed"
pkgver = "4.9"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-acl",
    "--program-prefix=g",
    "gl_cv_func_working_acl_get_file=yes",
    "ac_cv_lib_error_at_line=no",
    "ac_cv_header_sys_cdefs_h=no",
]
hostmakedepends = ["texinfo"]
makedepends = ["acl-devel"]
checkdepends = ["perl", "bash"]
pkgdesc = "GNU stream editor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/sed"
source = f"$(GNU_SITE)/sed/sed-{pkgver}.tar.xz"
sha256 = "6e226b732e1cd739464ad6862bd1a1aba42d7982922da7a53519631d24975181"
hardening = ["vis", "cfi"]
# mostly only gnulib tests run as they are
options = ["!check"]

configure_gen = []

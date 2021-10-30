pkgname = "gsed"
pkgver = "4.8"
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
checkdepends = ["perl"]
pkgdesc = "GNU stream editor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/sed"
source = f"$(GNU_SITE)/sed/sed-{pkgver}.tar.xz"
sha256 = "f79b0cfea71b37a8eeec8490db6c5f7ae7719c35587f21edb0617f370eeff633"
# most sed tests need bash
options = ["!check"]

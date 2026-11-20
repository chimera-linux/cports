pkgname = "gsed"
pkgver = "4.10"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-acl",
    "--program-prefix=g",
    "gl_cv_func_working_acl_get_file=yes",
    "ac_cv_lib_error_at_line=no",
    "ac_cv_header_sys_cdefs_h=no",
]
# fails to regen due to gnulib stuff
configure_gen = []
hostmakedepends = ["automake", "gettext-devel", "texinfo"]
makedepends = ["acl-devel", "linux-headers"]
checkdepends = ["perl", "bash"]
pkgdesc = "GNU stream editor"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/sed"
source = f"$(GNU_SITE)/sed/sed-{pkgver}.tar.xz"
sha256 = "b8e72182b2ec96a3574e2998c47b7aaa64cc20ce000d8e9ac313cc07cecf28c7"
hardening = ["vis", "cfi"]
# mostly only gnulib tests run as they are
options = ["!check"]

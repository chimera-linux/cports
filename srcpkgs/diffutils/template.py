pkgname = "diffutils"
version = "3.7"
revision = 1
bootstrap = True
build_style = "gnu_configure"
configure_args = [
    "gl_cv_func_gettimeofday_clobber=no",
    "gl_cv_func_tzset_clobber=no",
    "ac_cv_lib_error_at_line=no",
    "ac_cv_header_sys_cdefs_h=no"
]
checkdepends = ["perl"]
short_desc = "The GNU diff utilities"
maintainer = "Enno Boland <gottox@voidlinux.org>"
license = "GPL-3.0-or-later"
homepage = "https://www.gnu.org/software/diffutils"

from cbuild import sites

distfiles = [f"{sites.gnu}/{pkgname}/{pkgname}-{version}.tar.xz"]
checksum = ["b3a7a6221c3dc916085f0d205abf6b8e1ba443d4dd965118da364a1dc1cb3a26"]

def pre_configure(self):
    if self.cross_build:
        self.configure_args.append("gl_cv_func_getopt_gnu=yes")

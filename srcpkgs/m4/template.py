pkgname = "m4"
version = "1.4.18"
revision = 2
bootstrap = True
build_style = "gnu_configure"
configure_args = [
    "--enable-changeword", "--enable-threads",
    "ac_cv_lib_error_at_line=no", "ac_cv_header_sys_cdefs_h=no"
]
short_desc = "GNU version of UNIX m4 macro language processor"
homepage = "https://www.gnu.org/software/m4/"
license = "GPL-3.0-or-later"
maintainer = "Enno Boland <gottox@voidlinux.org>"

from cbuild import sites

distfiles = [f"{sites.gnu}/{pkgname}/{pkgname}-{version}.tar.xz"]
checksum = ["f2c1e86ca0a404ff281631bdc8377638992744b175afb806e25871a24a934e07"]

if current.bootstrapping:
    # disable makeinfo always
    # texinfo defaults to utf-8 now and the file is in iso-8859-1
    # don't touch the file otherwise it will try to rebuild
    env = {"MAKEINFO": ":"}

pkgname = "chroot-grep"
version = "3.3"
revision = 1
wrksrc = f"grep-{version}"
bootstrap = True
build_style = "gnu_configure"
configure_args = [
    "--disable-perl-regexp", "--disable-nls", "ac_cv_path_GREP=grep",
    "ac_cv_lib_error_at_line=no", "ac_cv_header_sys_cdefs_h=no"
]
short_desc = "The GNU grep utility - for use with xbps-src"
maintainer = "Enno Boland <gottox@voidlinux.org>"
license = "GPL-3.0-or-later"
homepage = "http://www.gnu.org/software/grep/"

from cbuild import sites

distfiles = [f"{sites.gnu}/grep/grep-{version}.tar.xz"]
checksum = ["b960541c499619efd6afe1fa795402e4733c8e11ebf9fafccc0bb4bccdc5b514"]
conflicts = ["grep>=0"]
provides = [f"grep-{version}_{revision}"]

def post_install(self):
    self.rmtree("usr/share/info")
    self.rmtree("usr/share/man")

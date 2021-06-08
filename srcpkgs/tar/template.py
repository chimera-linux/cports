pkgname = "tar"
version = "1.34"
revision = 2
build_style = "gnu_configure"
configure_args = ["gl_cv_struct_dirent_d_ino=yes"]
makedepends = ["acl-devel"]
short_desc = "GNU tape archiver with remote magnetic tape support"
maintainer = "Enno Boland <gottox@voidlinux.org>"
license = "GPL-3.0-or-later"
homepage = "https://www.gnu.org/software/tar/"

from cbuild import sites

distfiles = [f"{sites.gnu}/tar/{pkgname}-{version}.tar.xz"]
checksum = ["63bebd26879c5e1eea4352f0d03c991f966aeb3ddeb3c7445c902568d5411d28"]

def pre_configure(self):
    import os
    # avoid regenerating doc on install
    st = os.stat(self.abs_wrksrc / "doc/stamp-vti")
    os.utime(self.abs_wrksrc / "configure", (st.st_atime, st.st_mtime))

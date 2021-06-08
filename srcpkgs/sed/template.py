pkgname = "sed"
version = "4.8"
revision = 1
bootstrap = True
build_style = "gnu_configure"
configure_args = ["--enable-acl", "gl_cv_func_working_acl_get_file=yes"]
makedepends = ["acl-devel"]
checkdepends = ["perl"]
short_desc = "The GNU stream editor"
maintainer = "Enno Boland <gottox@voidlinux.org>"
license = "GPL-3.0-or-later"
homepage = "http://www.gnu.org/software/sed"

from cbuild import sites

distfiles = [f"{sites.gnu}/{pkgname}/{pkgname}-{version}.tar.xz"]
checksum = ["f79b0cfea71b37a8eeec8490db6c5f7ae7719c35587f21edb0617f370eeff633"]

def post_extract(self):
    import re
    import os

    with open(self.abs_wrksrc / "Makefile.in") as ifile:
        with open(self.abs_wrksrc / "Makefile.in.new", "w") as ofile:
            for ln in ifile:
                ln = re.sub("(^doc/sed.1:).*$", r"\1", ln)
                ofile.write(ln)

    os.rename(
        self.abs_wrksrc / "Makefile.in.new", self.abs_wrksrc / "Makefile.in"
    )

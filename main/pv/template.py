pkgname = "pv"
pkgver = "1.9.34"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "gettext-devel"]
pkgdesc = "Tool for monitoring the progress of data through a pipeline"
license = "GPL-3.0-or-later"
url = "https://www.ivarch.com/programs/pv.shtml"
source = f"https://www.ivarch.com/programs/sources/pv-{pkgver}.tar.gz"
sha256 = "c0626bed6cbef5006b53d3281e8e3ae4b2838729462b21eccf28140eefef6bb1"


def post_extract(self):
    self.rm("po/Makefile.in.in")

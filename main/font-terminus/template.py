pkgname = "font-terminus"
pkgver = "4.49.1"
pkgrel = 2
build_style = "configure"
configure_args = [
    "--prefix=/usr",
    "--x11dir=/usr/share/fonts/misc",
    "--otbdir=/usr/share/fonts/misc",
]
make_build_args = ["all", "otb"]
make_install_args = ["install-otb"]
hostmakedepends = [
    "bdftopcf",
    "python",
]
pkgdesc = "Monospace bitmap font"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "OFL-1.1"
url = "https://terminus-font.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/terminus-font/terminus-font-{pkgver}.tar.gz"
sha256 = "d961c1b781627bf417f9b340693d64fc219e0113ad3a3af1a3424c7aa373ef79"
# no tests
options = ["!check"]


def post_install(self):
    self.install_file(
        "./75-yes-terminus.conf", "usr/share/fontconfig/conf.avail"
    )
    self.install_license("OFL.TXT")

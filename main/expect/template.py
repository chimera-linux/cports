pkgname = "expect"
pkgver = "5.45.4"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["expect_cv_wnohang_value=1"]
make_dir = "."
make_check_target = "test"
hostmakedepends = ["automake", "libtool", "tcl-devel"]
makedepends = ["tcl-devel"]
pkgdesc = "Programmed dialogue with interactive programs"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "http://www.nist.gov/el/msid/expect.cfm"
source = (
    f"$(SOURCEFORGE_SITE)/{pkgname}/Expect/{pkgver}/{pkgname}{pkgver}.tar.gz"
)
sha256 = "49a7da83b0bdd9f46d04a04deec19c7767bb9a323e40c4781f89caf760b92c34"
tool_flags = {"LDFLAGS": [f"-Wl,-rpath=/usr/lib:/usr/lib/{pkgname}{pkgver}"]}


def post_install(self):
    self.uninstall("usr/bin/weather")


@subpackage("expect-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return self.default_devel()

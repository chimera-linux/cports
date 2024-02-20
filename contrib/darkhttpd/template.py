pkgname = "darkhttpd"
pkgver = "1.15"
pkgrel = 0
build_style = "makefile"
make_use_env = True
pkgdesc = "Single-threaded static content webserver"
maintainer = "ttyyls <contact@behri.org>"
license = "ISC"
url = "https://unix4lyfe.org/darkhttpd"
source = f"https://github.com/emikulic/darkhttpd/archive/v{pkgver}.tar.gz"
sha256 = "ea48cedafbf43186f4a8d1afc99b33b671adee99519658446022e6f63bd9eda9"
hardening = ["vis", "cfi"]
# no tests defined
options = ["!check"]


def do_install(self):
    self.install_license("COPYING")
    self.install_bin("darkhttpd")
    self.install_service(self.files_path / "darkhttpd")
    self.install_file(
        self.files_path / "sysusers.conf",
        "usr/lib/sysusers.d",
        name="darkhttpd.conf",
    )
    self.install_file(
        self.files_path / "tmpfiles.conf",
        "usr/lib/tmpfiles.d",
        name="darkhttpd.conf",
    )
    self.install_file(
        self.files_path / "darkhttpd.default",
        "etc/default",
        name="darkhttpd",
    )

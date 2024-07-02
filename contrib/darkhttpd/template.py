pkgname = "darkhttpd"
pkgver = "1.16"
pkgrel = 0
build_style = "makefile"
make_use_env = True
pkgdesc = "Single-threaded static content webserver"
maintainer = "ttyyls <contact@behri.org>"
license = "ISC"
url = "https://unix4lyfe.org/darkhttpd"
source = f"https://github.com/emikulic/darkhttpd/archive/v{pkgver}.tar.gz"
sha256 = "ab97ea3404654af765f78282aa09cfe4226cb007d2fcc59fe1a475ba0fef1981"
hardening = ["vis", "cfi"]
# no tests defined
options = ["!check"]


def do_install(self):
    self.install_license("COPYING")
    self.install_bin("darkhttpd")
    self.install_service(self.files_path / "darkhttpd")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_file(
        self.files_path / "darkhttpd.default",
        "etc/default",
        name="darkhttpd",
    )

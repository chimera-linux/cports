pkgname = "agate"
pkgver = "3.3.7"
pkgrel = 0
build_style = "cargo"
make_check_args = ["--", "--test-threads=1"]
hostmakedepends = ["cargo", "pkgconf"]
makedepends = ["openssl-devel"]
pkgdesc = "Gemini hyptertext protocol server"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT OR Apache-2.0"
url = "https://github.com/mbrubeck/agate"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f106230720812eeaede897f6ccf7b2a498c84b5661e9b40902eb9a387df0367f"


def post_install(self):
    self.install_license("LICENSE-MIT")
    self.install_file(
        self.files_path / "sysusers.conf",
        "usr/lib/sysusers.d",
        name="agate.conf",
    )
    self.install_file(
        self.files_path / "tmpfiles.conf",
        "usr/lib/tmpfiles.d",
        name="agate.conf",
    )
    self.install_service(self.files_path / "agate")

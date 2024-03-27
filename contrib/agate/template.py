pkgname = "agate"
pkgver = "3.3.5"
pkgrel = 0
build_style = "cargo"
make_check_args = ["--", "--test-threads=1"]
hostmakedepends = ["cargo"]
pkgdesc = "Gemini hyptertext protocol server"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT OR Apache-2.0"
url = "https://github.com/mbrubeck/agate"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6db98b3b9ecb7b06a399aa2ca4e9fb77428f227524f95d8d3386319d91c851e7"


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

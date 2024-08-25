pkgname = "font-inter-variable"
pkgver = "4.0"
pkgrel = 0
pkgdesc = "Inter typeface family"
maintainer = "beb <beb_@tutamail.com>"
license = "OFL-1.1"
url = "https://rsms.me/inter"
source = f"https://github.com/rsms/inter/releases/download/v{pkgver}/Inter-{pkgver}.zip"
sha256 = "ff970a5d4561a04f102a7cb781adbd6ac4e9b6c460914c7a101f15acb7f7d1a4"


def do_install(self):
    for f in (self.cwd).glob("*.ttf"):
        self.install_file(f, "usr/share/fonts/inter-variable")

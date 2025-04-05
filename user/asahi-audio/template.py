pkgname = "asahi-audio"
pkgver = "3.1"
pkgrel = 0
archs = ["aarch64"]
build_style = "makefile"
depends = [
    "bankstown",
    "lsp-plugins-lv2",
    "pipewire",
    "speakersafetyd",
    "triforce",
    "wireplumber",
]
pkgdesc = "Asahi Linux userspace audio configuration"
license = "MIT"
url = "https://github.com/AsahiLinux/asahi-audio"
source = f"https://github.com/AsahiLinux/asahi-audio/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6c0c48df9585fd67c2582ca3c1ea33125cd83c7611ac34db0fb140705a4d9786"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

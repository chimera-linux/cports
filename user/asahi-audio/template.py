pkgname = "asahi-audio"
pkgver = "3.4"
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
sha256 = "b8417e214dfabaf1cadd0e162961e0341b0f1b864d2f865f2b101d7dce0c9eb1"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

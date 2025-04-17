pkgname = "asahi-audio"
pkgver = "3.3"
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
sha256 = "1de5033215dbadc8b0e388815575c0078daa168e83d05493419c19f383e7cbe2"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

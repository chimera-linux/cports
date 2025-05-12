pkgname = "fonts-intel-one-mono-otf"
pkgver = "1.4.0"
pkgrel = 0
pkgdesc = "Intel One Mono font"
license = "OFL-1.1"
url = "https://github.com/intel/intel-one-mono"
source = f"{url}/releases/download/V{pkgver}/otf.zip"
sha256 = "74ef8ee667403c760745bc12fc5e2cb1684544194fad3d5340919c173a8227fc"


def install(self):
    self.install_file("*.otf", "usr/share/fonts/intel-one-mono", glob=True)
    self.install_license("OFL.txt")

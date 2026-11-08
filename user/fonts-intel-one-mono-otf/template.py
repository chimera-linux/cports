pkgname = "fonts-intel-one-mono-otf"
pkgver = "1.5.0"
pkgrel = 0
pkgdesc = "Intel One Mono font"
license = "OFL-1.1"
url = "https://github.com/intel/intel-one-mono"
source = f"{url}/archive/refs/tags/V{pkgver}.tar.gz"
sha256 = "eecfab1296970d16baa21c0c1ac9fb3337caf38e21c78cd49d80d942b4d96619"


def install(self):
    self.install_file(
        "fonts/intel-one-mono-otf/*.otf",
        "usr/share/fonts/intel-one-mono",
        glob=True,
    )
    self.install_license("fonts/intel-one-mono-otf/OFL.txt")

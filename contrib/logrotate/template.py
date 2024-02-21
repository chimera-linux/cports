pkgname = "logrotate"
pkgver = "3.22.0"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = ["autoconf", "automake", "libtool"]
makedepends = ["acl-devel", "popt-devel"]
pkgdesc = "Tool to rotate logfiles"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/logrotate/logrotate"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f55b0f105f8ff145ea5b98166247d0c5d107f7fa8e8708130a2213dbde992db9"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
    self.install_file(
        self.files_path / "logrotate",
        "etc/cron.weekly",
        mode=0o755,
    )
    self.install_file(self.files_path / "logrotate.conf", "etc")
    self.install_dir("etc/logrotate.d", empty=True)

pkgname = "dracut-install"
pkgver = "107"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-dracut-cpio"]
configure_gen = []
make_dir = "."
make_build_target = "dracut-install"
hostmakedepends = ["bash", "pkgconf"]
makedepends = ["chimerautils-devel", "kmod-devel"]
checkdepends = ["asciidoc"]
pkgdesc = "Dracut-install command from dracut"
license = "GPL-2.0-or-later"
url = "https://github.com/dracut-ng/dracut"
# upstream renamed the GitHub repo dracut-ng/dracut-ng -> dracut-ng/dracut;
# same tag/commit, but GitHub's auto-generated archive now uses the new repo
# name for its internal top-level dir (dracut-107/ instead of
# dracut-ng-107/), which changes the tarball's bytes and thus its checksum.
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "fab19fb41d86de681c022d1a8798804595750be934d98a785ff0257dcdfc9a78"
hardening = ["vis", "cfi"]
# assumes rw filesystem
options = ["!check"]


def install(self):
    self.install_file("dracut-install", "usr/lib/dracut", mode=0o755)

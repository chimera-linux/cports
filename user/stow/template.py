pkgname = "stow"
pkgver = "2.4.1"
pkgrel = 0
build_style = "configure"
configure_args = ["--prefix=/usr/"]
hostmakedepends = ["perl"]
makedepends = ["perl"]
checkdepends = ["perl-io-stringy", "perl-test-output", "perl-capture-tiny"]
depends = ["perl", "perl-io-stringy"]
pkgdesc = "Symlink Farm Manager / Dotfiles Manager"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/stow"
source = f"https://ftp.gnu.org/gnu/stow/stow-{pkgver}.tar.gz"
sha256 = "2a671e75fc207303bfe86a9a7223169c7669df0a8108ebdf1a7fe8cd2b88780b"

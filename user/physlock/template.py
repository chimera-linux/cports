pkgname = "physlock"
pkgver = "13_git20200116"
pkgrel = 0
_gitrev = "4fbacee834abef613d7f4bd37d52a9f5fe269c82"
build_style = "makefile"
make_build_args = ["HAVE_SYSTEMD=0", "HAVE_ELOGIND=1"]
make_install_args = [*make_build_args]
makedepends = ["elogind-devel", "linux-headers", "linux-pam-devel"]
pkgdesc = "Lightweight Linux console locking tool"
license = "GPL-2.0-or-later"
url = "https://github.com/xyb3rt/physlock"
source = f"{url}/archive/{_gitrev}/physlock-{_gitrev}.tar.gz"
sha256 = "16dcfa06fd573d317078a4710eab7eff9a97715d666e26f6f21f1be4ba351663"
file_modes = {"usr/bin/physlock": ("root", "root", 0o4755)}
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]

pkgname = "meson"
pkgver = "1.4.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-devel",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python", "ninja"]
pkgdesc = "Meson build system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://mesonbuild.com"
source = f"https://github.com/mesonbuild/meson/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "1b8aad738a5f6ae64294cc8eaba9a82988c1c420204484ac02ef782e5bba5f49"
# meson is early in our bootstrap path but has a million checkdepends
options = ["!check"]


def post_install(self):
    # vim syntax
    self.install_dir("usr/share/vim/vimfiles")
    for f in ["ftdetect", "ftplugin", "indent", "syntax"]:
        self.install_files(
            f"data/syntax-highlighting/vim/{f}", "usr/share/vim/vimfiles"
        )
    with self.pushd("data/shell-completions"):
        self.install_completion("bash/meson", "bash")
        self.install_completion("zsh/_meson", "zsh")

pkgname = "mingw-w64-environment"
pkgver = "0.1"
pkgrel = 0
pkgdesc = (
    "Script providing common environment variables for Windows development"
)
license = "GPL-2.0-or-later"
url = "https://chimera-linux.org"


# TODO source from url release properly
def post_patch(self):
    self.cp(self.files_path / "mingw-env.sh", self.cwd)
    (self.cwd / "mingw-env.sh").chmod(0o755)


def install(self):
    self.install_bin("mingw-env.sh", name="mingw-env")

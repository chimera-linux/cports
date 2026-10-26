pkgname = "mingw-w64-meson"
pkgver = "1.0.0"
pkgrel = 0
build_style = "none"
# TODO maybe remove python makedep and source toolchain-generator directly to the template.py ???
makedepends = ["python"]
depends = ["meson", "mingw-w64-pkg-config", "clang-mingw-w64"]
pkgdesc = "Meson wrapper for MinGW"
license = "GPL-2.0-or-later"
url = "https://fedoraproject.org/wiki/MinGW"

_targets = ["x86_64", "i686", "aarch64", "armv7"]


def build(self):
    for an in _targets:
        at = an + "-w64-mingw32"
        self.cp(self.sources_path / "toolchain_generator.py", self.build_wrksrc)
        self.do(
            "python",
            "toolchain_generator.py",
            "--arch",
            f"{at}",
            "--output-file",
            f"toolchain-{at}.meson",
        )
        self.do(
            "sed",
            f"s|@TRIPLE@|{at}|g;",
            self.files_path / "meson-mingw-wrapper",
            ">",
            f"{at}-meson",
        )


def install(self):
    for an in _targets:
        at = an + "-w64-mingw32"
        self.install_bin(
            self.files_path / "toolchain_generator.py",
            name="meson-cross-file-generator",
        )
        self.install_dir("/usr/share/mingw")
        self.install_file(f"toolchain-{at}.meson", "/usr/share/mingw")
        self.install_bin(f"{at}-meson")

pkgname = "plan9port"
pkgver = "0_git20240110"
pkgrel = 1
_commit = "be7c68f6954f7dcaa53403e0f600716f65a13d32"
hostmakedepends = ["perl"]
makedepends = [
    "fontconfig-devel",
    "freetype-devel",
    "libx11-devel",
    "libxext-devel",
    "libxt-devel",
    "linux-headers",
]
pkgdesc = "Port of programs from Plan 9"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MIT"
url = "https://9fans.github.io/plan9port"
source = f"https://github.com/9fans/plan9port/archive/{_commit}.zip"
sha256 = "931b96e814b31769bf62b2ef2189ac2f474207d079932987c468b1c86854fb39"
options = ["!cross", "!lintstatic"]


def do_configure(self):
    with open(self.cwd / "LOCAL.config", "w") as config:
        config.write(f"CC9=" + self.get_tool("CC") + "\n")
        config.write(
            f"CC9FLAGS='"
            + self.get_cflags(shell=True)
            + " "
            + self.get_ldflags(shell=True)
            + "'\n"
        )


def do_build(self):
    self.do("./INSTALL", "-b", env={"NPROC": str(self.make_jobs)})


def do_install(self):
    self.do("./INSTALL", "-c", env={"PLAN9_TARGET": "/usr/lib/plan9"})

    self.install_license("LICENSE")
    self.rm("LICENSE")

    self.rm(".github", recursive=True)
    self.rm(".gitignore")
    self.rm("configure")
    self.rm("Makefile")
    self.rm("install.log")
    self.rm("install.sum")
    self.rm("install.txt")
    self.rm("*.patch", glob=True)

    self.install_files(".", "usr/lib", name="plan9")

    self.install_dir("usr/bin")
    self.install_link("../lib/plan9/bin/9", "usr/bin/9")
    self.install_file(
        self.files_path / "acme.desktop", "usr/share/applications"
    )

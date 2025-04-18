pkgname = "cgit-pink"
pkgver = "1.4.1"
_gitver = "2.37.1"
pkgrel = 0
build_style = "makefile"
makedepends = ["openssl3-devel", "pcre2-devel", "zlib-ng-compat-devel"]
checkdepends = ["git"]
pkgdesc = "Updated fork of cgit, a web frontend for git"
license = "GPL-2.0-only"
url = "https://git.causal.agency/cgit-pink/about"
source = [
    f"https://git.causal.agency/cgit-pink/snapshot/cgit-pink-{pkgver}.tar.gz",
    f"https://www.kernel.org/pub/software/scm/git/git-{_gitver}.tar.xz",
]
source_paths = [".", "git"]
sha256 = [
    "f1246c6c81305800c24e7eee2b224319ab5e57b1ddb07b4883aea845f29046d5",
    "c8162c6b8b8f1c5db706ab01b4ee29e31061182135dc27c4860224aaec1b3500",
]


def pre_configure(self):
    (self.cwd / "cgit.conf").write_text(
        f"""
CC = {self.get_tool("CC")}
AR = {self.get_tool("AR")}
CFLAGS = {self.get_cflags(shell=True)}
LDFLAGS = {self.get_ldflags(shell=True)}
HOST_CPU = {self.profile().arch}
CGIT_SCRIPT_PATH = /usr/bin
CGIT_DATA_PATH = /usr/share/cgit
filterdir = /usr/share/cgit/filters
        """
    )
    (self.cwd / "git/config.mak").write_text(
        """
USE_LIBPCRE2 = Yes
NO_REGEX = Yes
        """
    )


def post_install(self):
    self.install_man("cgitrc.5.txt", "cgitrc", 5)


def check(self):
    (self.cwd / "cgitrc").write_text(f"scan-path={self.chroot_cwd}")
    self.mkdir("testrepo")
    self.do(
        "git",
        "init",
        "--bare",
        "-b",
        "trunk",
        wrksrc="testrepo",
    )
    response = self.do(
        "./cgit",
        env={
            "PATH_INFO": "/testrepo",
            "CGIT_CONFIG": f"{self.chroot_cwd}/cgitrc",
        },
        capture_output=True,
    )
    headers = response.stdout.decode().split("\r\n", 1)[0]
    for line in headers.split("\r\n"):
        key, value = line.split(": ", 1)
        if key.lower() == "status" and not value.startswith("200"):
            self.error(f"test call returned status {value}")


@subpackage("cgit-pink-filters")
def _(self):
    self.subdesc = "included filters"
    self.depends = [
        "mandoc",
        "python-docutils",
        "python-markdown",
        "python-pygments",
    ]
    return ["usr/share/cgit/filters"]

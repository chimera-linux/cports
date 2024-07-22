pkgname = "sauerbraten"
pkgver = "2020.12.29"
pkgrel = 1
build_wrksrc = "src"
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["gmake"]
makedepends = [
    "sdl-devel",
    "sdl_image-devel",
    "sdl_mixer-devel",
    "zlib-ng-compat-devel",
]
depends = [f"sauerbraten-data={pkgver}-r{pkgrel}"]
pkgdesc = "Free FPS game, successor to Cube"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Zlib"
url = "http://sauerbraten.org"
source = f"$(SOURCEFORGE_SITE)/sauerbraten/sauerbraten_{pkgver.replace('.', '_')}_linux.tar.bz2"
sha256 = "cdba7c4a47cefd30d0afdd6a912199a1384319cf1619923cb7189e72e468be70"
hardening = ["!int"]
# no tests
options = ["!check", "!cross"]


def post_install(self):
    # binaries
    self.install_bin("../bin_unix/native_client", name="sauer_client")
    self.install_bin("../bin_unix/native_server", name="sauer_server")
    # wrappers
    self.install_file("../server-init.cfg", "etc/sauerbraten")
    self.install_bin(self.files_path / "sauerbraten")
    self.install_bin(self.files_path / "sauerbraten-server")
    # data
    self.install_dir("usr/share/sauerbraten")
    self.install_files("../data", "usr/share/sauerbraten")
    self.install_files("../packages", "usr/share/sauerbraten")


@subpackage("sauerbraten-data")
def _data(self):
    self.subdesc = "data files"

    return ["usr/share/sauerbraten"]


@subpackage("sauerbraten-server")
def _server(self):
    self.subdesc = "dedicated server"

    return [
        "etc",
        "usr/bin/sauer_server",
        "usr/bin/sauerbraten-server",
    ]

pkgname = "nyagetty"
pkgver = "2.38.99"
pkgrel = 6
build_style = "meson"
hostmakedepends = ["meson"]
makedepends = ["dinit-chimera", "linux-headers"]
depends = ["cmd:login!shadow"]
pkgdesc = "Standalone util-linux agetty"
license = "0BSD"
url = "https://github.com/chimera-linux/nyagetty"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7033d6840f839a6ad6d788d92f45efd0bb10c835c0560dba5d15ad8a6b9dff90"
hardening = ["vis", "cfi"]


def post_install(self):
    # agetty dinit helper
    self.install_file(self.files_path / "dinit-agetty", "usr/lib", mode=0o755)
    # agetty conf wrapper
    self.install_file(self.files_path / "agetty-default", "usr/lib", mode=0o755)
    self.install_file(self.files_path / "agetty-serial", "usr/lib", mode=0o755)
    self.install_file(
        self.files_path / "agetty-service.sh",
        "usr/lib",
        name="agetty-service",
        mode=0o755,
    )
    # core services
    self.install_service(self.files_path / "agetty", enable=True)
    self.install_service(self.files_path / "agetty-service")


@subpackage("nyagetty-dinit")
def _(self):
    self.subdesc = "service files"

    self.depends = [self.parent, "dinit-chimera"]
    self.install_if = [self.parent, "dinit-chimera"]

    return ["usr/lib/dinit.d/agetty*", "usr/lib/dinit-agetty"]

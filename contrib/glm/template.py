pkgname = "glm"
pkgver = "0.9.9.8"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf", "dos2unix"]
pkgdesc = "OpenGL Mathematics"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/g-truc/glm"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.zip"
sha256 = "37e2a3d62ea3322e43593c34bae29f57e3e251ea89f4067506c94043769ade4c"
hardening = ["!int"]


def do_install(self):
    self.install_license("copying.txt")

    self.install_dir("usr/include")
    self.install_dir("usr/lib/cmake")
    self.install_dir("usr/share/pkgconfig")

    # does not provide an install target
    self.install_files("glm", "usr/include")
    self.install_files("cmake/glm", "usr/lib/cmake")
    self.rm(self.destdir / "usr/include/glm/CMakeLists.txt")

    # pkgconf file
    with open(self.destdir / "usr/share/pkgconfig/glm.pc", "w") as pcf:
        pcf.write(
            f"""prefix=/usr
includedir=${{prefix}}/include

Name: GLM
Description: OpenGL Mathematics
Version: {pkgver}
Cflags: -I${{includedir}}
"""
        )

    # convert line endings
    for f in (self.destdir / "usr/include").rglob("*"):
        if f.is_file() and not f.is_symlink():
            self.do(
                "dos2unix", self.chroot_destdir / f.relative_to(self.destdir)
            )

pkgname = "stb"
pkgver = "0_git20230129"
_commit = "5736b15f7ea0ffb08dd38af21067c314d6a3aae9"
pkgrel = 0
hostmakedepends = ["pkgconf"]
pkgdesc = "Single-header libraries for C/C++"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/nothings/stb"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "d00921d49b06af62aa6bfb97c1b136bec661dd11dd4eecbcb0da1f6da7cedb4c"


def install(self):
    self.install_file("stb_*", "usr/include", glob=True)
    self.install_file("docs/*", "usr/share/doc/stb", glob=True)
    self.install_license("LICENSE")
    # .pc file
    self.install_dir("usr/lib/pkgconfig")
    with open(self.destdir / "usr/lib/pkgconfig/stb.pc", "w") as outf:
        outf.write(
            f"""prefix=/usr
includedir=${{prefix}}/include

Name: stb
Description: {pkgdesc}
Cflags: -I${{includedir}}
Version: {pkgver}
"""
        )

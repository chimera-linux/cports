pkgname = "stb"
pkgver = "0_git20250512"
_commit = "802cd454f25469d3123e678af41364153c132c2a"
pkgrel = 0
hostmakedepends = ["pkgconf"]
pkgdesc = "Single-header libraries for C/C++"
license = "MIT"
url = "https://github.com/nothings/stb"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "d7f870bbe53a4171d5d5526043926b2f26194e6b08de63fc3f1cf4b54e5d5249"


def install(self):
    self.install_file("*.h", "usr/include", glob=True)
    self.install_file("deprecated/*.h", "usr/include", glob=True)
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
